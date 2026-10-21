"""Skeleton only. Implementation removed in the public copy."""

class WikiError(RuntimeError):
    pass

class WikiBlocked:
    pass

class WikiPage:
    pass

def html_to_paragraphs(markup):
    raise NotImplementedError('Implementation removed in the public copy.')

class WikiClient:

    def __init__(self, host, *, user_agent=..., cache_dir=..., cache_ttl_hours=..., delay_s=..., fetch=..., fetch_robots=..., sleep=..., clock=...):
        raise NotImplementedError('Implementation removed in the public copy.')

    def check_robots(self):
        raise NotImplementedError('Implementation removed in the public copy.')

    def search(self, query, limit=...):
        raise NotImplementedError('Implementation removed in the public copy.')

    def page(self, title):
        raise NotImplementedError('Implementation removed in the public copy.')

    def volume_ranges(self):
        raise NotImplementedError('Implementation removed in the public copy.')
