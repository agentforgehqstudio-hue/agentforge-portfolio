"""Skeleton only. Implementation removed in the public copy."""

class MapsError(Exception):
    pass

class MapsPlace:
    pass

class MapsMatch:
    pass

def maps_url(cid):
    raise NotImplementedError('Implementation removed in the public copy.')

def parse_place(data):
    raise NotImplementedError('Implementation removed in the public copy.')

def is_foreign_number(phone, market=...):
    raise NotImplementedError('Implementation removed in the public copy.')

def maps_query(name, location, country=...):
    raise NotImplementedError('Implementation removed in the public copy.')

def match_place(name, place, market=..., mode=..., location=..., listing_phones=...):
    raise NotImplementedError('Implementation removed in the public copy.')

class WebsiteInfo:

    @property
    def is_own_website(self):
        raise NotImplementedError('Implementation removed in the public copy.')

    @property
    def note(self):
        raise NotImplementedError('Implementation removed in the public copy.')

def classify_website(url):
    raise NotImplementedError('Implementation removed in the public copy.')

def http_post_json(url, headers, payload, timeout=..., client=...):
    raise NotImplementedError('Implementation removed in the public copy.')

class MapsClient:

    def __init__(self, api_key, post_json=...):
        raise NotImplementedError('Implementation removed in the public copy.')

    @property
    def credits_estimate(self):
        raise NotImplementedError('Implementation removed in the public copy.')

    def search(self, q, gl):
        raise NotImplementedError('Implementation removed in the public copy.')

    def lookup(self, name, location, gl=..., country=...):
        raise NotImplementedError('Implementation removed in the public copy.')
