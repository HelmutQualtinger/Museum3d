# CLAUDE.md

Guidance for Claude Code when working in this repository.

## Project

A walkable 3D art museum rendered entirely client-side with Three.js. The whole app — markup, styles, and logic — lives in a single file: `index.html`. There is no build step, no package.json, and no bundler; Three.js is loaded from a CDN via an import map.

## Architecture (all in `index.html`)

- **Data**: `ROOMS` array defines three galleries (Portrait, Landscape, Modern), each with an accent color, floor color, and three paintings (title, artist, image URL, aspect ratio).
- **Scene setup**: standard Three.js scene/camera/renderer boilerplate, ACES tone mapping, fog for depth.
- **Floor**: `makeWoodFloorTexture` draws light oak planks onto a 1024² canvas once at startup (per-plank color variation, wavy grain, staggered butt joints, seams) and repeats the tile across every floor — one tile ≈ 3.5 m, so planks read about 35 cm wide. Grain strokes must return to their starting y at the tile's right edge or the repeat shows a seam. Each room's `floor` value is now a near-white *tint* multiplied over that texture, not a solid color — dark values there would cancel the planks out.
- **Room construction** (`buildRoom`): builds floor, ceiling with light panels, front/back walls (two-tone: accent lower band, light upper band), side walls (solid or open doorway depending on room position), and a genre sign above the entrance.
- **Painting construction** (`buildPainting`): fits each painting's texture into a bounding box preserving aspect ratio, adds a frame, a placard (rendered to a canvas texture), and two spotlights.
- **Painting lighting** — deliberately tuned, don't undo it casually: the canvas material is near-matte (`roughness: 0.98`) and carries the texture as an `emissiveMap` at `emissiveIntensity: 0.45`, so the artwork shows its true colors independent of the lights. Spots are narrow (30°) and dim (11) rather than floodlights. The earlier glossy material under a 42-intensity, 54° spot put a specular sheen over every painting and a white halo on the wall. Room brightness comes from the ceiling `PointLight`s, not the picture lights — raise those if a hall looks too dark, not the spots.
- **Collision**: simple AABB colliders (`colliders` array) checked against a circular player radius in `resolveCollision`.
- **Look**: dragging rotates the camera using the "grab" metaphor — the scene follows the pointer, as in Street View or OrbitControls (`applyLook` *adds* the delta to yaw/pitch; an FPS scheme would subtract it). No Pointer Lock API, so the cursor stays free to click things.
- **Movement**: WASD/arrows feed `velFwd`/`velStrafe`, which are lerped toward the input each frame for smooth start/stop; the scroll wheel adds to `wheelVel`, an impulse that decays exponentially. Both are applied along the camera yaw in the render loop.
- **Click handling**: one `click` listener calls `handleSelect`, which resolves intent by raycast — a painting enters focus, the floor triggers `travelTo`, and anything else exits focus. `dragMoved` (set past `DRAG_THRESHOLD`) suppresses the click that ends a drag. Touch maps onto the same `pointerDown`/`pointerMove`/`pointerUp` helpers, with a tap calling `handleSelect`.
- **Focus mode**: `enterFocus`/`exitFocus` animate the camera to a frontal close-up of a painting, easing over a distance-scaled duration. There is deliberately **no** distance limit on painting raycasts — clicking a painting several halls away walks you to it.
- **`travelTo`**: reuses the same `focusState` animation machinery for click-to-walk, but leaves `focusState.active` false so normal movement resumes when it lands.
- **UI**: a start overlay with a loading bar (driven by `THREE.LoadingManager`; the start button stays dimmed until `onLoad` fires, since clicking before the module initializes does nothing), a room-name label that fades in/out on room transitions, a hover tooltip with title/artist, a **← Zurück** button shown only in focus mode, and an HUD hint whose text swaps between `HUD_DEFAULT` and `HUD_FOCUS`.
- **Esc**: exits the close-up first and only opens the menu when not focused.

## Gotchas

- `requestAnimationFrame` is paused entirely while the tab is backgrounded, so camera animations do not advance and any in-page wait that polls for them will hang. When testing with browser automation, step the animation by taking screenshots rather than sleeping in the page.
- Placard textures are drawn to a fixed 1024px canvas; `makePlacardTexture` shrinks the font to fit, because long titles used to be clipped.

## Conventions

- Keep everything in `index.html` unless the file becomes unwieldy — this project is intentionally a zero-build single-file app.
- UI copy and code comments are in German, matching the existing content; keep new user-facing text consistent with that unless asked otherwise.
- Painting data uses Wikimedia Commons URLs — when adding artwork, prefer high-resolution Commons URLs and set `ratio` to the image's height/width.
- No shadows on painting images/frames beyond what's already there — don't add extra shadow effects to images (per user's global design preference).
