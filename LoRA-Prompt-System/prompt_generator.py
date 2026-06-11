#!/usr/bin/env python3
"""RealisticSnapshot-Zimage-Turbov5 prompt generator.

Usage:
    python prompt_generator.py "She is taking selfie with BMW M4 in parking garage"
    python prompt_generator.py "She is taking mirror selfie in bedroom" --scene mirror
"""

from __future__ import annotations

import argparse
import re
import textwrap
from dataclasses import dataclass


NEGATIVE_LINE = (
    "Avoid cinematic lighting, DSLR look, studio photoshoot, airbrushed skin, plastic skin, "
    "perfect symmetry, glossy AI beauty, fake bokeh, over-clean background, warped anatomy, "
    "melted hands, distorted vehicle parts, unreadable logos, unnatural reflections, "
    "oversharpened render, and low-quality artifacts."
)


@dataclass(frozen=True)
class SceneRule:
    name: str
    keywords: tuple[str, ...]
    composition: str
    environment: str
    lighting: str
    camera: str


SCENES = [
    SceneRule(
        "parking_garage",
        ("parking garage", "garage", "basement parking", "car park"),
        "vertical 3:4 smartphone selfie or friend-shot framing with a slightly high or chest-height angle, imperfect crop, realistic phone perspective",
        "dim industrial concrete parking structure with overhead fluorescent tubes, exposed pipes, ductwork, painted stall lines, oil stains, tire marks, concrete pillars, traffic signs, and cold reflections",
        "harsh cold fluorescent overhead light creating specular highlights and deep shadow falloff",
        "mild wide-angle distortion, high-ISO texture in darker concrete, subtle compression, phone HDR behavior",
    ),
    SceneRule(
        "mirror",
        ("mirror", "mirror selfie", "bathroom selfie", "bedroom mirror"),
        "vertical mirror-reflection composition, phone partly covering the face or torso, chest-height framing, slight tilt, believable crop",
        "lived-in interior with shelves, curtains, door hinges, desk objects, chair, bottles, clothing pile, wall art, mirror dust, and small everyday clutter",
        "soft window daylight or warm indoor practical light with shallow shadows and realistic highlight rolloff",
        "mirror optics, slight smudges, reversed text or logos when relevant, mild digital sharpening and phone compression",
    ),
    SceneRule(
        "vehicle",
        ("bmw", "m4", "car", "vehicle", "bike", "motorcycle", "gt-r", "gtr", "nissan", "toyota"),
        "vertical phone lifestyle frame, subject foreground with vehicle clearly visible and physically accurate in the middle ground",
        "real parking lot or street setting with asphalt, parking lines, reflections on paint, headlights, grille, wheels, windshield, mirrors, dust, and surrounding street details",
        "practical daylight, sunset, garage light, or street light depending on topic, with believable reflections on glass and paint",
        "smartphone HDR, slight perspective stretch near frame edges, crisp vehicle surfaces without warped parts",
    ),
    SceneRule(
        "restaurant",
        ("restaurant", "cafe", "café", "dinner", "table", "terrace"),
        "vertical 4:5 table-level phone photo from across the table, close social-media framing, foreground objects visible",
        "busy terrace or cafe with plates, napkins, cutlery, glasses, phone on table, woven chairs, nearby diners, awnings, lamps, textured walls, and receding background depth",
        "warm tungsten practical lighting, amber white balance drift, occasional cool accent light, soft shadows, visible high-ISO grain",
        "handheld night phone texture, mild noise, slight motion softness, relaxed candid snapshot quality",
    ),
    SceneRule(
        "train",
        ("subway", "train", "metro", "public transit"),
        "vertical seated candid with phone-wide perspective, subject centered or slightly off-center on patterned transit seat",
        "utilitarian train interior with patterned seats, large windows, station blur, fluorescent ceiling strips, handrails, reflections, and dark exterior movement",
        "flat cool fluorescent interior light with realistic under-eye shadows and small specular highlights",
        "raw snapshot aesthetic, high-ISO noise, slight compression, deep phone depth of field",
    ),
    SceneRule(
        "night_flash",
        ("night flash", "flash", "night street", "dark street", "night parking"),
        "vertical flash portrait, subject centered and sharply lit, background falling quickly into darkness",
        "dark street or parking area with asphalt, parked cars, distant windows, utility poles, streetlights, and small bloomed light points",
        "hard direct on-camera flash with crushed blacks, immediate shadow falloff, glossy highlights on hair, lips, skin, and fabric",
        "smartphone flash photography, mild luminance noise in black areas, flat frontal contrast, candid night snapshot",
    ),
    SceneRule(
        "beach",
        ("beach", "sand", "sea", "ocean", "shore"),
        "vertical outdoor phone portrait, medium distance, horizon placed naturally, wind-touched hair and relaxed stance",
        "pale sand with footprints, calm sea, cloud layers, distant rocks, sailboat masts or shoreline objects, natural coastal depth",
        "soft diffused coastal daylight or warm sunset glow with natural skin highlights and gentle shadows",
        "clean phone capture with slight background softness, natural HDR sky handling, mild compression",
    ),
    SceneRule(
        "sports",
        ("stadium", "football", "soccer", "field", "goal", "jersey", "sports"),
        "vertical sports portrait, eye-level or slight low angle, subject sharp against turf or stadium geometry",
        "readable field structure, goal net, turf blades, seating rows, railings, pitch lines, and background architecture",
        "bright daylight with saturated sports colors, crisp shadows or soft overcast depending on topic",
        "social-media smartphone clarity, crisp fabric texture, slight computational sharpening, clean subject focus",
    ),
    SceneRule(
        "indoor",
        ("bedroom", "office", "hotel", "room", "indoor", "window"),
        "vertical indoor phone portrait or mirror selfie, casual crop from mid-thigh or torso up",
        "personal room details such as shelves, curtains, desk, chair, wall art, ceiling lights, windows, clothing, bottles, and small clutter",
        "mixed window daylight and warm ceiling practicals with natural shadows and realistic white balance",
        "phone snapshot rendering, slight wide-angle distortion, mild compression, readable background details",
    ),
    SceneRule(
        "outdoor",
        ("garden", "lawn", "park", "outdoor", "sunlight", "daylight"),
        "vertical friend-shot or phone portrait in natural daylight, relaxed pose, subject integrated with environment",
        "grass, foliage, hedges, trees, patios, houses, shadows, and natural surface texture with real depth",
        "direct sun or open shade with clipped highlights where natural, saturated greens, and realistic shadow direction",
        "deep phone depth of field, punchy consumer color, mild edge sharpening, casual snapshot look",
    ),
    SceneRule(
        "no_human",
        ("no human", "no person", "environment only", "object detail", "detail shot"),
        "vertical phone detail shot with no people, no face, no body, no reflection, no shadow silhouette",
        "specific real-world objects, surfaces, props, vehicle details, table details, room details, or street texture arranged naturally",
        "practical scene light with real reflections and shadows",
        "phone-camera close focus, mild compression, real surface imperfections, grounded snapshot realism",
    ),
]


def detect_scene(topic: str, override: str = "auto") -> SceneRule:
    if override != "auto":
        for scene in SCENES:
            if scene.name == override:
                return scene
    t = topic.lower()
    # priority order for compound topics
    for scene in SCENES:
        if any(k in t for k in scene.keywords):
            return scene
    return SceneRule(
        "generic",
        (),
        "vertical 4:5 realistic smartphone photo with casual social-media framing and imperfect crop",
        "specific lived-in environment inferred from the topic, with real objects, surfaces, background depth, and everyday imperfections",
        "practical real-world lighting appropriate to the scene, with believable highlights and shadows",
        "phone-camera realism with mild distortion, digital sharpening, subtle compression, and candid snapshot texture",
    )


def adult_subject_line(topic: str) -> str:
    lower = topic.lower()
    if any(word in lower for word in ["no human", "no person", "environment only", "object detail", "detail shot"]):
        return "A realistic phone snapshot based on the topic: " + topic.strip()
    return "A young adult woman in a tasteful realistic lifestyle scene based on the topic: " + topic.strip()


def generate_prompt(topic: str, scene_override: str = "auto") -> str:
    topic = topic.strip()
    scene = detect_scene(topic, scene_override)
    no_human = scene.name == "no_human"

    if no_human:
        subject = (
            f"A realistic vertical smartphone detail photograph based on the topic: {topic}. "
            "The frame contains no person, no face, no body, no human reflection, and no shadow silhouette."
        )
        human_detail = "Focus on physical surfaces, real textures, object edges, dust, fingerprints, reflections, wear marks, and believable spatial depth."
        outfit = "Describe only objects, props, materials, and environmental surfaces relevant to the topic."
    else:
        subject = (
            f"A young adult woman appears in a raw realistic smartphone-photo scene based on the topic: {topic}. "
            f"Use {scene.composition}."
        )
        human_detail = (
            "Her face, skin, and hair should look naturally human: visible pores, faint sebaceous filaments, subtle vellus hair, "
            "small flyaways or individual strands, realistic catchlights, natural skin tonal variation, and a slight oil or sweat sheen only where the scene lighting would create it."
        )
        outfit = (
            "Her outfit and accessories should be scene-appropriate and described with material realism: fabric weave, ribbing, stretch, seams, wrinkles, stitching, "
            "jewelry reflections, phone case texture, nails, and small personal details without making the image look staged."
        )

    env = f"Environment: {scene.environment}. Make the background specific and lived-in rather than generic."
    lighting = f"Lighting: {scene.lighting}."
    camera = f"Rendering: {scene.camera}; raw candid phone-gallery realism, mild imperfections, believable exposure, and no polished studio finish."

    prompt = " ".join([subject, human_detail, outfit, env, lighting, camera, NEGATIVE_LINE])
    return textwrap.fill(prompt, width=120)


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate RealisticSnapshot-Zimage-Turbov5 style prompts from simple topics.")
    parser.add_argument("topic", help="Simple image topic")
    parser.add_argument("--scene", default="auto", choices=["auto"] + [s.name for s in SCENES], help="Optional scene override")
    args = parser.parse_args()
    print(generate_prompt(args.topic, args.scene))


if __name__ == "__main__":
    main()
