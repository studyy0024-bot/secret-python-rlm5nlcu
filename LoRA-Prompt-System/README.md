# RealisticSnapshot-Zimage-Turbov5 Prompt System

This project turns a simple image topic into a detailed final prompt matching the RealisticSnapshot-Zimage-Turbov5 reference style family.

## What this system does

You provide a simple topic, for example:

```bash
python prompt_generator.py "She is taking selfie with BMW M4 in parking garage"
```

It outputs a complete image prompt using:

- raw smartphone snapshot realism
- practical lighting
- visible skin and material texture
- specific lived-in environments
- phone-camera imperfections
- scene-aware routing for selfies, mirror selfies, vehicles, restaurants, streets, beaches, stadiums, interiors, and no-human detail shots

## Main files

- `LORA_TECHNICAL_ANALYSIS.md` — safe technical notes from the LoRA file/header analysis.
- `LORA_STYLE_FINGERPRINT.md` — style DNA extracted from the reference prompts/images.
- `MASTER_TOPIC_TO_PROMPT_GENERATOR.md` — copy-paste master prompt for ChatGPT/Codex/Gemini/Claude.
- `prompt_generator.py` — local CLI prompt generator.
- `EXAMPLES.md` — example simple topics and final prompt outputs.
- `CODEX_TASK_PROMPT.md` — instruction prompt you can paste into Codex to improve/extend this project.

## Usage

```bash
cd LoRA-Prompt-System
python prompt_generator.py "She is sitting in a subway train at night"
```

Optional custom scene type:

```bash
python prompt_generator.py "She is taking mirror selfie in bedroom" --scene mirror
```

Available scene shortcuts:

- `auto`
- `selfie`
- `mirror`
- `vehicle`
- `garage`
- `restaurant`
- `train`
- `indoor`
- `night_flash`
- `outdoor`
- `beach`
- `sports`
- `friend_shot`
- `object_detail`
- `no_human`

## Style rules

Keep outputs tasteful, adult, realistic, and non-explicit. Avoid cinematic/DSLR/studio/8K language. Use real phone-camera behavior and practical environmental details.