"""Skeleton only. Implementation removed in the public copy."""

class MarketsError(Exception):
    pass

class Market:
    pass

class ExcludeRules:
    pass

class MarketsConfig:

    def in_focus(self, code, segment):
        raise NotImplementedError('Implementation removed in the public copy.')

    def market(self, code):
        raise NotImplementedError('Implementation removed in the public copy.')

    def quota_full(self, code, kept_today):
        raise NotImplementedError('Implementation removed in the public copy.')

    def all_quotas_full(self, kept_today):
        raise NotImplementedError('Implementation removed in the public copy.')

def fit_status(cfg, fit):
    raise NotImplementedError('Implementation removed in the public copy.')

def parse_markets(data):
    raise NotImplementedError('Implementation removed in the public copy.')

def load_markets(path=...):
    raise NotImplementedError('Implementation removed in the public copy.')
