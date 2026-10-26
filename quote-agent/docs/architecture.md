# Quote Agent: Architecture

The whole agent is one Google Apps Script file bound to one Google Sheet. There is no server to run:
the script is deployed as a web app (to receive form posts and owner clicks) and a timer runs it every 5 minutes.

## Pieces

| Piece | Role |
|---|---|
| Web form | Collects the enquiry and posts it to the script's web app link |
| Google Sheet | The database and the admin screen, one tab per kind of record |
| Apps Script web app | `doPost` takes enquiries; `doGet` serves the owner's Approve and Edit pages |
| Claude API | Drafts the estimate as structured JSON from the enquiry and the price list |
| Gmail | Sends the acknowledgement, owner, estimate and follow-up emails, and is checked for replies |
| 5-minute timer | Retries stuck drafts, watches for replies and STOP, sends due follow-ups |

## Sheet tabs

| Tab | Holds |
|---|---|
| Profiles | One row per business: name, trade, tone, currency, owner contact, follow-up timing |
| PriceList | Each business's items with low and high prices |
| Quotes | One row per enquiry, with its status and every timestamp |
| Log | Every email sent and every error |
| TestCases | Sample jobs used to check the drafting prompt without sending email |

Columns are found by header name, so the owner can reorder them freely. One sheet can serve several businesses.

## Flow A: enquiry to sent estimate

```mermaid
sequenceDiagram
    participant C as Customer
    participant F as Web form
    participant S as Apps Script
    participant AI as Claude
    participant O as Owner
    C->>F: Fills in job details
    F->>S: doPost (webhook)
    S->>C: "We've got your request"
    S->>AI: Enquiry + price list
    AI-->>S: Draft line items (JSON)
    S->>S: Drop unknown items, reset prices, total
    S->>O: Draft with Approve / Edit links
    O->>S: Approve (or edit, then send)
    S->>C: Estimate email
```

## Flow B: replies and follow-ups (every 5 minutes)

```mermaid
flowchart TD
    T[Timer] --> R[Retry failed drafts]
    T --> W[Check inbox for customer replies]
    W -->|STOP| X[Status: Stopped]
    W -->|Any other reply| Y[Status: Replied, owner notified]
    T --> U{Follow-up due?}
    U -->|2 days quiet| F1[Follow-up 1]
    U -->|5 days quiet| F2[Follow-up 2]
    F2 --> Q[Status: Quiet]
```

## Quote lifecycle

`New` → `Drafted` (or `Needs info` → `Info requested`) → `Sent` → `Follow-up 1` → `Follow-up 2` → `Quiet`,
with `Replied`, `Stopped` and `Error` reachable along the way. Each status change is stamped on the quote's row.

## Testing

The real build has offline tests that fake Google's services and the Claude API, so the full flow
(intake, drafting, price checks, approval, replies, STOP and follow-ups) runs with no network calls.
They are not included in this copy.
