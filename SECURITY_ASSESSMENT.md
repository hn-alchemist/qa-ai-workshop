# Security Assessment — QA + AI Workshop Kit

**Purpose:** An honest assessment of the security and privacy considerations of this kit, so the team and management can make an informed decision about how to use it.

**Scope:** The notebooks, the sample data, the GitHub repository, and the optional Hugging Face web app in this project.

**Summary verdict:** Low risk for learning with sample or made-up data. The one real consideration is data handling — content entered into the tool is processed on third-party free cloud services, so confidential or customer data must not be used.

---

## 1. What the kit is and how data flows

- The notebooks run on **Google Colab**, a free cloud service. The code, the AI model, and any text the user enters are all processed on a temporary Google-hosted machine, not on company infrastructure.
- The AI model is **open source (Qwen2.5)** and runs locally on that Colab machine. It does **not** call an external AI vendor's API, and it does not send data to a vendor that trains on it.
- The optional web app runs on **Hugging Face Spaces**, also a third-party cloud.
- The **GitHub repository** stores only the workshop code and fictional sample data.

Data flow in plain terms: a user's browser sends typed text to a Google Colab machine, the model processes it there, and the result is shown back in the browser. The Colab machine is wiped when the session ends.

---

## 2. Risk assessment

| # | Risk | Likelihood | Impact | Rating | Mitigation |
|---|------|-----------|--------|--------|------------|
| 1 | Confidential data (requirements, customer info, PII, credentials, NDA material) entered into the tool and processed on third-party cloud | Medium | High | **Medium–High** | Policy: use only non-confidential or made-up examples. Stated clearly in the README. Awareness during the workshop. |
| 2 | AI output is wrong or incomplete, leading to poor test coverage if trusted blindly | Medium | Medium | **Medium** | Treat output as a first draft; human review is mandatory. Stated in README and notebooks. |
| 3 | Sensitive data accidentally committed to the public GitHub repo | Low | High | **Low–Medium** | Repo contains only fictional sample data. No real data is committed. Reviewers should check before any future commits. |
| 4 | Public Hugging Face web app exposes the tool to anyone with the link | Low | Medium | **Low** | Keep the Space private, or do not deploy it. Same no-confidential-data rule applies. |
| 5 | Supply chain — installing Python packages and downloading model weights from third parties | Low | Medium | **Low** | Reputable sources only (Hugging Face, PyPI, Qwen by Alibaba). No untrusted remote code execution is enabled. |
| 6 | Credential or secret leakage | Very Low | High | **Low** | The kit uses no API keys or secrets, so there is nothing to leak. |

---

## 3. Detailed notes

**Data residency (Risk 1) — the main point.**
Anything typed into the tool leaves the company's controlled environment and is processed on Google Colab. This is not a hacking risk; it is a confidentiality and compliance consideration. The model running locally on Colab means there is no AI vendor training on the data, but the data still sits temporarily on a third-party machine. The control is procedural: do not enter confidential data.

**Output quality (Risk 2).**
The kit deliberately uses small models for speed and cost. Generated test cases can miss cases or invent incorrect ones. This is a quality risk, not a security one, but it matters: the kit is a productivity aid, not a replacement for tester judgement.

**Repository hygiene (Risk 3).**
The sample requirements and the fine-tuning dataset are generic and fictional. They contain nothing about the company, its systems, or its customers. This should be maintained — no real artifacts should ever be committed.

**No secrets (Risk 6).**
A deliberate design choice was to require no API keys. This removes a whole class of credential-leak risk.

---

## 4. Recommendations

1. **Data rule (required):** Use only non-confidential, anonymized, or made-up examples. No customer data, PII, credentials, or NDA material.
2. **Human review (required):** Always review AI-generated test cases before using them.
3. **Keep it private where appropriate:** Do not deploy the public web app unless needed; keep it private if deployed.
4. **For real or production use:** Move from free third-party cloud to company-controlled infrastructure (self-hosted model) so data stays in-house.
5. **Sign-off:** Obtain a quick review from the security/compliance team before any use involving real data.

---

## 5. Conclusion

As a learning exercise with sample data, this kit carries low security risk and introduces no secrets or company data into third-party systems. The single item that needs active control is what users type into the tool. With the stated data rule and human review in place, it is suitable for community learning. Any move toward real or production use should first move the processing onto company-controlled infrastructure and go through a compliance review.

This assessment reflects the kit as published in this repository and should be revisited if the architecture, data, or usage changes.
