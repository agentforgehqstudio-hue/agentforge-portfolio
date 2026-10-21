"""Skeleton only. Implementation removed in the public copy."""

class BatchStop(Exception):

    def __init__(self, reason, kind=...):
        raise NotImplementedError('Implementation removed in the public copy.')

class BatchLLM:

    def __init__(self, base, budget, daily_cap, spent_fn):
        raise NotImplementedError('Implementation removed in the public copy.')

    def gate_reason(self, est, run_cap):
        raise NotImplementedError('Implementation removed in the public copy.')

class RecordingLLM:

    def __init__(self, base):
        raise NotImplementedError('Implementation removed in the public copy.')

    @property
    def last(self):
        raise NotImplementedError('Implementation removed in the public copy.')

class SceneRecord:
    pass

class BatchResult:

    @property
    def parked(self):
        raise NotImplementedError('Implementation removed in the public copy.')

def parse_chapters(text):
    raise NotImplementedError('Implementation removed in the public copy.')

def plan_problems(project, chapter, plan_text):
    raise NotImplementedError('Implementation removed in the public copy.')

def blocking_canon(requests):
    raise NotImplementedError('Implementation removed in the public copy.')

def export_chapter(project, chapter):
    raise NotImplementedError('Implementation removed in the public copy.')

def git_commit(project_dir, message):
    raise NotImplementedError('Implementation removed in the public copy.')

def git_push(project_dir):
    raise NotImplementedError('Implementation removed in the public copy.')

class Batch:

    def __init__(self, llm, project_dir, chapters, budget, commit_fn=..., push_fn=..., log=...):
        raise NotImplementedError('Implementation removed in the public copy.')

    def spent(self):
        raise NotImplementedError('Implementation removed in the public copy.')

    def scene(self, chapter, scene):
        raise NotImplementedError('Implementation removed in the public copy.')

    def chapter(self, chapter):
        raise NotImplementedError('Implementation removed in the public copy.')

    def run(self):
        raise NotImplementedError('Implementation removed in the public copy.')

    def write_report(self):
        raise NotImplementedError('Implementation removed in the public copy.')

def run_batch(llm, project_dir, chapters, budget, **kwargs):
    raise NotImplementedError('Implementation removed in the public copy.')

class EstimateRow:

    @property
    def worst(self):
        raise NotImplementedError('Implementation removed in the public copy.')

    @property
    def expected(self):
        raise NotImplementedError('Implementation removed in the public copy.')

class BatchEstimate:

    @property
    def expected(self):
        raise NotImplementedError('Implementation removed in the public copy.')

    @property
    def worst(self):
        raise NotImplementedError('Implementation removed in the public copy.')

    @property
    def worst_with_revisions(self):
        raise NotImplementedError('Implementation removed in the public copy.')

    def lines(self, budget):
        raise NotImplementedError('Implementation removed in the public copy.')

def estimate_batch(llm, project_dir, chapters, scenes_per_chapter=...):
    raise NotImplementedError('Implementation removed in the public copy.')

def approval_phrase_ok(answer):
    raise NotImplementedError('Implementation removed in the public copy.')
