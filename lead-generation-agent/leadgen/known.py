"""Skeleton only. Implementation removed in the public copy."""

class DuplicateResult:
    pass

def is_shared_line(e164, kind=...):
    raise NotImplementedError('Implementation removed in the public copy.')

def candidate_phones(c):
    raise NotImplementedError('Implementation removed in the public copy.')

def candidate_handles(c):
    raise NotImplementedError('Implementation removed in the public copy.')

class KnownSet:

    def __init__(self):
        raise NotImplementedError('Implementation removed in the public copy.')

    def add_row(self, origin, *, name=..., phone=..., website=..., social=..., company=..., market=...):
        raise NotImplementedError('Implementation removed in the public copy.')

    def add(self, c):
        raise NotImplementedError('Implementation removed in the public copy.')

    def check(self, c, state=...):
        raise NotImplementedError('Implementation removed in the public copy.')

    def record(self, c, state):
        raise NotImplementedError('Implementation removed in the public copy.')

def load_known(client, mode=...):
    raise NotImplementedError('Implementation removed in the public copy.')

def load_suppression(client):
    raise NotImplementedError('Implementation removed in the public copy.')
