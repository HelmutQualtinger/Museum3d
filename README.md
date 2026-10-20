# 3D Museum

A walkable 3D art gallery in the browser — five themed halls (Portrait, Landscape, Modern, Sculpture, Gauguin), forty paintings, a live-rendered Mandelbrot spiral and two 3D sculptures, built with [Three.js](https://threejs.org/). Single self-contained `index.html`, no build step, no dependencies to install.

**[Live demo →](https://helmutqualtinger.github.io/Museum3d/)**

![The gallery, looking through all three halls](docs/screenshot.jpg)

## Features

- Navigation that follows familiar web conventions — drag to look, click the floor to walk there, click a painting to view it
- Five galleries: Portrait, Landscape and Modern art in an enfilade, plus a Sculpture hall behind and a Gauguin hall in front of the Landscape hall — each with its own accent color and lighting, joined by wide doorways
- Polished marble floor in a checkerboard of light and grey slabs, generated procedurally at startup — no texture files to download
- Forty paintings loaded from Wikimedia Commons, each lit by a narrow spot that picks out the artwork without washing it out
- Two 3D sculptures in the Sculpture hall: Michelangelo's David and the golden mask of Tutankhamun
- Hovering a painting shows its title and artist; clicking walks you up to it, even from another hall
- Collision detection against walls so you can't walk through them
- Works on touch devices: drag to look, tap to select
- Open Graph / Twitter Card metadata, so shared links render a preview card

## Controls

| Action | Input |
| --- | --- |
| Look around | Drag (the scene follows your pointer, like a map) |
| Walk to a spot | Click the floor there |
| View a painting | Click it — you'll be walked in front of it |
| Leave the close-up | Click beside the painting, the **← Zurück** button, or `Esc` |
| Move | `W` `A` `S` `D` / arrow keys, or the scroll wheel |
| Menu | `Esc` |

## The collection

| Hall | Works |
| --- | --- |
| I — Porträt | Mona Lisa · Mädchen mit dem Perlenohrring · Selbstbildnis (Rembrandt) · Selbstbildnis (van Gogh) · Die Arnolfini-Hochzeit |
| II — Landschaft | Sternennacht · Impression, Sonnenaufgang · Der Wanderer über dem Nebelmeer · Die große Welle vor Kanagawa · Die letzte Fahrt der Temeraire |
| III — Moderne | Der Kuss · Der Schrei · Blaues Pferd I · Komposition VIII · Komposition II in Rot, Blau und Gelb |
| IV — Skulptur | *David* (3D) · *Goldmaske des Tutanchamun* (3D) · Dame mit dem Hermelin · Das Abendmahl · Johannes der Täufer · Die Verkündigung · Felsgrottenmadonna (Leonardo) · Die Erschaffung Adams · Tondo Doni · Die Delphische Sibylle · Das Jüngste Gericht (Michelangelo) |
| V — Gauguin | Vision nach der Predigt · Ia Orana Maria · Woher kommen wir? Wer sind wir? Wohin gehen wir? · Arearea · Der gelbe Christus · Selbstbildnis · Manaò tupapaú · Zwei Tahitianerinnen |

Halls I–III also carry further works on their head and dividing walls (Klimt, Dürer, Matisse, Klee, Whistler, Monet, Constable, Rousseau), and hall III a Mandelbrot spiral rendered in real time by a GPU shader with relief shading — no image file. In its close-up you can zoom roughly 10²³-fold into the fractal: a BigInt reference orbit on the CPU plus perturbation theory on the GPU keeps it sharp far beyond float32 precision.

All images are public-domain reproductions served from Wikimedia Commons.

3D models (in `models/`, Draco-compressed GLB):

- **David** — [Scan the World](https://www.myminifactory.com/scantheworld/), via [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:David_(Michelangelo).stl), CC BY-SA 4.0; decimated to ~144k triangles
- **Tutankhamun mask** — [vmmaniac on Sketchfab](https://sketchfab.com/3d-models/tutankhamun-mask-hunyuan-f79ba82300cc4b9b9637d94f8959e970), CC BY 4.0 (an AI-assisted reconstruction, not a scan); textures reduced to 1024 px

## Running locally

This is a single static HTML file — just open it in a browser, or serve it locally:

```bash
python3 -m http.server 8000
```

Then visit `http://localhost:8000`.

## Tech

- [Three.js](https://threejs.org/) r160, loaded via CDN import map — no npm install required
- Vanilla JavaScript (ES modules), no framework
- Artwork textures loaded on demand from Wikimedia Commons
