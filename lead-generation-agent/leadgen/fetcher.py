"""Skeleton only. Implementation removed in the public copy."""

def http_post(url, payload, client=..., timeout=...):
    raise NotImplementedError('Implementation removed in the public copy.')

class SourceHealth:
    pass

class FetchResult:
    pass

class MakeFetcher:

    def __init__(self, client, state, webhook_url, post=..., sleep=..., monotonic=..., uuid_factory=..., timeout_seconds=..., poll_seconds=...):
        raise NotImplementedError('Implementation removed in the public copy.')

    def fetch(self, trade, location, sources, pages=...):
        raise NotImplementedError('Implementation removed in the public copy.')
