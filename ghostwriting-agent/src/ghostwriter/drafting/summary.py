"""Skeleton only. Implementation removed in the public copy."""

class SummaryResult:
    pass

class ChapterStatus:

    @property
    def complete(self):
        raise NotImplementedError('Implementation removed in the public copy.')

    @property
    def can_summarise(self):
        raise NotImplementedError('Implementation removed in the public copy.')

def word_flag(count):
    raise NotImplementedError('Implementation removed in the public copy.')

def expected_scenes(project, chapter, runs_dir=...):
    raise NotImplementedError('Implementation removed in the public copy.')

def chapter_status(project, chapter, runs_dir=...):
    raise NotImplementedError('Implementation removed in the public copy.')

def volatile_sections(project, chapter):
    raise NotImplementedError('Implementation removed in the public copy.')

def next_summary_version(project, chapter):
    raise NotImplementedError('Implementation removed in the public copy.')

def run_summary(llm, project_dir, chapter, dry_run=..., prompts_dir=...):
    raise NotImplementedError('Implementation removed in the public copy.')

def estimate_summary(llm, project_dir, chapter, prompts_dir=...):
    raise NotImplementedError('Implementation removed in the public copy.')

def save_edit(project_dir, chapter, new_text):
    raise NotImplementedError('Implementation removed in the public copy.')
