"""Skeleton only. Implementation removed in the public copy."""

class StateStore:

    def get(self, key, default=...):
        raise NotImplementedError('Implementation removed in the public copy.')

    def set(self, key, value):
        raise NotImplementedError('Implementation removed in the public copy.')

    def has(self, key):
        raise NotImplementedError('Implementation removed in the public copy.')

    def delete(self, key):
        raise NotImplementedError('Implementation removed in the public copy.')

    def flush(self):
        raise NotImplementedError('Implementation removed in the public copy.')

class InMemoryState:

    def __init__(self, initial=..., updated=..., today=...):
        raise NotImplementedError('Implementation removed in the public copy.')

    def get(self, key, default=...):
        raise NotImplementedError('Implementation removed in the public copy.')

    def set(self, key, value):
        raise NotImplementedError('Implementation removed in the public copy.')

    def has(self, key):
        raise NotImplementedError('Implementation removed in the public copy.')

    def delete(self, key):
        raise NotImplementedError('Implementation removed in the public copy.')

    def flush(self):
        raise NotImplementedError('Implementation removed in the public copy.')

    def keys(self):
        raise NotImplementedError('Implementation removed in the public copy.')

    def updated_on(self, key):
        raise NotImplementedError('Implementation removed in the public copy.')

class ModeState:

    def __init__(self, inner, mode):
        raise NotImplementedError('Implementation removed in the public copy.')

    def get(self, key, default=...):
        raise NotImplementedError('Implementation removed in the public copy.')

    def set(self, key, value):
        raise NotImplementedError('Implementation removed in the public copy.')

    def has(self, key):
        raise NotImplementedError('Implementation removed in the public copy.')

    def delete(self, key):
        raise NotImplementedError('Implementation removed in the public copy.')

    def flush(self):
        raise NotImplementedError('Implementation removed in the public copy.')

    def keys(self):
        raise NotImplementedError('Implementation removed in the public copy.')

    def updated_on(self, key):
        raise NotImplementedError('Implementation removed in the public copy.')

def idem_key(kind, source, source_id):
    raise NotImplementedError('Implementation removed in the public copy.')

def maps_unverified_value(code):
    raise NotImplementedError('Implementation removed in the public copy.')

def is_stale_maps_tag(value):
    raise NotImplementedError('Implementation removed in the public copy.')

def attempts_key(kind, source, source_id):
    raise NotImplementedError('Implementation removed in the public copy.')

def name_key(name):
    raise NotImplementedError('Implementation removed in the public copy.')

def phone_key(e164):
    raise NotImplementedError('Implementation removed in the public copy.')

def domain_key(domain):
    raise NotImplementedError('Implementation removed in the public copy.')

def handle_key(handle):
    raise NotImplementedError('Implementation removed in the public copy.')

def company_key(number):
    raise NotImplementedError('Implementation removed in the public copy.')

def keeps_key(day, market):
    raise NotImplementedError('Implementation removed in the public copy.')

def review_key(day):
    raise NotImplementedError('Implementation removed in the public copy.')

def queue_searched_key(market, city, segment):
    raise NotImplementedError('Implementation removed in the public copy.')

def queue_done_key(market, city, segment):
    raise NotImplementedError('Implementation removed in the public copy.')

def maps_cache_key(name, location, market=...):
    raise NotImplementedError('Implementation removed in the public copy.')

def spend_key(day):
    raise NotImplementedError('Implementation removed in the public copy.')
