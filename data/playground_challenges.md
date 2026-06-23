# 🎮 Playground Challenges — experiment and think smarter

The notebooks work out of the box. The *real* learning is when you start poking at them.
Here are challenges, grouped by skill level. Try them, then discuss what happened and **why**.

> The goal is not to get a "right answer" — it's to build intuition for what AI is good at,
> where it breaks, and how to steer it.

---

## 🟢 Warm-up (everyone)

1. **Change the model's tone.** In Notebook 01, edit the `system` message to "You are a sarcastic QA engineer." Re-run. What changed, what didn't?
2. **Feed it a vague requirement.** In Notebook 02, try `Users should be able to search.` What did the AI *assume*? Is that dangerous in real life?
3. **Spot the hallucination.** Ask the plain model (Notebook 01) "What is our company's bug severity policy?" It has no idea — does it admit that, or invent one?
4. **Compare prompts.** In Notebook 02, generate test cases, then add "Focus especially on security and abuse cases" to the prompt and re-run. How much did it improve?

---

## 🟡 Intermediate (think like a tester)

5. **Break the JSON.** In Notebook 02, ask for "200 test cases." Does the output stay valid? What does the retry logic do? (This is why validation matters.)
6. **Ambiguity hunt.** Give it `As a user, I can transfer money to another account.` Does it ask about limits, currencies, fraud, failed transfers? List what a *human* tester would add that the AI missed.
7. **Format shifting.** Ask for the same test cases as: (a) a table, (b) Gherkin, (c) a checklist, (d) Playwright pseudo-code. Which format does it do best?
8. **Persona power.** In Notebook 03, write a QA-Bot persona that enforces *your* real team's bug template. Feed it the worst report from `sample_bug_reports.txt`. Good enough to use?
9. **RAG honesty test.** In Notebook 05, ask a question that's NOT in the docs (see `sample_questions.txt`). Does it say "I don't know" or make something up? Now remove the "say I don't know" rule from the system prompt and try again — see the difference.

---

## 🔴 Advanced (for the experts)

10. **Two-document reasoning (RAG).** Ask a question that requires combining two policies, e.g. *"If a regression test uses real customer data, which rules did we break?"* Did it cite both sources?
11. **Chunking experiment.** In Notebook 05, replace one long document with the same text split into 3 smaller chunks. Does retrieval get better or worse?
12. **Judge the judge (Notebook 07).** Run the AI judge on the *same* candidate 3 times. Do the scores match? What does that tell you about trusting a single AI evaluation?
13. **Prove fine-tuning worked.** Generate test cases with the base model and your fine-tuned model (Notebook 04), then score both with the judge (Notebook 07). Did training actually help — with numbers?
14. **Adversarial requirement.** Write a requirement designed to trick the AI into missing a critical edge case (e.g. a boundary at exactly 0, or a negative number). Did it catch it?
15. **Cost vs quality.** Switch Notebook 02 to the 3B model. Is the quality jump worth the extra time? When would you pick small vs large?

---

## 💬 Group discussion questions

- Where did the AI save you real time today? Where did it waste your time?
- What's one task you would trust it with, and one you never would?
- If you gave this to a brand-new tester, would it help them or mislead them?
- What would it take to use this on *real* work safely? (Hint: see the Security Assessment.)

---

## 🧪 Make your own

Add your own tricky requirements, bug reports, or questions to the files in this `data/` folder
and share what you discover with the team. The best examples often come from real testing pain.
