"""Skeleton only. Implementation removed in the public copy."""

class RegistryError(Exception):
    pass

class SourceSpec:
    pass

class SourceRegistry:

    def __init__(self, specs):
        raise NotImplementedError('Implementation removed in the public copy.')

    def all_ids(self):
        raise NotImplementedError('Implementation removed in the public copy.')

    def get(self, source_id):
        raise NotImplementedError('Implementation removed in the public copy.')

    def is_enabled(self, source_id):
        raise NotImplementedError('Implementation removed in the public copy.')

    def sources_for(self, mode, market):
        raise NotImplementedError('Implementation removed in the public copy.')

def parse_registry(data):
    raise NotImplementedError('Implementation removed in the public copy.')

def load_registry(path=...):
    raise NotImplementedError('Implementation removed in the public copy.')
