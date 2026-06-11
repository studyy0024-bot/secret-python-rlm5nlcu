# OPEN THIS FOR PROMPTS

Bhai agar Codex logs me output nahi mil raha, to ye file open karo. Yahan direct sample generated prompts aur use karne ka tareeka hai.

## Sabse easy method

Codex ke chat box me ye paste karo:

```text
Open LoRA-Prompt-System/OPEN_THIS_FOR_PROMPTS.md and show me the prompts inside.
```

Ya repo file tree me left side se open karo:

```text
LoRA-Prompt-System > OPEN_THIS_FOR_PROMPTS.md
```

## Command run karna ho to

```bash
cd LoRA-Prompt-System
python prompt_generator.py "She is taking selfie with BMW M4 in parking garage"
```

Agar Codex terminal me folder already `LoRA-Prompt-System` ke andar hai, to sirf ye run karo:

```bash
python prompt_generator.py "She is taking selfie with BMW M4 in parking garage"
```

---

# Sample Prompt 1: BMW M4 parking garage selfie

A young adult woman takes an arm-length smartphone selfie in a dim industrial parking garage, framed vertically in a 3:4 phone-photo crop from a slightly high angle, her face and upper body filling the immediate foreground while a silver BMW M4 coupe sits clearly behind her in the middle ground. Her face, skin, and hair should look naturally human: visible pores, faint sebaceous filaments, subtle vellus hair, small flyaways, realistic catchlights, and a slight oil sheen where the overhead fluorescent light hits her forehead, nose, cheekbones, and collarbones. She wears a scene-appropriate fitted casual black top with realistic fabric stretch, soft creases, and small jewelry highlights. The BMW is physically accurate and complete, with kidney grille, headlights, hood reflections, windshield, side mirror, wheel arch, and metallic paint clearly rendered. The garage background includes concrete pillars, white parking lines, tire marks, oil stains, exposed ducts, red fire pipes, fluorescent ceiling tubes, and a dark directional sign with reversed selfie-style lettering. Harsh cold overhead lighting creates strong highlights on the car paint and realistic shadows under the vehicle. Raw handheld smartphone selfie, slight wide-angle distortion, mild high-ISO grain in the darker areas, subtle compression, imperfect framing, natural HDR behavior, and unpolished urban realism. Avoid cinematic lighting, DSLR look, studio photoshoot, airbrushed skin, plastic skin, perfect symmetry, glossy AI beauty, fake bokeh, over-clean background, warped anatomy, melted hands, distorted vehicle parts, unreadable logos, unnatural reflections, oversharpened render, and low-quality artifacts.

---

# Sample Prompt 2: Bedroom mirror selfie

A young adult woman takes a vertical bedroom mirror selfie in a bright white room, phone held at chest height with the case clearly visible, framed from mid-thigh up with a clean but casual social-media crop. Her skin shows realistic pores, soft forehead and cheek highlights, faint natural texture, and believable catchlights. Her hair is styled casually with face-framing strands and small flyaways. She wears a comfortable matching set or simple indoor outfit with ribbed fabric, stretch, seams, waistband texture, necklace, rings, and manicured nails. The room includes white floating shelves, a wall vent, sheer curtains, gray wood-look floor, a chair, small bottles, a clothing pile, and a cardboard box corner for lived-in realism. Soft window daylight from one side produces gentle shadows and a slightly cool white balance, with mild digital sharpening and mirror-surface imperfections. Casual smartphone mirror selfie, everyday indoor daylight, slight optical distortion, natural phone compression, not a produced shoot. Avoid cinematic lighting, DSLR look, studio photoshoot, airbrushed skin, plastic skin, perfect symmetry, glossy AI beauty, fake bokeh, over-clean background, warped anatomy, melted hands, unreadable logos, unnatural reflections, oversharpened render, and low-quality artifacts.

---

# Sample Prompt 3: Subway train candid

A young adult woman sits alone on a patterned subway seat at night, photographed vertically in a candid phone frame from across the aisle at seated eye level. Her posture is relaxed and slightly tucked in, with one hand near her face and her gaze turned just away from the camera. Her face and hair show natural detail: visible pores, faint skin texture, small flyaways, realistic eyelashes, and soft highlights on lips and fingertips. She wears a casual layered outfit with ribbed cotton, nylon jacket texture, sock knit, sneaker scuffs, and small metal accessories catching the fluorescent light. The subway interior includes patterned navy seats, large windows with station-light reflections, fluorescent ceiling strips, dark window glass, handrails, worn floor panels, and a bag partly cropped at the side. Cool flat train lighting creates soft but utilitarian shadows, while the station outside blurs into small light streaks. Raw smartphone public-transit snapshot, mild high-ISO noise, slight compression, deep phone depth of field, and unpolished urban realism. Avoid cinematic lighting, DSLR look, studio photoshoot, airbrushed skin, plastic skin, perfect symmetry, glossy AI beauty, fake bokeh, over-clean background, warped anatomy, melted hands, unreadable logos, unnatural reflections, oversharpened render, and low-quality artifacts.

---

# Sample Prompt 4: Outdoor restaurant night candid

A young adult woman sits at an outdoor restaurant table at night, photographed vertically in a 4:5 handheld phone frame from across the table at seated eye level. She is centered in a woven cafe chair, relaxed and looking slightly away from the lens with a candid expression. Her skin has natural pores, subtle highlights on cheekbones and collarbones, and warm tonal variation from tungsten practical lights. Her hair catches amber edge highlights with loose strands near the face. Her outfit is described with realistic fabric texture, seams, trim, and small jewelry reflections. The foreground table includes a plate, folded napkin, fork, glass edge, and phone lying face-down; behind her are white-clothed tables, nearby diners, textured stucco wall, shutters, burgundy awnings, potted plants, and a row of woven pendant lamps receding into the background. Warm tungsten lamps create amber white-balance drift, soft shadows, and visible high-ISO grain in the darker terrace areas, with one cooler wall light as contrast. Handheld smartphone night photography, slight motion softness, mild compression, practical-light realism, and relaxed social-media snapshot mood. Avoid cinematic lighting, DSLR look, studio photoshoot, airbrushed skin, plastic skin, perfect symmetry, glossy AI beauty, fake bokeh, over-clean background, warped anatomy, melted hands, unreadable logos, unnatural reflections, oversharpened render, and low-quality artifacts.

---

# Sample Prompt 5: No-human object detail shot

A realistic vertical smartphone detail photograph with no person, no face, no body, no human reflection, and no shadow silhouette, showing a BMW key fob and a takeaway coffee cup resting on the glossy hood of a silver performance car inside a dim parking garage. The frame is close and slightly angled from above with phone-camera perspective. The car paint shows realistic fluorescent tube reflections, tiny dust specks, faint fingerprints near the key, and subtle curvature of the hood. The key fob has crisp buttons, worn plastic edges, a small metal ring, and realistic shadow contact; the coffee cup has a cardboard sleeve, lid seam, and a small drip mark. The background falls softly into concrete pillars, parking lines, oil stains, ductwork, and cold overhead lights. Harsh fluorescent light creates specular highlights and deep concrete shadows. Phone-camera close focus, mild digital sharpening, slight compression, high-ISO texture in the darker background, grounded object snapshot realism. Avoid cinematic lighting, DSLR look, studio photoshoot, glossy AI render, fake bokeh, over-clean background, warped object geometry, unreadable logos, unnatural reflections, oversharpened render, and low-quality artifacts.

---

# Apna simple topic ka prompt kaise nikaalna hai

Example:

```bash
python prompt_generator.py "She is taking mirror selfie in bedroom"
```

Scene force karna ho:

```bash
python prompt_generator.py "She is taking mirror selfie in bedroom" --scene mirror
python prompt_generator.py "She is taking selfie with BMW M4 in parking garage" --scene parking_garage
python prompt_generator.py "No human detail shot of BMW key and coffee on parking garage hood" --scene no_human
```
