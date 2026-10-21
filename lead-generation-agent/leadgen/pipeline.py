"""Skeleton only. Implementation removed in the public copy."""

class RunContext:
    pass

class MarketOverride:

    @property
    def limits(self):
        raise NotImplementedError('Implementation removed in the public copy.')

    def market_reached(self, market, leads):
        raise NotImplementedError('Implementation removed in the public copy.')

    def reached(self, leads):
        raise NotImplementedError('Implementation removed in the public copy.')

    def line(self):
        raise NotImplementedError('Implementation removed in the public copy.')

    @classmethod
    def from_split(cls, text, markets, run_cap):
        raise NotImplementedError('Implementation removed in the public copy.')

class Services:
    pass

class RunStats:
    pass

class RunResult:
    pass

def round_robin(lists):
    raise NotImplementedError('Implementation removed in the public copy.')

class Pipeline:

    def __init__(self, *, settings, cfg, state, known, suppression, writer, logs, services, today, budget=..., dry_run=..., mode=..., legal_rules=..., enabled=..., override=..., require_email=...):
        raise NotImplementedError('Implementation removed in the public copy.')

    def run(self, candidates, ctx):
        raise NotImplementedError('Implementation removed in the public copy.')
