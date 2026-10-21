"""Skeleton only. Implementation removed in the public copy."""

class ReviewError(Exception):
    pass

def spend_rows(runs_dir):
    raise NotImplementedError('Implementation removed in the public copy.')

def daily_series(runs_dir):
    raise NotImplementedError('Implementation removed in the public copy.')

class SceneRow:
    pass

def list_scenes(project_dir, runs_dir):
    raise NotImplementedError('Implementation removed in the public copy.')

class CanonItem:
    pass

class SceneReview:
    pass

def build_review(project_dir, chapter, scene):
    raise NotImplementedError('Implementation removed in the public copy.')

class ApprovalPlan:
    pass

class ApprovalResult:
    pass

def plan_approval(project_dir, chapter, scene):
    raise NotImplementedError('Implementation removed in the public copy.')

def approve(plan, runs_dir, apply_ledger, note=..., action=...):
    raise NotImplementedError('Implementation removed in the public copy.')

class BatchScene:
    pass

def batch_scenes(project_dir, runs_dir):
    raise NotImplementedError('Implementation removed in the public copy.')

def batch_reports(project_dir):
    raise NotImplementedError('Implementation removed in the public copy.')

def save_edit(project_dir, chapter, scene, new_body):
    raise NotImplementedError('Implementation removed in the public copy.')

def run_free_checks(project_dir, chapter, scene):
    raise NotImplementedError('Implementation removed in the public copy.')

def estimate_full_checks(llm, project_dir, chapter, scene):
    raise NotImplementedError('Implementation removed in the public copy.')

def run_full_checks(llm, project_dir, chapter, scene):
    raise NotImplementedError('Implementation removed in the public copy.')

def reject(project_dir, chapter, scene, runs_dir, reason):
    raise NotImplementedError('Implementation removed in the public copy.')

def list_canon_items(project_dir):
    raise NotImplementedError('Implementation removed in the public copy.')

def mark_canon(project_dir, item, new_status):
    raise NotImplementedError('Implementation removed in the public copy.')

def bible_snippet(items):
    raise NotImplementedError('Implementation removed in the public copy.')

class ProjectSummary:
    pass

def project_summary(project_dir, runs_dir, daily_cap):
    raise NotImplementedError('Implementation removed in the public copy.')

def scene_manifests(project_dir, chapter, scene):
    raise NotImplementedError('Implementation removed in the public copy.')

class ChapterRow:
    pass

def chapter_rows(project_dir, runs_dir):
    raise NotImplementedError('Implementation removed in the public copy.')

def read_summary(project_dir, chapter):
    raise NotImplementedError('Implementation removed in the public copy.')

def save_summary_edit(project_dir, chapter, text):
    raise NotImplementedError('Implementation removed in the public copy.')

def estimate_summary(llm, project_dir, chapter):
    raise NotImplementedError('Implementation removed in the public copy.')

def run_summary_job(llm, project_dir, chapter):
    raise NotImplementedError('Implementation removed in the public copy.')

def list_plan_rows(project_dir, runs_dir):
    raise NotImplementedError('Implementation removed in the public copy.')

def read_plan(project_dir, plan_name):
    raise NotImplementedError('Implementation removed in the public copy.')

def save_plan_edit(project_dir, chapter, text):
    raise NotImplementedError('Implementation removed in the public copy.')

def approve_plan(project_dir, runs_dir, chapter, plan_name, note=...):
    raise NotImplementedError('Implementation removed in the public copy.')

def actionable_items(data):
    raise NotImplementedError('Implementation removed in the public copy.')

def estimate_revise(llm, project_dir, chapter, scene, numbers):
    raise NotImplementedError('Implementation removed in the public copy.')

def run_revise_job(llm, project_dir, chapter, scene, numbers):
    raise NotImplementedError('Implementation removed in the public copy.')
