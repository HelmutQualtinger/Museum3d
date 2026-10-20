# Rendert das Mandelbrot-Relief für Saal III:
#   python3 art/mandelbrot.py 3840 2560 2 out.png   (Breite, Höhe, Supersampling, Ausgabe)
# danach mit sips auf 500/1280/1920/3840 px als art/<w>px-mandelbrot-relief.jpg ablegen.
# Mandelbrot-Menge mit Relief-Beleuchtung (Normal-Map aus der Ableitung dz/dc),
# Farbe aus geglätteter Iterationszahl. Rendert supersampled und skaliert herunter.
import sys, time
import numpy as np
from PIL import Image

W, H = int(sys.argv[1]), int(sys.argv[2])
SS = int(sys.argv[3]) if len(sys.argv) > 3 else 2
out = sys.argv[4]
CX, CY, SPAN = -0.745, 0.0, 3.05          # Bildmitte, Breite in der Ebene
MAXIT, R = 1500, 100.0
ANGLE = np.deg2rad(45)                     # Lichtrichtung
LV = np.exp(1j * ANGLE)
H2 = 0.9                                   # Lichthöhe

def palette(t):
    # warmes Gold → Kupfer → tiefes Blau, zyklisch
    t = t % 1.0
    stops = np.array([
        [0.00, 0.02, 0.05, 0.16],
        [0.16, 0.09, 0.27, 0.52],
        [0.42, 0.93, 0.85, 0.62],
        [0.64, 0.86, 0.52, 0.16],
        [0.86, 0.36, 0.11, 0.07],
        [1.00, 0.02, 0.05, 0.16],
    ])
    rgb = np.empty(t.shape + (3,))
    for k in range(3):
        rgb[..., k] = np.interp(t, stops[:, 0], stops[:, k + 1])
    return rgb

def render_rows(y0, y1, w, h):
    xs = CX + (np.arange(w) + 0.5 - w / 2) * (SPAN / w)
    ys = CY - (np.arange(y0, y1) + 0.5 - h / 2) * (SPAN / w)
    c = xs[None, :] + 1j * ys[:, None]
    z = np.zeros_like(c); dz = np.zeros_like(c)
    n = np.full(c.shape, -1.0)
    zf = np.zeros_like(c); dzf = np.zeros_like(c)
    # Hauptkardioide und Periode-2-Kreis sind sicher innen — spart den Großteil der Rechenzeit
    q = (c.real - 0.25) ** 2 + c.imag ** 2
    inside = (q * (q + (c.real - 0.25)) < 0.25 * c.imag ** 2) | ((c.real + 1) ** 2 + c.imag ** 2 < 1 / 16)
    idx = np.flatnonzero(~inside)
    cc = c.ravel()[idx]; zz = np.zeros_like(cc); dd = np.zeros_like(cc)
    for it in range(MAXIT):
        dd = 2 * zz * dd + 1
        zz = zz * zz + cc
        esc = (zz.real ** 2 + zz.imag ** 2) > R * R
        if esc.any():
            e = idx[esc]
            n.ravel()[e] = it
            zf.ravel()[e] = zz[esc]; dzf.ravel()[e] = dd[esc]
            keep = ~esc
            idx, cc, zz, dd = idx[keep], cc[keep], zz[keep], dd[keep]
        if idx.size == 0:
            break
    rgb = np.zeros(c.shape + (3,))
    m = n >= 0
    zm, dm = zf[m], dzf[m]
    # geglättete Iteration
    nu = n[m] + 1 - np.log(np.log(np.abs(zm))) / np.log(2)
    # Relief: Normale aus z/dz
    u = zm / dm
    u = u / np.abs(u)
    refl = (u.real * LV.real + u.imag * LV.imag + H2) / (1 + H2)
    refl = np.clip(refl, 0, 1)
    col = palette(np.log(nu + 1) * 1.1 + 0.55)
    shade = 0.08 + 1.05 * refl
    spec = np.clip(refl, 0, 1) ** 24 * 0.35
    rgb[m] = np.clip(col * shade[:, None] + spec[:, None], 0, 1)
    rgb[~m] = [0.015, 0.012, 0.02]
    return rgb

t0 = time.time()
w, h = W * SS, H * SS
img = np.zeros((h, w, 3))
step = 256
for y in range(0, h, step):
    img[y:y + step] = render_rows(y, min(y + step, h), w, h)
    print(f'{y}/{h} {time.time() - t0:.0f}s', flush=True)
if SS > 1:
    img = img.reshape(H, SS, W, SS, 3).mean(axis=(1, 3))
img = (np.clip(img, 0, 1) ** (1 / 1.0) * 255 + 0.5).astype(np.uint8)
Image.fromarray(img).save(out, quality=92)
print('done', time.time() - t0)
