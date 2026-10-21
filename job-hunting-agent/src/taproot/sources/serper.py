"""Skeleton only. Implementation removed in the public copy."""

class SourceStopped(Exception):
    pass

class Query:
    pass

class SerperSource:

    def __init__(self, ctx, budget, secrets, config, post=..., sleep=..., fixture_path=..., clock=..., env=...):
        raise NotImplementedError('Implementation removed in the public copy.')

    def build_queries(self):
        raise NotImplementedError('Implementation removed in the public copy.')

    def fetch(self):
        raise NotImplementedError('Implementation removed in the public copy.')

    def raw_search(self, query_text):
        raise NotImplementedError('Implementation removed in the public copy.')
