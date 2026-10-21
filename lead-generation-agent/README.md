# Agent Forge: AI Lead Generation Agent

An AI agent that finds small businesses, checks whether they are a good fit, and prepares
personalised outreach emails for a human to review. Built by **Pelumi, Founder, Agent Forge**.

> This is a **portfolio copy**. It explains how the system works and shows sample output.
> The working code, prompts, qualification rules, configuration and data are kept private,
> so nothing here can run the agent. All businesses, emails and numbers in the samples are made up.

## What it does

| Step | What happens |
|---|---|
| 1. Find | Searches business directories and Google Maps for a chosen trade in a chosen city (US, UK, Australia, Nigeria) |
| 2. Clean | Removes duplicates (name, phone, website, company number) and anyone on the do-not-contact list |
| 3. Verify | Confirms the business is real and active, and checks its website |
| 4. Qualify | Claude (Anthropic) reads the business details and website and judges fit against a written checklist |
| 5. Decide | Plain code, not AI, makes the final call: New Lead, Needs Review, or skip, plus which contact channels are legally allowed |
| 6. Log | Writes good leads, a run summary and costs to a shared Google Sheet |
| 7. Draft | Writes an outreach email per lead from fixed templates; a Google Apps Script turns them into Gmail drafts |
| 8. Human | A person reads every draft and presses send. **The agent never contacts anyone itself.** |

See [docs/architecture.md](docs/architecture.md) for the full flow diagram.

## Highlights

- **Cost per lead tracked on every run.** Typical real runs cost about $0.01 to $0.02 per qualified lead.
- **Cheap checks first.** Free filters run before any paid API call, so money is only spent on promising businesses.
- **Safety switches.** A kill switch, a monthly budget guard (warns at 80%, stops at 100%), daily caps per market,
  and dry run by default. See [docs/safety-and-cost-controls.md](docs/safety-and-cost-controls.md).
- **Compliance built in.** Per-country rules decide whether email, phone or LinkedIn outreach is allowed
  (for example US CAN-SPAM footers and UK rules on cold email), and sensitive sectors are logged silently and never contacted.
- **AI where it helps, code where it matters.** Claude judges fit; deterministic code applies every rule, cap and channel decision.
- **Heavily tested.** About 1,900 automated tests run on saved, synthetic sample pages, with no network calls.
- **Runs in the cloud.** GitHub Actions workflows for manual runs, a schedule, email drafts and a daily health check.

## Tech stack

Python 3 · Anthropic Claude API · Serper (Google Maps search) · Make.com (page fetching) ·
Google Sheets API · Google Apps Script + Gmail · GitHub Actions · pytest

## What is in this repo

| Path | What it is |
|---|---|
| `docs/architecture.md` | How the pieces fit together, with a diagram |
| `docs/safety-and-cost-controls.md` | Kill switch, budget guard, caps, compliance |
| `sample-output/` | Example leads, run summary and email draft (all fictional) |
| `snippets/` | Two small, simplified code examples written for this showcase |
| `leadgen/`, `scripts/` | Skeleton of the real code: module, class and function names only, every body removed |
| `config/` | Config file names only, every value removed |
| `.github/workflows/` | Workflow names only, steps removed |
| `.env.example` | The names of the settings the real agent needs (no values) |

## Other agents Agent Forge builds

The same approach (find or read data, let AI judge, let code decide, keep a human in charge) is used for client
agents such as quote-drafting and quote follow-up for trades businesses, CRM follow-up agents, and admin assistants
for recruitment and real estate firms.

**Contact:** agentforgehq.studio@gmail.com · https://agentforgehq.netlify.app

© 2026 Agent Forge. All rights reserved. Shared for viewing only.
