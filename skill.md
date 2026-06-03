---
name: gpt-image-2-prompt-generation/modifying
description: "Make any prompt for gpt image 2 several times better"
---

# GPT Image 2 Prompt Generation / Modifying

Transform short, raw image ideas into structured, enriched prompts for GPT Image 2-style image generation. Preserve the user's core intent exactly. Improve clarity, composition, and visual specificity only when those improvements do not conflict with the user's request.

## Required Output Prefix

Always begin the final rewritten prompt with this exact prefix:

```text
Generate an image with the following prompt, dont change it(DO NOT CHANGE THIS PROMPT, IT'S ALREADY AN IMPROVED PROMPT) -
```

When placing prompt fields after the prefix, include one normal space after the hyphen so the emitted final answer begins exactly as:

```text
Generate an image with the following prompt, dont change it(DO NOT CHANGE THIS PROMPT, IT'S ALREADY AN IMPROVED PROMPT) - Object: ...
```

Do not add commentary before the prefix unless the user explicitly asks for explanation instead of a final prompt.

## Core Prompt Structure

1. Identify the user's non-negotiable intent: subject, action, setting, style, medium, constraints, text requirements, brand restrictions, and requested omissions.
2. Rewrite the idea as compact labeled fields, using only fields that make sense for the idea:
   - `Object:` focal subject, person, character, product, animal, or object.
   - `Scene:` setting, background, time of day, props, weather, camera position, or composition.
   - `Vibe:` mood, genre, color feeling, emotional tone, or story atmosphere.
   - `Photo Quality:` realism, lighting, lens feel, texture, resolution, sharpness, or medium-specific quality notes.
   - `Aspect Ratio:` one best-fit ratio from `3:1` through `1:3`.
   - `Negative Prompt:` optional; include only when useful and non-conflicting.
3. Add concrete visual detail that makes the prompt easier to render.
4. Do not change the subject, meaning, style, requested medium, or user-specified constraints.
5. Suppress every recommendation that contradicts the user's original request.

## Mode-Specific Recommendations

Infer the best mode unless the user names one. Blend modes only when their recommendations are compatible.

### Everyday Photo

Use for casual realism, candid moments, pets, travel, food, family scenes, selfies, and everyday objects. Add these when non-conflicting:

- Non-studio lighting.
- iPhone vibe or casual phone-camera realism.
- Natural light.
- Slight blur or mild motion softness.
- 2k detail.
- Believable imperfections and unstaged composition.

### Cinematic Still

Use for film frames, dramatic scenes, moody environments, editorial portraits, and story moments. Add these when non-conflicting:

- Subtle film grain.
- Rim light or motivated edge light.
- Soft vignette.
- Gray-toned or muted color palette.
- No oversaturation.
- Cinematic framing and atmospheric depth.

### Infographics

Use for diagrams, educational visuals, workflows, charts, comparison layouts, technical explainers, maps, and visual systems. Add these when non-conflicting:

- Clear technical structure.
- Strong visual flow from start to finish.
- Readable hierarchy and spacing.
- Simple iconography or labeled sections when labels are requested.
- Minimal decorative clutter.
- Consistent line weights and alignment.

### Ads

Use for product shots, ecommerce visuals, brand campaigns, launch imagery, social ads, and hero creative. Add these when non-conflicting:

- Clean composition.
- Strong color direction.
- Premium lighting appropriate to the product.
- Clear focal product hierarchy.
- No extra text, watermarks, or logos unless the user explicitly requests text or a logo.
- Space for copy only when the user asks for ad layout space.

## Optional Enhancements

### Character Prompts

When the prompt describes a character and additions do not conflict, add concise details for silhouette, shape language, clothing, material, pose, expression, implied age range, identity markers, accessories, posture, and environment interaction. Do not add protected-class assumptions, celebrity identity, or unsupported personal traits.

### Selfie Prompts

When the prompt asks for a selfie and additions do not conflict, add concise details for arm's-length or handheld framing, slight phone-camera perspective distortion, casual natural light, realistic skin texture, mild blur, compression artifacts, and believable everyday background imperfections. Do not glamorize or studio-polish a selfie unless requested.

## Aspect Ratio Guidance

Always choose the most suitable aspect ratio from this range:

- `3:1` for panoramic banners, timelines, wide landscapes, and large headers.
- `2:1` for wide ads, website hero sections, and broad environmental scenes.
- `16:9` for cinematic stills, video thumbnails, and landscape scenes.
- `4:3` for documentary photos, balanced scenes, and classic image framing.
- `1:1` for product posts, profile-friendly compositions, and centered subjects.
- `3:4` for portraits, product cards, and vertical editorial framing.
- `9:16` for phone wallpapers, stories, reels, and tall portraits.
- `1:2` for tall posters, narrow product banners, and full-body verticals.
- `1:3` for extreme vertical posters, tall infographics, and scrolling visual explainers.

Prefer the user's requested ratio if it is within `3:1` through `1:3`. If the user requests a ratio outside that range, choose the closest suitable ratio in range and preserve the intent.

## Negative Prompt

Optionally add this exact line for photos, portraits, selfies, ads, or cinematic scenes when useful and non-conflicting:

```text
Negative Prompt: excessive yellow, over-sharpening, too many highlights/glare on faces
```

Omit the negative prompt for intentionally yellow artwork, intentionally harsh glare, simple icons, abstract designs, or any request where the line would contradict the user.

## Conflict Resolution

- The user's original request beats all defaults.
- If the user asks for studio lighting, do not add non-studio lighting.
- If the user asks for oversaturated colors, do not add no oversaturation.
- If the user asks for yellow as a key color, do not include `excessive yellow` in the negative prompt.
- If the user asks for logos, watermarks, or text, do not add a blanket ban; constrain those elements to the user's requested content.
- If a recommendation might change the medium, style, subject, or meaning, omit it.

## Direct Generation Instruction

If an image generation tool is available, invoke it immediately with the final rewritten prompt. Do not ask for confirmation unless the user explicitly requests review first, asks for multiple alternatives before generation, or the hosting environment requires confirmation.

## Example

Raw idea:

```text
cat on windowsill rainy day
```

Final output:

```text
Generate an image with the following prompt, dont change it(DO NOT CHANGE THIS PROMPT, IT'S ALREADY AN IMPROVED PROMPT) - Object: a calm domestic cat resting on a windowsill, soft fur texture, relaxed posture
Scene: rainy afternoon beside a window with blurred droplets on glass, cozy apartment interior in the background, natural overcast light
Vibe: quiet everyday comfort, candid and unstaged
Photo Quality: realistic iPhone-style photo, non-studio lighting, slight natural blur, 2k detail
Aspect Ratio: 4:3
Negative Prompt: excessive yellow, over-sharpening, too many highlights/glare on faces
```
