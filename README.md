# Transparent Video Maker

A desktop GUI tool for converting videos with solid-color backgrounds into
true transparent videos with an alpha channel (`.webm` or `.mov`).

Built around **ffmpeg** (chroma key removal) and **rembg** (AI background removal),
with a simple point-and-click interface — no command line required.

---

## Features

- **Chroma Key removal** — precise color-based removal for solid-color backgrounds
  (green screen, blue screen, black, white, or any custom color)
- **AI removal** — rembg-powered background removal for more complex backgrounds,
  with multiple model options including a character/figure-optimized model
- **Frames → Video** tab — encode a folder of manually-edited transparent PNG frames
  into a transparent video (useful if you edit frames yourself in Photoshop, etc.)
- Output to **WebM/VP9** (best for web, OBS, most editors) or **MOV/ProRes 4444**
  (high-quality editing master)
- Live log output and step-by-step progress indicators
- Auto-detects frame filename patterns

---

## Requirements

### 1. Python 3.10 or 3.11

Download from [python.org](https://www.python.org/downloads/).
During installation, check **"Add Python to PATH"**.

### 2. ffmpeg

Download the latest **ffmpeg-release-essentials.zip** (or full build) from:
> https://www.gyan.dev/ffmpeg/builds/

Extract the zip, then add the `bin` folder to your system PATH.

*ffmpeg is a separate program licensed under GPL v3. It is not included in this
repository. See [ffmpeg.org](https://ffmpeg.org) for more information.*

### 3. rembg (Python package)

Open Command Prompt and run:

```
pip install rembg[cli]
```

*rembg is licensed under the MIT License.*

---

## Installation

1. Install Python, ffmpeg, and rembg as described above.
2. Download or clone this repository.
3. Run the app:

```
python TransparentVideoMaker.py
```

Or double-click `TransparentVideoMaker.py` if Python is associated with `.py` files.

---

## Quick Start

### Full Pipeline (video in → transparent video out)

1. Open the **Full Pipeline** tab.
2. Click **Browse** and select your video file.
3. Choose a removal method:
   - **Chroma Key** — recommended if your background is a solid color.
     Pick the background color (use the presets or color picker),
     then adjust **Similarity** and **Edge Blend** as needed.
   - **AI Model** — use if the background is complex or unknown.
4. Choose your output format (WebM recommended for most uses).
5. Click **▶ RUN FULL PIPELINE**.

### Frames → Video (manually edited frames → transparent video)

1. Open the **Frames → Video** tab.
2. Click **Browse** and select the folder containing your transparent PNG frames.
3. Click **Auto-detect** to detect the filename pattern automatically.
4. Set your framerate and output format.
5. Click **▶ ENCODE VIDEO FROM FRAMES**.

### Tips for best chroma key results

- Keep **Similarity** low (0.05–0.15) to avoid eating into the character's edges.
- Raise **Edge Blend** slightly (0.03–0.08) if the outline looks jagged or harsh.
- A clean, evenly-lit solid background will give the sharpest result.

---

## License

This project (the Python GUI script) is released under the **MIT License**.
See [LICENSE](LICENSE) for details.

**Third-party tools** (not included — must be installed separately):
- **ffmpeg** — GPL v3 — https://ffmpeg.org
- **rembg** — MIT — https://github.com/danielgatis/rembg
