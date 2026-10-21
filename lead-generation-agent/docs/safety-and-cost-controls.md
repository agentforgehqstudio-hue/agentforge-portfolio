# Safety and cost controls

| Control | What it does |
|---|---|
| Dry run by default | A real run needs an explicit flag **and** an environment setting; otherwise it only prints what it would do |
| Kill switch | A repository variable must be exactly `true`; it is checked before every paid call, so a run can be stopped mid-way |
| Monthly budget guard | Month-to-date spend is stored; warns at 80% and stops at 100% of the budget |
| Daily caps | A quota per market (for example 7 US and 3 Australia leads a day) and a global daily cap |
| Confirm phrase | Live runs from GitHub need a typed confirmation phrase |
| Never contacts anyone | The agent only writes drafts; a person sends every email |
| No double contact | Before a Gmail draft is made, Gmail is searched so a business is never emailed twice |
| Allowed channels | Per-country rules decide if email, phone or LinkedIn is allowed for each lead |
| Sensitive sectors | Legal and finance businesses are logged silently with no contact details and never contacted |
| Do-not-contact list | Anyone who opts out is suppressed on every future run |
| Secrets | Keys live only in GitHub Secrets or a local `.env` that git ignores; nothing secret is ever logged |
| Draft checks | AI-written opening lines are rejected unless they are one plain sentence with no placeholders |

Cost figures in the Run Summary are estimates from published API prices, not bills.
