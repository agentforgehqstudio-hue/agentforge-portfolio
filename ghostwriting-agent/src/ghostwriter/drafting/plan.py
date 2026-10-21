"""Skeleton only. Implementation removed in the public copy."""

def plans_dir(project_dir):
    raise NotImplementedError('Implementation removed in the public copy.')

def plan_versions(project_dir, chapter):
    raise NotImplementedError('Implementation removed in the public copy.')

def latest_plan(project_dir, chapter):
    raise NotImplementedError('Implementation removed in the public copy.')

def next_plan_version(project_dir, chapter):
    raise NotImplementedError('Implementation removed in the public copy.')

def scene_numbers(plan_text):
    raise NotImplementedError('Implementation removed in the public copy.')

def scene_entry(plan_text, scene):
    raise NotImplementedError('Implementation removed in the public copy.')

def section_text(plan_text, heading):
    raise NotImplementedError('Implementation removed in the public copy.')

def bullets(plan_text, heading):
    raise NotImplementedError('Implementation removed in the public copy.')

def constraints_text(plan_text):
    raise NotImplementedError('Implementation removed in the public copy.')

def approved_plan(project_dir, runs_dir, chapter):
    raise NotImplementedError('Implementation removed in the public copy.')

def approve_plan(project_dir, runs_dir, chapter, plan_name, note=...):
    raise NotImplementedError('Implementation removed in the public copy.')

def save_plan_edit(project_dir, chapter, new_text):
    raise NotImplementedError('Implementation removed in the public copy.')

class PlanRow:
    pass

def list_plans(project, runs_dir):
    raise NotImplementedError('Implementation removed in the public copy.')

class PlanResult:
    pass

def volatile_sections(project, chapter):
    raise NotImplementedError('Implementation removed in the public copy.')

def estimate_plan(llm, project_dir, chapter, prompts_dir=...):
    raise NotImplementedError('Implementation removed in the public copy.')

def run_plan(llm, project_dir, chapter, dry_run=..., prompts_dir=...):
    raise NotImplementedError('Implementation removed in the public copy.')
