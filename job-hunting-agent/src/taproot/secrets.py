"""Skeleton only. Implementation removed in the public copy."""

class MissingSecret(RuntimeError):
    pass

class SecretStr:

    def __init__(self, value):
        raise NotImplementedError('Implementation removed in the public copy.')

    def reveal(self):
        raise NotImplementedError('Implementation removed in the public copy.')

class Secrets:

    def __init__(self, values):
        raise NotImplementedError('Implementation removed in the public copy.')

def clear_registry():
    raise NotImplementedError('Implementation removed in the public copy.')

def load_env_file(path=...):
    raise NotImplementedError('Implementation removed in the public copy.')

def load_secrets(mode, required, env=..., dotenv_path=...):
    raise NotImplementedError('Implementation removed in the public copy.')

def redact(text, secrets=...):
    raise NotImplementedError('Implementation removed in the public copy.')

class RedactingFilter:

    def filter(self, record):
        raise NotImplementedError('Implementation removed in the public copy.')

def install_log_filter(target=...):
    raise NotImplementedError('Implementation removed in the public copy.')
