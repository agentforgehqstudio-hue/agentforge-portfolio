"""Skeleton only. Implementation removed in the public copy."""

class CheckRun:
    pass

class ModelCounts:
    pass

def canon_file(project, tag):
    raise NotImplementedError('Implementation removed in the public copy.')

def latest_ledger_update(project, tag):
    raise NotImplementedError('Implementation removed in the public copy.')

class LedgerPlan:

    @property
    def applicable(self):
        raise NotImplementedError('Implementation removed in the public copy.')

def ledger_plan(project, tag, stored, ledger_text, draft_text=...):
    raise NotImplementedError('Implementation removed in the public copy.')

def report_paths(project, tag):
    raise NotImplementedError('Implementation removed in the public copy.')

def ledger_plan_for_text(stored, ledger_text):
    raise NotImplementedError('Implementation removed in the public copy.')

def render_report(tag, draft_rel, words, code, model_lines, model_note, verdict, model_name, when, cost_text, act_lines=...):
    raise NotImplementedError('Implementation removed in the public copy.')

def valid_findings(inp):
    raise NotImplementedError('Implementation removed in the public copy.')

def refresh_report(project_dir, chapter, scene, draft_path=...):
    raise NotImplementedError('Implementation removed in the public copy.')

def estimate_checks(llm, project_dir, chapter, scene, prompts_dir=...):
    raise NotImplementedError('Implementation removed in the public copy.')

def run_checks(llm, project_dir, chapter, scene, dry_run=..., draft_path=..., prompts_dir=...):
    raise NotImplementedError('Implementation removed in the public copy.')
