"""Skeleton only. Implementation removed in the public copy."""

def sha256_bytes(data):
    raise NotImplementedError('Implementation removed in the public copy.')

def sha256_file(path):
    raise NotImplementedError('Implementation removed in the public copy.')

def fingerprint(*parts):
    raise NotImplementedError('Implementation removed in the public copy.')

class Manifest:

    def __init__(self, path, slug=...):
        raise NotImplementedError('Implementation removed in the public copy.')

    def step_done(self, name, fp):
        raise NotImplementedError('Implementation removed in the public copy.')

    def mark_step(self, name, fp, **info):
        raise NotImplementedError('Implementation removed in the public copy.')

    def output_current(self, scene, kind, fp, path=...):
        raise NotImplementedError('Implementation removed in the public copy.')

    def entry(self, scene, kind):
        raise NotImplementedError('Implementation removed in the public copy.')

    def record_output(self, scene, kind, fp, path, **info):
        raise NotImplementedError('Implementation removed in the public copy.')

    def save(self):
        raise NotImplementedError('Implementation removed in the public copy.')
