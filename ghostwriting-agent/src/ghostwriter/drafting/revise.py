"""Skeleton only. Implementation removed in the public copy."""

class ReviseResult:
    pass

def parse_item_numbers(text):
    raise NotImplementedError('Implementation removed in the public copy.')

def selected_items(items, numbers):
    raise NotImplementedError('Implementation removed in the public copy.')

def volatile_sections(chapter, scene, draft_text, chosen, intent, intent_file, draft_file):
    raise NotImplementedError('Implementation removed in the public copy.')

def describe_items(project_dir, chapter, scene, numbers):
    raise NotImplementedError('Implementation removed in the public copy.')

def estimate_revise(llm, project_dir, chapter, scene, numbers, prompts_dir=...):
    raise NotImplementedError('Implementation removed in the public copy.')

def changed_percent(before, after):
    raise NotImplementedError('Implementation removed in the public copy.')

def run_revise(llm, project_dir, chapter, scene, numbers, dry_run=..., prompts_dir=...):
    raise NotImplementedError('Implementation removed in the public copy.')
