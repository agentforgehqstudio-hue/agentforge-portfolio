"""Skeleton only. Implementation removed in the public copy."""

class IdeaSpec:

    @property
    def query(self):
        raise NotImplementedError('Implementation removed in the public copy.')

def build_specs(bends, a2_ideas, max_ideas):
    raise NotImplementedError('Implementation removed in the public copy.')

def judge(demand, small_in_top5, strong_recent, max_strong, covering_recent=..., few_recent=...):
    raise NotImplementedError('Implementation removed in the public copy.')

def check_idea(client, spec, settings, classifier, today):
    raise NotImplementedError('Implementation removed in the public copy.')

def unchecked(spec, why):
    raise NotImplementedError('Implementation removed in the public copy.')

class A4Result:
    pass

def shortlist(checks, a4):
    raise NotImplementedError('Implementation removed in the public copy.')

def run_a4(settings, client, specs, *, today=...):
    raise NotImplementedError('Implementation removed in the public copy.')

def write_outputs(result, today, out_dir=...):
    raise NotImplementedError('Implementation removed in the public copy.')

def latest_checks_json(directory=...):
    raise NotImplementedError('Implementation removed in the public copy.')

def load_checks(path):
    raise NotImplementedError('Implementation removed in the public copy.')
