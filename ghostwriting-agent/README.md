# Ghostwriting Agent

An AI agent that finds real demand for practical guides and genre fiction, then researches, outlines, drafts,
self-edits and fact-checks them, and prepares each product for a human to approve and list for sale.
It never publishes, lists, spends or contacts anyone on its own. Built by **Pelumi, Founder, Agent Forge**.

> This is a **portfolio copy**. It shows the structure of the agent: folder layout and the names of its modules, classes and functions.
> Every function body, prompt, setting, test and piece of data has been removed, so nothing here can run.

## What it does

| Stage | Jobs |
|---|---|
| A. Demand scout | Collects real questions people ask, checks what already sells, proposes and scores product angles |
| B. Planning | Reader brief, research pack from primary sources, chapter-by-chapter outline |
| C. Writing | Drafts each chapter or scene, self-edits, fact-checks every claim against a source, checks originality |
| D. Packaging | Titles, cover brief, sales page, pricing proposal, metadata and a review package |
| Fiction | A story bible, voice guide and continuity ledger per series; scene beats, drafting, automatic checks and revision |

```mermaid
flowchart LR
    A[Demand research] --> B[Score + shortlist] --> C[Brief + outline]
    C --> D[Plan beats] --> E[Draft scene] --> F[Code + AI checks] --> G[Revise]
    G --> H[Review dashboard] --> I{Human approves?}
    I -- yes --> J[Package for sale]
```

## Built-in safety

- Propose only: nothing is listed or sent without a human approval in the review dashboard.
- Spend gate: cost is estimated before a batch; paid runs need a typed approval phrase.
- Checks in code and AI: every scene goes through rule-based prose checks and a model check before review.
- No rewriting of other people's books or courses.

## Tech stack

Python 3.11 · Claude API · Streamlit review dashboard · YAML project templates · pytest

**Contact:** agentforgehq.studio@gmail.com · https://agentforgehq.netlify.app

© 2026 Agent Forge. All rights reserved. Shared for viewing only.
