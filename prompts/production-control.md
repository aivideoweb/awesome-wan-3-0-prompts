# Production Control, Editing, and Reference Workflows for Wan 3.0

<!-- core-template-context -->

These core briefs come from the [Flaq AI source collection](../UPSTREAM.md) and have not each been generated and verified on VideoWeb. Durations, aspect ratios and modes are creative targets, not a list of available controls. Before copying, read the [VideoWeb settings guide](../guides/videoweb-workflow.md#adapt-settings); save your settings and results with the [generation record](../templates/generation-record.md).

These prompts are designed for reusable production assets: clean plates, previs, geometry tests, multi-reference role assignment, local edits, aspect-ratio planning, and seamless loops.

<a id="prompt-01"></a>

## 01｜Green-screen cape performance plate

**Mode**: R2V / Green-screen generation　**Suggested**: 10 seconds, 16:9

[Before copying: adapt these target settings](../guides/videoweb-workflow.md#adapt-settings)

```text
10 seconds, 16:9, full-body performance plate on an evenly lit chroma-green cyclorama. Original adult performer wears a charcoal fitted motion costume and a long matte ivory cape with no reflective trim. Preserve face, body proportions, costume, cape length, and screen color.

00:00–00:03: Performer stands centered in neutral pose with arms slightly away from torso. Camera locked at waist height, 50mm-equivalent lens, full body and cape fully inside frame.
00:03–00:07: Performer takes two measured steps forward, turns left 90 degrees, and raises right arm. A controlled fan from frame right moves the cape left with visible inertia; feet remain grounded.
00:07–00:10: Performer returns to front, lowers arm, and holds still for one second. Cape settles naturally and never touches frame edges.

Production constraints: uniform green without gradients, tracking markers only if explicitly added later, no cast shadow beyond a soft contact shadow, no camera movement, no motion blur hiding edges, no green spill on cape, no props, text, logo, or watermark.
```

<a id="prompt-02"></a>

## 02｜White-model warehouse camera rehearsal

**Mode**: Previs / T2V　**Suggested**: 15 seconds, 2.39:1

[Before copying: adapt these target settings](../guides/videoweb-workflow.md#adapt-settings)

```text
15 seconds, 2.39:1, untextured white-model previsualization for an original warehouse conversation scene. Set lock: six columns, loading door, staircase, two crates, overhead walkway. Characters are neutral gray mannequins A and B with clear chest letters represented only as simple colored shapes, not generated text.

00:00–00:05: Camera begins behind the left crate at shoulder height, dollies forward 2 meters as mannequin A enters through the loading door.
00:05–00:10: Camera arcs right 45 degrees around A while mannequin B descends exactly four visible stair steps and stops on the landing. Preserve screen direction and never cross the A–B axis.
00:10–00:15: Camera settles into a balanced two-shot with A frame left and B frame right; both hold neutral poses for two seconds to evaluate composition.

Use uniform diffuse lighting, no textures, no facial animation, no final-film atmosphere. Keep set dimensions, mannequin colors, path, and camera height consistent. No cinematic fog, explosions, extra props, impossible wall passage, text, logo, or watermark.
```

<a id="prompt-03"></a>

## 03｜Stable 360-degree sneaker geometry test

**Mode**: I2V / Product test　**Suggested**: 12 seconds, 1:1

[Before copying: adapt these target settings](../guides/videoweb-workflow.md#adapt-settings)

```text
12 seconds, 1:1, neutral ecommerce geometry test. Product lock: original low-top sneaker with off-white canvas upper, dark teal heel panel, gum sole, seven eyelets per side, flat cream laces, no logo. Preserve silhouette, eyelet count, stitching, colors, and sole thickness.

The sneaker rests on a matte light-gray turntable and completes exactly one clockwise rotation over 12 seconds. Camera is fixed at midsole height with an 85mm-equivalent product lens. Lighting is a large softbox above-left plus low fill; reflections and shadows rotate only as expected from the object's changing surface orientation. Hold the first and final front-left three-quarter view for 0.5 seconds so they match.

Audio: quiet turntable motor only. No camera orbit, no foot inside, no lace movement, no material morph, no changing eyelet count, no duplicate shoe, no text, logo, or watermark.
```

<a id="prompt-04"></a>

## 04｜Start-to-end frame clay portrait transition

**Mode**: Start/end frames　**Suggested**: 14 seconds, 16:9

[Before copying: adapt these target settings](../guides/videoweb-workflow.md#adapt-settings)

```text
14 seconds, 16:9, controlled stop-motion transition from the provided first frame of a rough clay block to the provided final frame of an original simplified portrait bust. Preserve table, rotating base, sculptor hands, tool set, background, and lighting from both anchors.

00:00–00:05: Hands press the clay block into a head-and-shoulder volume through visible incremental stop-motion changes. Material volume is conserved; trimmed clay accumulates in one tray.
00:05–00:10: A wooden tool defines eye sockets, nose plane, and mouth line in a believable order. The base turns no more than 45 degrees to access the side; features do not appear all at once.
00:10–00:14: Fingers smooth only the cheek and brow, then rotate the bust to the exact final-frame orientation. Hands leave frame and the final pose holds for one second.

Audio: tactile clay and tool sounds, no music. No human skin transformation, no perfect photoreal face, no extra tools, no clay appearing from nowhere, no mismatch with end-frame silhouette, text, or watermark.
```

<a id="prompt-05"></a>

## 05｜Local edit: change only the window weather

**Mode**: Video edit　**Suggested**: preserve source duration and ratio

[Before copying: adapt these target settings](../guides/videoweb-workflow.md#adapt-settings)

```text
Edit only the weather visible through the office windows, changing a clear afternoon into gentle early winter snow. Preserve every interior pixel relationship: the two employees, faces, clothing, hand actions, computer screens, desk objects, reflections, camera path, focus changes, timing, and room lighting.

Outside only: replace blue sky with pale overcast, add sparse snow moving downward-right according to the existing wind, soften distant building contrast, and allow a very thin snow layer to accumulate only on exterior horizontal ledges. Window reflections must continue to show the same interior and camera movement. Do not put snow, fog, or breath inside the climate-controlled office.

Keep the original audio exactly unchanged. No identity edits, wardrobe edits, new people, interior color grade shift, moving buildings, frozen windows, readable text change, logo, or watermark.
```

<a id="prompt-06"></a>

## 06｜One scene planned for three aspect ratios

**Mode**: T2V / Previs　**Suggested**: 10 seconds, master 16:9

[Before copying: adapt these target settings](../guides/videoweb-workflow.md#adapt-settings)

```text
10 seconds, master 16:9 composition designed to crop safely to 1:1 and 9:16. Original scene: a bicycle mechanic in a cobalt apron pumps a repaired tire at the center of a compact workshop. Keep face, apron, bicycle, pump, and background tools consistent.

00:00–00:04: Medium full-body shot with subject and bicycle inside the central 40% safe zone. Mechanic connects the pump hose and presses down once; hands and valve remain visible in all crops.
00:04–00:07: Camera makes a subtle 8% push-in only. Pressure gauge sits just below center, while decorative shelves remain expendable at left and right edges.
00:07–00:10: Mechanic spins the wheel by hand, watches one full rotation, then gives a small satisfied nod. Hold a centered final frame with clean space above, never placing essential information near horizontal edges.

Audio: pump, freewheel, workshop ambience. No lateral camera move, off-center subject, tool teleportation, changing crop during generation, brand, text, or watermark.
```

<a id="prompt-07"></a>

## 07｜Three references with one role each

**Mode**: R2V　**Suggested**: 15 seconds, 16:9

[Before copying: adapt these target settings](../guides/videoweb-workflow.md#adapt-settings)

```text
Reference roles are strict and separate:
Image 1 supplies only the original dancer's identity, short curly hair, silver jumpsuit, and white boots.
Video 1 supplies only the five-beat footwork rhythm and weight shifts; do not copy its person, clothing, room, camera, or background.
Image 2 supplies only the amber theater stage, three vertical light panels, and polished black floor.

Generate a new 15-second performance. 00:00–00:05: locked medium-wide front view establishes the dancer and stage; she performs the five-beat footwork once at natural speed. 00:05–00:10: camera tracks left two meters as she repeats the rhythm with an added arm sweep, feet maintaining the same timing. 00:10–00:15: camera stops; she turns front, lands both feet, and holds the final pose while the three light panels dim from left to right.

Audio: original percussion matched to five beats, no copied music. Preserve identity, outfit, stage, floor reflections, and foot contact. No reference blending, costume from Video 1, extra dancers, body distortion, text, logo, or watermark.
```

<a id="prompt-08"></a>

## 08｜Phone UI action matched to real-world result

**Mode**: I2V / T2V　**Suggested**: 12 seconds, 9:16

[Before copying: adapt these target settings](../guides/videoweb-workflow.md#adapt-settings)

```text
12 seconds, 9:16, clean fictional smart-home interaction demo. Phone lock: black device, blank status bar, three large abstract room cards; room lock: one warm table lamp, closed blinds, ceiling light off. Do not require small readable text.

00:00–00:04: Over-shoulder close-up. Thumb taps the lamp card once; the card changes from gray to amber and the real table lamp in background turns on after a natural 0.2-second response. Show clear contact and no other UI changes.
00:04–00:08: Thumb drags the same card slider halfway; lamp brightness reduces smoothly while room exposure stays fixed so the change remains honest.
00:08–00:12: Focus shifts from phone to lamp. The hand lowers but keeps the phone in frame; lamp remains at half brightness and the other room devices remain unchanged. Finish with negative space for real interface labels in post.

Audio: two subtle interface tones and room tone. No floating holograms, unreadable fake text, duplicate phone, delayed random lights, exposure pumping, brand, or watermark.
```

<a id="prompt-09"></a>

## 09｜Seamless loop with matched first and last frame

**Mode**: T2V / Start-end frames　**Suggested**: 8 seconds, 1:1 loop

[Before copying: adapt these target settings](../guides/videoweb-workflow.md#adapt-settings)

```text
8 seconds, 1:1, seamless photoreal tabletop loop. A clear glass marble travels through an original small brass kinetic sculpture: left ramp, central circular track, right lever, and return channel. Lock camera, sculpture geometry, marble size, lighting, and background.

00:00–00:02: Marble begins at the exact top-left start mark and rolls down under gravity, contacting the brass ramp with realistic acceleration.
00:02–00:05: It enters the circular track, completes one full clockwise loop, and exits toward the right lever; reflections rotate across the glass without changing marble shape.
00:05–00:07: Marble depresses the lever, which tips the return channel upward. The marble rolls behind the central disk and reappears near the top-left.
00:07–00:08: Lever resets and marble settles on the exact start mark with the same reflection and zero velocity as frame one. Hold for two frames before looping.

Audio forms an eight-beat mechanical loop with brass clicks aligned to contacts. No hidden hand, perpetual acceleration, extra marble, geometry shift, camera movement, text, logo, or watermark.
```

<a id="prompt-10"></a>

## 10｜Continuity slate for wardrobe and hand props

**Mode**: R2V / Production reference　**Suggested**: 12 seconds, 16:9

[Before copying: adapt these target settings](../guides/videoweb-workflow.md#adapt-settings)

```text
12 seconds, 16:9, neutral continuity-reference plate for an original café character. Identity lock: adult actor with short dark curls, mustard cardigan, white collar, black watch on left wrist. Prop lock: blue ceramic cup with chipped handle, folded newspaper, silver pen. Preserve every side and placement.

00:00–00:04: Static front medium shot. Actor stands in neutral pose, turns both empty hands toward camera, then lowers them. Even soft lighting and color chart remain at frame edge.
00:04–00:08: Cut to seated left-side profile at the café table. Actor holds the blue cup in the right hand, watch visible on left wrist, newspaper below the cup, pen parallel to table edge. Hold for two seconds.
00:08–00:12: Overhead insert records exact prop positions; actor places the cup back on its marked ring and removes both hands. End on a clean still frame suitable for comparison.

Audio: slate clap once, room tone, cup contact. No performance emotion, costume redesign, watch switching wrists, cup-chip repair, prop movement between angles, text, brand, or watermark.
```

<a id="prompt-11"></a>

## 11｜Clean background plate and controlled object removal

**Mode**: Video edit / Clean plate　**Suggested**: preserve source duration and ratio

[Before copying: adapt these target settings](../guides/videoweb-workflow.md#adapt-settings)

```text
Create two matched deliverables from the original locked-off 8-second street-corner shot.

Version A, clean plate: remove only the parked red bicycle and its contact shadow from the wall. Reconstruct the occluded pale brick, curb, and two paving joints using surrounding texture and perspective. Preserve pedestrians, tree movement, passing bus, reflections, camera, exposure, timing, and original audio exactly.

Version B, object-isolation check: keep the original bicycle but replace the surrounding scene with flat middle gray, preserving every bicycle edge, wheel spoke, handlebar, basket opening, and contact shadow as a separate visible element. Do not change bicycle geometry.

No new pedestrian, brick repetition artifact, flicker, moving repair patch, missing reflection, bicycle redesign, camera stabilization, color-grade change, text, logo, or watermark.
```
