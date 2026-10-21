"""Skeleton only. Implementation removed in the public copy."""

def data_dir():
    raise NotImplementedError('Implementation removed in the public copy.')

class ConfigError(Exception):
    pass

class Settings:

    def __init__(self, data, source):
        raise NotImplementedError('Implementation removed in the public copy.')

    def get(self, key):
        raise NotImplementedError('Implementation removed in the public copy.')

    def get_or(self, key, default):
        raise NotImplementedError('Implementation removed in the public copy.')

def load_settings(path=..., env_path=...):
    raise NotImplementedError('Implementation removed in the public copy.')
