# Sketch-Clean-AI
AI-powered application that cleans up rough sketches for webtoon artists

### Assumptions
- background is always the lightest
- structural lines are always darker than the background but lighter than outlines
- outline is always the darkest
- no shading
- there is only 3 colors: background, structural lines, and outlines
### Preprocess
- convert to greyscale
- bilateral filtering
### Run Edge Detectors
- Adaptive Canary
- HED/DexiNed
### Postprocess
- Connect broken lines (morphological closing)


