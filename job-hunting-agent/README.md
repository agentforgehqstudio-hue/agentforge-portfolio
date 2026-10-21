# Taproot: Job Hunting Agent

An AI agent that finds job postings, scores each one out of 100 against a candidate's evidence profile,
and prepares (never submits) applications for the strongest matches. Built by **Pelumi, Founder, Agent Forge**.

> This is a **portfolio copy**. It shows the structure of the agent: folder layout and the names of its modules, classes and functions.
> Every function body, prompt, setting, test and piece of data has been removed, so nothing here can run.

## What it does

| Step | What happens |
|---|---|
| 1. Search | Runs saved searches through a search API |
| 2. Normalise | Cleans titles, companies, locations and pay into one format |
| 3. Dedupe | Skips postings already seen |
| 4. Score | Rates each job on skills, seniority, domain and practical fit; only real work evidence counts |
| 5. Log | Writes the shortlist and a run log to a Google Sheet and a digest |
| 6. Prepare | Picks the right CV and drafts the application for a human to check and submit |

```mermaid
flowchart LR
    A[Saved searches] --> B[Search API] --> C[Normalise] --> D[Dedupe]
    D --> E[Score out of 100] --> F[Sheet + digest] --> G[Human applies]
```

## Built-in safety

- Dry run by default; live mode needs an extra confirmation setting.
- Kill switch: a file named KILL or one setting stops every run.
- Monthly credit budget with monitoring.
- Secrets are redacted from every log line.

## Tech stack

Python 3.11 · Claude API · Serper search API · Google Sheets · pytest

**Contact:** agentforgehq.studio@gmail.com · https://agentforgehq.netlify.app

© 2026 Agent Forge. All rights reserved. Shared for viewing only.
