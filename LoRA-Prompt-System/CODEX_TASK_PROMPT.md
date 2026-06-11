# Codex Task Prompt

Paste this into Codex when you want Codex to improve or extend the project.

```text
You are an expert image-prompt engineer and Python developer.

Analyze this project folder:

LoRA-Prompt-System/

Improve the RealisticSnapshot-Zimage-Turbov5 topic-to-prompt generator.

Tasks:

1. Read README.md, LORA_TECHNICAL_ANALYSIS.md, LORA_STYLE_FINGERPRINT.md, MASTER_TOPIC_TO_PROMPT_GENERATOR.md, EXAMPLES.md, and prompt_generator.py.
2. Improve prompt_generator.py so the generated prompts feel more specific, less generic, and closer to the reference style.
3. Add more scene routers if needed.
4. Add a references/ folder structure:
   - references/images/
   - references/prompts/
   - references/all_reference_prompts.md
5. Add tests or simple example runs if useful.
6. Keep the project simple and usable from terminal.

Style constraints:

- raw realistic smartphone photo
- practical lighting
- visible real skin texture when humans are present
- detailed fabric/materials
- lived-in environment details
- phone-camera imperfections
- tasteful adult social-media realism
- no cinematic/DSLR/studio/8K language
- no airbrushed plastic skin
- no explicit or pornographic framing

Final output should preserve the simple workflow:

python prompt_generator.py "simple topic here"

and return one complete final prompt.
```
