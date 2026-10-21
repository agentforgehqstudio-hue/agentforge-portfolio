"""Skeleton only. Implementation removed in the public copy."""

class RecordNotFoundError:
    pass

class Store:

    def save(self, record):
        raise NotImplementedError('Implementation removed in the public copy.')

    def get(self, model, key):
        raise NotImplementedError('Implementation removed in the public copy.')

    def list(self, model):
        raise NotImplementedError('Implementation removed in the public copy.')
