# LoRA Technical Analysis

## File analyzed

RealisticSnapshot-Zimage-Turbov5 style adapter.

## Safe technical findings

- Base model metadata reports: zimage.
- Training software metadata reports: ai-toolkit.
- Training info metadata reports approximately: step 28600, epoch 11.
- File size observed: about 163 MB.
- Tensor entries observed: 480 LoRA tensors.
- Layer coverage observed: diffusion model layers 0 through 29, for a total of 30 layers.
- Repeated module coverage observed across layers:
  - adaLN_modulation.0
  - attention.to_q
  - attention.to_k
  - attention.to_v
  - attention.to_out.0
  - feed_forward.w1
  - feed_forward.w2
  - feed_forward.w3
- Tensor shape pattern indicates an effective LoRA rank around 32.
- Most tensors were FP16.

## Interpretation

This appears to be a broad visual-style LoRA rather than a narrow identity-only LoRA. It affects attention, feed-forward, and adaptive layer-normalization pathways across many transformer layers, so it likely influences overall rendering behavior: texture, lighting response, surface detail, realism density, and final image feel.

The strongest practical conclusion should come from reference images and prompts, not weights alone. We should not claim that the weights directly encode exact objects, brands, locations, or poses. Those concepts come from the reference examples. The file structure only supports the conclusion that this is a model-wide realism and style adapter.

## Prompting implications

Use prompts that describe:

- real smartphone capture behavior
- practical lighting sources
- environmental specificity
- skin and material texture
- optics and sensor imperfections
- grounded candid composition

Do not rely on one short trigger phrase. This style is best activated by dense, physical, scene-specific prompts.