# 🧪 QA + AI Workshop Kit (Free · Cloud · No Installs)

A complete, hands-on learning kit that teaches a **software QA community** how to use AI —
turning requirements into test cases, building a custom QA assistant, and even fine-tuning a
model. **Everything runs free, in the cloud (Google Colab). Nothing installs on anyone's computer.**

Built for a mixed room: **juniors** get a real tool running in ~10 minutes (no coding needed),
**experts** get a real model-training track on a free GPU.

> **Repo:** https://github.com/hn-alchemist/qa-ai-workshop

---

## What is this?

This is a small, self-contained **learning kit** that helps a software QA team get hands-on with AI — safely, for free, and without installing anything. You open a link, it runs in your browser on Google's free cloud, and you work through short interactive lessons that solve real QA problems.

It is **not** a finished company product. Think of it as a guided playground: a place to learn what AI can and can't do for testing, so the team can make informed decisions about using it for real.

## Where can you use it?

Practical things you can do with the kit today (using non-confidential examples):

- **Draft test cases faster** — paste a requirement or user story, get positive, negative, edge, and boundary cases to review and refine.
- **Improve bug reports** — turn a vague report into a clear, standard one.
- **Build a team QA assistant** — shape the AI with your own standards, severity scale, and definition of done.
- **Answer questions from your own docs** — point it at QA policies/wikis and get cited answers (the RAG notebook).
- **Generate test cases at scale** — batch a whole backlog and export to Jira/TestRail CSV or Gherkin `.feature` files.
- **Measure quality objectively** — score and compare outputs with an AI judge.
- **Learn AND go deep** — juniors use point-and-click; experts can fine-tune and evaluate models.

**Good fit for:** learning sessions, internal upskilling, prototyping ideas, and speeding up the *first draft* of QA work.
**Not a fit for:** anything involving real customer data, PII, or confidential material, and it is not a replacement for tester judgement (always review the output).

---

## Important — please read first (learning use & data)

This kit is for **learning and experimentation first**. It is not an official company tool, and it comes with no guarantees. By using it, you accept responsibility for how you use it and what data you put into it.

- Use **only non-confidential, made-up, or anonymized examples**. Do **not** paste real customer data, personal data, credentials, or anything confidential or under NDA.
- The notebooks run on **third-party free cloud services** (Google Colab, Hugging Face). Any text you enter is processed on their servers, outside company control.
- AI output can be **wrong or incomplete**. Always review generated test cases yourself before relying on them.
- If you are unsure whether something is safe to use here, **check with your security/compliance team first**.

A full [Security Assessment](SECURITY_ASSESSMENT.md) is included in this repo covering data flow, risks, and recommendations.

---

## 📑 Table of contents
1. [Is this running on my computer?](#-is-this-running-on-my-computer)
2. [The free-cloud stack](#️-the-free-cloud-stack)
3. [Quick start (step by step)](#-quick-start-step-by-step)
4. [How to view and run the notebooks](#-how-to-view-and-run-the-notebooks)
5. [The notebooks (learning path)](#-the-notebooks-learning-path)
6. [⚠️ "Colab is loading old code" — how to fix](#️-colab-is-loading-old-code--how-to-fix)
7. [Common errors & fixes](#-common-errors--fixes)
8. [The shareable web app](#-the-shareable-web-app-hugging-face-space)
9. [Workshop run-of-show](#️-workshop-run-of-show-2-hours)
10. [What's in this kit](#-whats-in-this-kit)
11. [The big lessons](#-the-big-lessons-for-the-community)

---

## 💻 Is this running on my computer?

**No. Nothing runs or installs on your Mac/PC.** It all happens on Google's computers.

```
Your computer (just a browser)  ───►  Google's cloud computer (Colab)
                                       ├─ installs the AI libraries   ← here, NOT on you
                                       ├─ downloads the AI model       ← here
                                       └─ runs the AI on a free GPU    ← here
```

- ✅ Your computer stays clean — no Python packages, no big model files.
- ✅ It's free — Google provides the computer + GPU.
- ✅ It's temporary — close the tab (or ~90 min idle) and Google wipes that computer. Reopen the link to start fresh.
- ✅ Each community member gets their **own** free cloud computer when they click a link.

The only thing stored on your machine / GitHub is the **notebook files** (the "recipes").
The actual work happens on Google's computer when you open one in Colab.

---

## ☁️ The free-cloud stack

| What | Free tool | Why |
|------|-----------|-----|
| Run models & notebooks | **Google Colab** | Free T4 GPU, zero install — just open a link |
| Train / fine-tune | **Google Colab (free GPU)** | Real LoRA fine-tuning, $0 |
| Host the finished tool | **Hugging Face Spaces** | Free public URL to share with the whole community |
| The model | **Open models (Qwen2.5)** via Hugging Face | No API key, no cost |

---

## 🚀 Quick start (step by step)

**Step 1.** Click a notebook link below — it opens in Google Colab in your browser.
(Sign in with any free Google account if asked.)

**Step 2.** Turn on the free GPU: top menu → **Runtime → Change runtime type → T4 GPU → Save**.

**Step 3.** Click the first code cell, press **Shift + Enter** to run it. Wait for the ✅.
(The first cell installs libraries + downloads the model — ~1–2 min.)

**Step 4.** Keep pressing **Shift + Enter** down the notebook, one cell at a time, top to bottom.

**Step 5.** Done with one notebook? Open the next one and repeat. Each notebook is independent.

> 💡 **Tip for juniors:** In Notebook 02, after the model loads, there's an **⭐ Easy mode** cell
> with a **text box and a button** — just type a requirement and click. No coding at all.

---

## 👀 How to view and run the notebooks

There are three ways to open a notebook, depending on what you want to do:

| I want to… | Use | Link style |
|------------|-----|-----------|
| **Run it** (the main use) | **Google Colab** | The "Open in Colab" links below — always works |
| **Just read it** on the web | **nbviewer** | `https://nbviewer.org/github/hn-alchemist/qa-ai-workshop/blob/main/notebooks/<name>.ipynb` |
| Quick peek on GitHub | GitHub preview | Click the file in the repo |

> ℹ️ **Note about GitHub's preview:** GitHub sometimes shows **"Unable to render code block"** when previewing a notebook. This is a known, cosmetic issue on GitHub's side — **the notebook is fine and runs perfectly in Colab.** If you just want to *read* a notebook in the browser, use the **nbviewer** link (it never has this problem). If GitHub still shows it, hard-refresh the page (**Cmd/Ctrl + Shift + R**).
>
> Example nbviewer link: <https://nbviewer.org/github/hn-alchemist/qa-ai-workshop/blob/main/notebooks/02_test_case_generator.ipynb>

---

## 📓 The notebooks (learning path)

Open each one in Colab (click the link). Do them in order.

| # | Notebook | Level | Time | What it does | Open |
|---|----------|-------|------|--------------|------|
| 01 | First run | Everyone | 10 min | Run a real AI model free in the cloud; learn prompts | [Open in Colab](https://colab.research.google.com/github/hn-alchemist/qa-ai-workshop/blob/main/notebooks/01_first_run.ipynb) |
| 02 | Test-case generator ⭐ | Everyone | 20 min | Requirement → structured test cases (with a no-code text box) | [Open in Colab](https://colab.research.google.com/github/hn-alchemist/qa-ai-workshop/blob/main/notebooks/02_test_case_generator.ipynb) |
| 03 | Custom QA-Bot | Juniors+ | 20 min | Shape the model into *your team's* QA assistant via prompting | [Open in Colab](https://colab.research.google.com/github/hn-alchemist/qa-ai-workshop/blob/main/notebooks/03_custom_qa_assistant.ipynb) |
| 04 | Fine-tune (LoRA) | Experts | 60 min | **Train** a model on QA data with LoRA — free GPU | [Open in Colab](https://colab.research.google.com/github/hn-alchemist/qa-ai-workshop/blob/main/notebooks/04_finetune_lora.ipynb) |

### Advanced track (for experts — same simple journey, more depth)

| # | Notebook | What it does | Open |
|---|----------|--------------|------|
| 05 | Ask Your Test Docs (RAG) | Retrieval-Augmented Generation: answer questions from *your* docs, with citations — the core technique behind real AI assistants | [Open in Colab](https://colab.research.google.com/github/hn-alchemist/qa-ai-workshop/blob/main/notebooks/05_rag_ask_your_docs.ipynb) |
| 06 | Test cases at scale | Validation + auto-retry, **batch** a whole backlog, **export** to Jira/TestRail CSV and Gherkin `.feature` files | [Open in Colab](https://colab.research.google.com/github/hn-alchemist/qa-ai-workshop/blob/main/notebooks/06_batch_and_export.ipynb) |
| 07 | Measure quality (AI judge) | Score test cases objectively with an **LLM-as-judge**; compare prompts, models, or fine-tunes with numbers | [Open in Colab](https://colab.research.google.com/github/hn-alchemist/qa-ai-workshop/blob/main/notebooks/07_evaluate_quality.ipynb) |

---

## ⚠️ "Colab is loading old code" — how to fix

This is the most common confusion. There are **two different causes** — figure out which one you have.

### Cause A — The notebook *text* is the old version
You reopened a notebook but don't see the latest changes (e.g. the new text box isn't there).
This happens because Colab opened a **saved copy** (in your Google Drive) or a browser-cached page,
instead of the fresh file from GitHub.

**Fix — get the latest from GitHub:**
1. With the notebook open in Colab, go to **File → Revert to GitHub…**
2. Pick the branch **`main`** and confirm. Colab reloads the newest version from the repo. ✅

**If "Revert to GitHub" isn't shown** (because you opened a Drive copy):
1. Close the Colab tab.
2. Click the **Open in Colab link from this README again** (always opens fresh from GitHub).
3. If it *still* looks old, hard-refresh your browser on that tab: **Cmd + Shift + R** (Mac) / **Ctrl + Shift + R** (Windows).
4. Avoid clicking **"Save a copy in Drive"** during the workshop — that copy won't get future updates.

### Cause B — You edited a cell, but the model still uses the OLD behaviour
You changed a function (e.g. `generate_test_cases`) and re-ran it, but the result didn't change.
This is because Colab's running session still holds the **old function in memory**.

**Fix — restart the session and re-run from the top:**
1. Menu → **Runtime → Restart session** (or **Restart runtime**).
2. Then **Runtime → Run all** (or press Shift+Enter from the very first cell down).

> 🧠 Rule of thumb: changed the *file/notebook*? → **Revert to GitHub** (Cause A).
> Changed a *cell and re-ran but nothing changed*? → **Restart session** (Cause B).

---

## 🧯 Common errors & fixes

| Error you see | Why | Fix |
|---------------|-----|-----|
| `SyntaxError: unterminated string literal` | A text value spans **multiple lines inside single quotes** `'...'` | Use **triple quotes** `"""..."""` for multi-line text. Or just use the **⭐ Easy mode text box** in Notebook 02 — no quotes needed. |
| `NameError: name 'chat' is not defined` | You ran a later cell before the setup cell | Run cells **top to bottom**, starting from cell 1. |
| `No GPU` / very slow | GPU not enabled | **Runtime → Change runtime type → T4 GPU → Save**, then re-run. |
| "No test cases parsed" / weird output | The small model returned imperfect JSON | Re-run the cell. For better quality, change `MODEL` to `Qwen/Qwen2.5-3B-Instruct` (commented tip is in the cell). |
| Session disconnected / variables gone | Colab wiped the idle session | **Runtime → Run all** to re-run from the top. |
| Notebook 04 can't find the dataset | The data file wasn't uploaded | Upload `data/qa_finetune_dataset.jsonl` via the 📁 **Files** panel on the left. |

> 📝 **Logs:** Notebook 02 writes a log to `qa_tool.log` (see the 📁 Files panel). If something
> fails, open that file — it records what went wrong for each run.

### The string-quote rule (memorize this)
| Your text is… | Use |
|---|---|
| One line | `'...'` or `"..."` |
| Multiple lines | `"""..."""` (triple quotes) |

---

## 🌐 The shareable web app (Hugging Face Space)

The `huggingface-space/` folder is a ready-to-deploy **Gradio** web app — the test-case generator
as a real website. Deploy it once (5 min, free) and share **one public URL** with your whole
community; nobody needs Colab or any setup.

**Deploy steps:**
1. Make a free account at https://huggingface.co
2. **New → Space** → SDK **Gradio** → hardware **CPU basic (free)**.
3. Upload `app.py`, `requirements.txt`, `README.md` from the `huggingface-space/` folder.
4. It builds itself (~3–5 min) and gives you a public URL. Done.

See [`huggingface-space/README.md`](huggingface-space/README.md) for details.

---

## 🗓️ Workshop run-of-show (~2 hours)

1. **(15 min)** Intro: what an LLM is, why open/free models, and *nothing installs locally*.
2. **(20 min)** Everyone runs **Notebook 01** together.
3. **(25 min)** Everyone runs **Notebook 02** — the "wow" moment. Use the ⭐ Easy mode text box.
   Discuss: did it find edge cases you'd miss? Did it hallucinate any?
4. **(5 min)** Split the room.
5. **(30 min)** Juniors → **Notebook 03** (custom QA-Bot). Experts → **Notebook 04** (fine-tuning).
6. **(15 min)** Regroup: compare base model vs. fine-tuned. Demo the deployed Hugging Face Space.
7. **(10 min)** Wrap: where AI helps QA, where it doesn't, what to try next.

---

## 📁 What's in this kit

```
qa-ai-workshop/
├── README.md                          ← you are here
├── notebooks/
│   ├── 01_first_run.ipynb             ← everyone: first AI run
│   ├── 02_test_case_generator.ipynb   ← everyone: the QA tool (+ no-code text box & logging)
│   ├── 03_custom_qa_assistant.ipynb   ← juniors+: custom QA-Bot via prompting
│   └── 04_finetune_lora.ipynb         ← experts: real LoRA fine-tuning
├── huggingface-space/                 ← deploy the tool as a free web app
│   ├── app.py
│   ├── requirements.txt
│   └── README.md
└── data/
    ├── sample_requirements.txt        ← many requirements to try (easy, tricky, high-stakes)
    ├── sample_bug_reports.txt         ← bug reports to feed the QA-Bot (Notebook 03)
    ├── sample_questions.txt           ← questions for the RAG notebook (Notebook 05)
    ├── playground_challenges.md       ← ⭐ experiments to think smarter (start here to explore)
    └── qa_finetune_dataset.jsonl      ← 12 example pairs for the fine-tuning notebook
```

> 🎮 **Want to actually learn, not just run cells?** Open
> [`data/playground_challenges.md`](data/playground_challenges.md) — it has graded challenges
> (warm-up → advanced) and discussion questions that build real intuition for where AI helps
> QA and where it fails.

---

## 🧠 The big lessons for the community

- AI is a **fast first draft** for QA work — not a replacement for tester judgement.
- **90% of "custom AI" is just a great prompt** (Notebook 03). Train only when you must.
- **Fine-tuning is accessible** — LoRA on a free GPU (Notebook 04). Data quality matters more than model size.
- **Good tools take input from a UI**, not from people editing code — that's why Notebook 02 has a text box.
- It's all **free and open** — your community can keep building after the workshop.
