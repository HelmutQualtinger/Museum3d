# 3D Museum

A walkable 3D art gallery in the browser — six themed halls (Portrait, Landscape, Modern, Sculpture, Gauguin, Cave painting), forty-nine pictures, a live-rendered Mandelbrot spiral and four 3D sculptures, built with [Three.js](https://threejs.org/). Single self-contained `index.html`, no build step, no dependencies to install.

**[Live demo →](https://helmutqualtinger.github.io/Museum3d/)**

![The gallery, looking through all three halls](docs/screenshot.jpg)

## Features

- Navigation that follows familiar web conventions — drag to look, click the floor to walk there, click a painting to view it
- Six galleries: Portrait, Landscape and Modern art in an enfilade, plus a Sculpture hall behind and a Gauguin hall in front of the Landscape hall, and a Cave-painting hall in front of that — each with its own accent color and lighting, joined by wide doorways
- Polished marble floor in a checkerboard of light and grey slabs, generated procedurally at startup — no texture files to download
- Forty-nine pictures loaded from Wikimedia Commons, each lit by a narrow spot that picks out the artwork without washing it out
- Five 3D objects, each slowly turning on a turntable: Michelangelo's David in the Sculpture hall, the golden mask of Tutankhamun and the bust of Nefertiti (both enlarged threefold — Nefertiti wearing sunglasses, Tutankhamun smoking a glowing cigarette) in the Portrait hall, and the Venus of Willendorf enlarged twelvefold (1.33 m instead of 11 cm) in the Cave-painting hall, plus the parametric vase *Evolution* (80 cm, brushed copper, with a procedurally built sunflower) in the Modern hall
- Hovering a painting shows its title and artist; clicking walks you up to it, even from another hall
- Every painting and sculpture has a short German explanation of the work and the artist — open it with **ⓘ Über das Werk** in the close-up or by clicking a sculpture — and can be read aloud with the browser's most natural German voice
- Collision detection against walls so you can't walk through them; benches are no obstacle — you step over them
- Quiet cool jazz in the background, synthesised live in the browser (electric piano, walking bass, brushes, vibraphone — no vocals, no audio files); toggle it with the ♪ button
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
| I — Porträt | *Goldmaske des Tutanchamun* (3D, 3×) · *Büste der Nofretete* (3D, 3×) · Mona Lisa · Mädchen mit dem Perlenohrring · Selbstbildnis (Rembrandt) · Selbstbildnis (van Gogh) · Die Arnolfini-Hochzeit |
| II — Landschaft | Sternennacht · Impression, Sonnenaufgang · Der Wanderer über dem Nebelmeer · Die große Welle vor Kanagawa · Die letzte Fahrt der Temeraire |
| III — Moderne | *Vase „Evolution“ mit Sonnenblume* (3D, 4×, Kupfer) · Der Kuss · Der Schrei · Blaues Pferd I · Komposition VIII · Komposition II in Rot, Blau und Gelb |
| IV — Skulptur | *David* (3D) · Dame mit dem Hermelin · Das Abendmahl · Johannes der Täufer · Die Verkündigung · Felsgrottenmadonna (Leonardo) · Die Erschaffung Adams · Tondo Doni · Die Delphische Sibylle · Das Jüngste Gericht (Michelangelo) |
| V — Gauguin | Vision nach der Predigt · Ia Orana Maria · Woher kommen wir? Wer sind wir? Wohin gehen wir? · Arearea · Der gelbe Christus · Selbstbildnis · Manaò tupapaú · Zwei Tahitianerinnen |
| VI — Höhlenmalerei | *Venus von Willendorf* (3D, 4×) · Lascaux: Saal der Stiere (3 Ausschnitte), Das „Chinesische Pferd“ · Chauvet: Pferdefries, Löwenfries · Niaux: Bisons im Salon noir, Zwei Bisons · Pech Merle: Gefleckte Pferde |

Halls I–III also carry further works on their head and dividing walls (Klimt, Dürer, Matisse, Klee, Whistler, Monet, Constable, Rousseau), and hall III a Mandelbrot spiral rendered in real time by a GPU shader with relief shading — no image file. In its close-up you can zoom roughly 10²³-fold into the fractal: a BigInt reference orbit on the CPU plus perturbation theory on the GPU keeps it sharp far beyond float32 precision.

All images are served from Wikimedia Commons. The paintings are public-domain reproductions; most cave-painting photos show museum replicas (Anthropos Brno, public domain). Three photos are CC BY-SA: *Pferdefries* (Chauvet) by Thomas T. (2.0), *Gefleckte Pferde* (Pech Merle) by Céréales Killer (4.0), *Zwei Bisons* (Niaux) by Christelle Molinié (4.0).

3D models (in `models/`, Draco-compressed GLB):

- **David** — [Scan the World](https://www.myminifactory.com/scantheworld/), via [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:David_(Michelangelo).stl), CC BY-SA 4.0; decimated to ~144k triangles
- **Tutankhamun mask** — [vmmaniac on Sketchfab](https://sketchfab.com/3d-models/tutankhamun-mask-hunyuan-f79ba82300cc4b9b9637d94f8959e970), CC BY 4.0 (an AI-assisted reconstruction, not a scan); textures reduced to 1024 px
- **Venus of Willendorf** — [Scan the World](https://www.myminifactory.com/scantheworld/), via [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Scan_the_World_-_Venus_of_Willendorf.stl), CC BY-SA 4.0; decimated to 110k triangles, shown at 12× the original 11 cm
- **Nefertiti** — the Egyptian Museum Berlin's own colour scan (3D model by Trigon Art, Berlin 2008, © Ägyptisches Museum und Papyrussammlung, Staatliche Museen zu Berlin – Preußischer Kulturbesitz), released after a freedom-of-information request by [Cosmo Wenman](https://www.thingiverse.com/thing:3974391) (mirror on the [Internet Archive](https://archive.org/details/thingiverse-3974391)), [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/); decimated from 6.4M to 128k triangles, colour texture reduced to 2048 px WebP. The derived `models/nofretete-berlin.glb` is under the same licence, non-commercial use only
- **Vase „Evolution“** — own parametric design from the `Allerlei` project (Python: spline loft triangle → circle, lettering with manifold3d), 200 mm STL rotated to Y-up, welded and simplified to 142k triangles, Draco; shown at 80 cm with a procedural brushed-copper material and a sunflower built from geometry and painted canvas textures

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
