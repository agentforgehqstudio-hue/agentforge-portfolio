"""Skeleton only. Implementation removed in the public copy."""

def slugify(text):
    raise NotImplementedError('Implementation removed in the public copy.')

def pluralise(trade):
    raise NotImplementedError('Implementation removed in the public copy.')

def direct_url(source, trade, location, page=...):
    raise NotImplementedError('Implementation removed in the public copy.')

def http_get_page(url, timeout=..., client=...):
    raise NotImplementedError('Implementation removed in the public copy.')

class DirectResult:

    @property
    def ok(self):
        raise NotImplementedError('Implementation removed in the public copy.')

class DirectFetcher:

    def __init__(self, get=..., sleep=..., gap_seconds=...):
        raise NotImplementedError('Implementation removed in the public copy.')

    def fetch(self, source, trade, location, page=...):
        raise NotImplementedError('Implementation removed in the public copy.')
