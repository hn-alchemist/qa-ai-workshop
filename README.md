# 🧪 QA + AI Workshop Kit (Free · Cloud · No Installs)

A hands-on learning kit for a software QA community. **Everything runs free, in the cloud.**
No paid API keys. No local installs. Juniors just open a link; experts get a real
model-training track on a free GPU.

> Built for a mixed room: **juniors** get something real running in 10 minutes,
> **experts** actually **fine-tune** a model — all on free cloud GPUs.

---

## ☁️ The free-cloud stack

| What | Free tool | Why |
|------|-----------|-----|
| Run models & notebooks | **Google Colab** | Free T4 GPU, zero install — just open a link |
| Train / fine-tune | **Google Colab (free GPU)** | Real LoRA fine-tuning, $0 |
| Host the finished tool | **Hugging Face Spaces** | Free public URL to share with the whole community |
| The model | **Open models (Qwen2.5)** via Hugging Face | No API key, no cost |

---

## ▶️ One-click open in Colab (for the dry run)

| Notebook | Open |
|----------|------|
| 01 · First run | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/hn-alchemist/qa-ai-workshop/blob/main/notebooks/01_first_run.ipynb) |
| 02 · Test-case generator | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/hn-alchemist/qa-ai-workshop/blob/main/notebooks/02_test_case_generator.ipynb) |
| 03 · Custom QA-Bot | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/hn-alchemist/qa-ai-workshop/blob/main/notebooks/03_custom_qa_assistant.ipynb) |
| 04 · Fine-tune (LoRA) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/hn-alchemist/qa-ai-workshop/blob/main/notebooks/04_finetune_lora.ipynb) |

---

## 🧭 Learning path (do the notebooks in order)

Click an **Open in Colab** badge above (works once this repo is on GitHub),
or go to <https://colab.research.google.com> → **Upload** and pick a `.ipynb`
from the `notebooks/` folder.

| Step | Notebook | Level | Time | What happens |
|------|----------|-------|------|--------------|
| 1 | `notebooks/01_first_run.ipynb` | Everyone | 10 min | Run a real AI model free in the cloud; learn prompts |
| 2 | `notebooks/02_test_case_generator.ipynb` | Everyone | 20 min | The QA tool: requirement → structured test cases ✨ |
| 3 | `notebooks/03_custom_qa_assistant.ipynb` | Juniors+ | 20 min | Shape the model into *your team's* QA-Bot (prompting) |
| 4 | `notebooks/04_finetune_lora.ipynb` | Experts | 60 min | **Fine-tune** a model on QA data with LoRA — free GPU |

> ⚙️ In every notebook: enable the free GPU via **Runtime → Change runtime type → T4 GPU**.

---

## 🌐 The shareable web app (Hugging Face Space)

`huggingface-space/` is a ready-to-deploy **Gradio** app — the test-case generator as a
website. Deploy it once (5 min, free) and share **one public URL** with your whole community,
no one needs Colab or any setup. See [`huggingface-space/README.md`](huggingface-space/README.md).

---

## 📁 What's in this kit

```
qa-ai-workshop/
├── README.md                          ← you are here
├── notebooks/
│   ├── 01_first_run.ipynb             ← everyone: first AI run
│   ├── 02_test_case_generator.ipynb   ← everyone: the QA tool
│   ├── 03_custom_qa_assistant.ipynb   ← juniors+: custom QA-Bot via prompting
│   └── 04_finetune_lora.ipynb         ← experts: real LoRA fine-tuning
├── huggingface-space/                 ← deploy the tool as a free web app
│   ├── app.py
│   ├── requirements.txt
│   └── README.md
└── data/
    ├── sample_requirements.txt        ← requirements to try the tool on
    └── qa_finetune_dataset.jsonl      ← 12 example pairs for the fine-tuning notebook
```

---

## 🗓️ Suggested workshop run-of-show (~2 hours)

1. **(15 min)** Intro: what an LLM is, why local/open models, why free.
2. **(20 min)** Everyone runs **Notebook 01** together.
3. **(25 min)** Everyone runs **Notebook 02** — the "wow" moment. Discuss: did it find edge cases you'd miss? Did it hallucinate any?
4. **(5 min)** Split the room.
5. **(30 min)** Juniors → **Notebook 03** (custom QA-Bot). Experts → **Notebook 04** (fine-tuning).
6. **(15 min)** Regroup: compare base model vs. fine-tuned. Demo the deployed **Hugging Face Space**.
7. **(10 min)** Wrap: where AI helps QA, where it doesn't, what to try next.

---

## 🧠 The big lessons for the community

- AI is a **fast first draft** for QA work — not a replacement for tester judgement.
- **90% of "custom AI" is just a great prompt** (Notebook 03). Train only when you must.
- **Fine-tuning is accessible** — LoRA on a free GPU (Notebook 04). Data quality matters more than model size.
- It's all **free and open** — your community can keep building after the workshop.
