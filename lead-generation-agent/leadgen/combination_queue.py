"""Skeleton only. Implementation removed in the public copy."""

class QueueChanged(Exception):
    pass

def parse_date(text):
    raise NotImplementedError('Implementation removed in the public copy.')

class QueueRow:
    pass

class Queue:

    def make_row(self, mode, market, country, city, segment):
        raise NotImplementedError('Implementation removed in the public copy.')

    @classmethod
    def from_rows(cls, rows):
        raise NotImplementedError('Implementation removed in the public copy.')

    def with_last_searched(self, dates):
        raise NotImplementedError('Implementation removed in the public copy.')

    def eligible(self, mode=..., closed_markets=...):
        raise NotImplementedError('Implementation removed in the public copy.')

    def pick(self, mode=..., closed_markets=...):
        raise NotImplementedError('Implementation removed in the public copy.')

    def counts(self):
        raise NotImplementedError('Implementation removed in the public copy.')

def load_queue(client):
    raise NotImplementedError('Implementation removed in the public copy.')

def mark_searched(client, queue, row, today):
    raise NotImplementedError('Implementation removed in the public copy.')
