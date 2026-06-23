"""
QA Test-Case Generator — Hugging Face Space (free, shareable web app).

Deploy:
  1. Create a free account at https://huggingface.co
  2. New → Space → SDK: Gradio → (free CPU hardware is fine)
  3. Upload this app.py + requirements.txt + README.md
  4. The Space builds itself and gives you a public URL to share with your community.

No API key. No cost. Runs an open model (Qwen2.5) right inside the Space.
"""
import json
import re

import gradio as gr
import torch
from transformers import pipeline

# 0.5B keeps it responsive on the FREE CPU tier. Upgrade to 1.5B/3B if you enable a GPU.
MODEL = "Qwen/Qwen2.5-0.5B-Instruct"

chat = pipeline(
    "text-generation",
    model=MODEL,
    torch_dtype=torch.bfloat16 if torch.cuda.is_available() else torch.float32,
    device_map="auto" if torch.cuda.is_available() else None,
)

SYSTEM = """You are a senior QA engineer. You write thorough, practical test cases.
For a given requirement, produce test cases covering POSITIVE, NEGATIVE, EDGE, and BOUNDARY scenarios.
Return ONLY valid JSON (no prose, no markdown fences) shaped exactly as:
{"test_cases": [
  {"id": "TC-01", "title": "...", "type": "positive|negative|edge|boundary",
   "priority": "high|medium|low", "steps": ["..."], "expected": "..."}
]}"""


def generate(requirement):
    if not requirement or not requirement.strip():
        return "Please enter a requirement or user story.", []
    user = f"Requirement:\n{requirement}\n\nGenerate 6-10 test cases as JSON."
    out = chat(
        [{"role": "system", "content": SYSTEM}, {"role": "user", "content": user}],
        max_new_tokens=1200,
        do_sample=False,
    )
    text = out[0]["generated_text"][-1]["content"]
    match = re.search(r"\{.*\}", text, re.DOTALL)
    if not match:
        return "Could not parse model output. Raw output:\n\n" + text, []
    try:
        data = json.loads(match.group(0))
    except json.JSONDecodeError:
        return "Model returned invalid JSON. Try again. Raw output:\n\n" + text, []

    rows = []
    for tc in data.get("test_cases", []):
        steps = tc.get("steps", [])
        steps = " → ".join(steps) if isinstance(steps, list) else str(steps)
        rows.append([
            tc.get("id", ""), tc.get("title", ""), tc.get("type", ""),
            tc.get("priority", ""), steps, tc.get("expected", ""),
        ])
    return f"✅ Generated {len(rows)} test cases.", rows


with gr.Blocks(title="QA Test-Case Generator") as demo:
    gr.Markdown(
        "# 🧪 AI Test-Case Generator\n"
        "Paste a **requirement or user story** → get structured test cases "
        "(positive, negative, edge, boundary). Free & open-source — built for our QA community."
    )
    req = gr.Textbox(
        label="Requirement / User story",
        lines=3,
        value="As a user, I can reset my password via an email link that expires in 15 minutes.",
    )
    btn = gr.Button("Generate test cases ✨", variant="primary")
    status = gr.Markdown()
    table = gr.Dataframe(
        headers=["ID", "Title", "Type", "Priority", "Steps", "Expected result"],
        wrap=True,
        label="Test cases",
    )
    btn.click(generate, inputs=req, outputs=[status, table])
    gr.Markdown("_Reminder: AI gives a fast first draft — a tester's review is still essential._")


if __name__ == "__main__":
    demo.launch()
