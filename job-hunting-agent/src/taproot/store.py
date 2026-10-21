"""Skeleton only. Implementation removed in the public copy."""

class Claim:
    pass

def load_dedupe_window_days(path):
    raise NotImplementedError('Implementation removed in the public copy.')

class Store:

    def __init__(self, path=..., dedupe_window_days=..., clock=...):
        raise NotImplementedError('Implementation removed in the public copy.')

    @property
    def conn(self):
        raise NotImplementedError('Implementation removed in the public copy.')

    def close(self):
        raise NotImplementedError('Implementation removed in the public copy.')

    def get(self, job_key):
        raise NotImplementedError('Implementation removed in the public copy.')

    def claim(self, job):
        raise NotImplementedError('Implementation removed in the public copy.')

    def claim_with_key(self, job):
        raise NotImplementedError('Implementation removed in the public copy.')

    def peek(self, job):
        raise NotImplementedError('Implementation removed in the public copy.')

    def complete(self, job_key, outcome):
        raise NotImplementedError('Implementation removed in the public copy.')

    def fail(self, job_key, error):
        raise NotImplementedError('Implementation removed in the public copy.')
