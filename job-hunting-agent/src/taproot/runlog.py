"""Skeleton only. Implementation removed in the public copy."""

class Outcome:
    pass

class OutcomeAlreadySet(RuntimeError):
    pass

class UnknownJob:
    pass

class Summary:

    @property
    def exit_code(self):
        raise NotImplementedError('Implementation removed in the public copy.')

    def funnel_line(self):
        raise NotImplementedError('Implementation removed in the public copy.')

def load_max_error_ratio(path):
    raise NotImplementedError('Implementation removed in the public copy.')

class RunLog:

    def __init__(self, ctx, store, log_dir=..., max_error_ratio=..., env=...):
        raise NotImplementedError('Implementation removed in the public copy.')

    def event(self, name, **data):
        raise NotImplementedError('Implementation removed in the public copy.')

    def stage(self, name):
        raise NotImplementedError('Implementation removed in the public copy.')

    def received(self, job_key, source, url):
        raise NotImplementedError('Implementation removed in the public copy.')

    def outcome(self, job_key, outcome, reason, stage, cost_usd=...):
        raise NotImplementedError('Implementation removed in the public copy.')

    def stop(self, reason, event=...):
        raise NotImplementedError('Implementation removed in the public copy.')

    def check_kill(self, stage):
        raise NotImplementedError('Implementation removed in the public copy.')

    def finish(self):
        raise NotImplementedError('Implementation removed in the public copy.')
