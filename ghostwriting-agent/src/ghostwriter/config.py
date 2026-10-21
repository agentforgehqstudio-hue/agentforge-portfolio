"""Skeleton only. Implementation removed in the public copy."""

class ConfigError(Exception):
    pass

def repo_root():
    raise NotImplementedError('Implementation removed in the public copy.')

def load_env(path=...):
    raise NotImplementedError('Implementation removed in the public copy.')

class ModelConfig:

    @property
    def cache_read_price(self):
        raise NotImplementedError('Implementation removed in the public copy.')

    def for_job(self, job):
        raise NotImplementedError('Implementation removed in the public copy.')

def load_model_config(path=...):
    raise NotImplementedError('Implementation removed in the public copy.')
