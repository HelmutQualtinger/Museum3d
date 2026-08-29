# CLAUDE.md

Guidance for Claude Code when working in this repository.

## Project

A walkable 3D art museum rendered entirely client-side with Three.js. The whole app — markup, styles, and logic — lives in a single file: `index.html`. There is no build step, no package.json, and no bundler; Three.js is loaded from a CDN via an import map.

## Architecture (all in `index.html`)

- **Data**: `ROOMS` array defines three galleries (Portrait, Landscape, Modern), each with an accent color, floor color, and three paintings (title, artist, image URL, aspect ratio).
- **Scene setup**: standard Three.js scene/camera/renderer boilerplate, ACES tone mapping, fog for depth.
- **Room construction** (`buildRoom`): builds floor, ceiling with light panels, front/back walls (two-tone: accent lower band, light upper band), side walls (solid or open doorway depending on room position), and a genre sign above the entrance.
- **Painting construction** (`buildPainting`): fits each painting's texture into a bounding box preserving aspect ratio, adds a frame, a placard (rendered to a canvas texture), and two spotlights.
- **Collision**: simple AABB colliders (`colliders` array) checked against a circular player radius in `resolveCollision`.
- **Movement/look**: mouse movement always rotates the camera (pointer stays unlocked, no Pointer Lock API); holding the left mouse button and dragging translates the camera based on cursor offset from screen center. WASD/arrow keys also translate.
- **Focus mode**: double-clicking a painting raycasts against `paintingHotspots` and animates the camera to a frontal close-up (`enterFocus`/`exitFocus`), with easing.
- **UI**: a start overlay with a loading bar (driven by `THREE.LoadingManager`), a room-name label that fades in/out on room transitions, and an HUD hint.

## Conventions

- Keep everything in `index.html` unless the file becomes unwieldy — this project is intentionally a zero-build single-file app.
- UI copy and code comments are in German, matching the existing content; keep new user-facing text consistent with that unless asked otherwise.
- Painting data uses Wikimedia Commons URLs — when adding artwork, prefer high-resolution Commons URLs and set `ratio` to the image's height/width.
- No shadows on painting images/frames beyond what's already there — don't add extra shadow effects to images (per user's global design preference).
