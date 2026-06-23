---
title: QA Test-Case Generator
emoji: 🧪
colorFrom: indigo
colorTo: purple
sdk: gradio
sdk_version: 4.44.0
app_file: app.py
pinned: false
license: mit
---

# 🧪 QA Test-Case Generator (Hugging Face Space)

A free, shareable web app that turns a requirement / user story into structured
test cases (positive, negative, edge, boundary). Runs an open model — no API key, no cost.

## How to deploy (5 minutes, free)

1. Make a free account at <https://huggingface.co>.
2. Click **New → Space**. Choose **SDK: Gradio**, hardware **CPU basic (free)**.
3. Upload the three files from this folder: `app.py`, `requirements.txt`, `README.md`.
4. The Space builds itself (~3–5 min) and gives you a **public URL** — share it with your community.

## Notes
- Free CPU tier uses a small model (`Qwen2.5-0.5B-Instruct`) so it stays responsive.
  For better quality, enable a GPU in Space settings and switch `MODEL` in `app.py` to
  `Qwen/Qwen2.5-3B-Instruct`.
- The YAML block at the top of this file is the Hugging Face Space config — keep it.
