# 3D Museum

A walkable 3D art gallery in the browser — three themed halls (Portrait, Landscape, Modern), nine masterpieces, built with [Three.js](https://threejs.org/). Single self-contained `index.html`, no build step, no dependencies to install.

**[Live demo →](https://helmutqualtinger.github.io/Museum3d/)**

## Features

- First-person walkthrough with mouse-look and click-and-drag movement (WASD also supported)
- Three galleries: Portrait, Landscape, and Modern art, each with its own accent color and lighting
- High-resolution paintings loaded from Wikimedia Commons, spotlit on the gallery walls
- Double-click a painting for a close-up view
- Collision detection against walls so you can't walk through them

## Controls

| Action | Input |
|---|---|
| Look around | Move mouse |
| Walk | Hold left mouse button and drag |
| Walk (alternative) | `W` `A` `S` `D` / arrow keys |
| Close-up view | Double-click a painting |
| Menu | `Esc` |

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
