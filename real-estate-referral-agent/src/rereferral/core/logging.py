"""Skeleton only. Implementation removed in the public copy."""

class JobLogger:

    def __init__(self, path=...):
        raise NotImplementedError('Implementation removed in the public copy.')

    def start(self, job, input_hash, **extra):
        raise NotImplementedError('Implementation removed in the public copy.')

    def finish(self, job, run_id, input_hash, output_ref=..., **extra):
        raise NotImplementedError('Implementation removed in the public copy.')

    def error(self, job, run_id, input_hash, error, **extra):
        raise NotImplementedError('Implementation removed in the public copy.')

    def event(self, event, **fields):
        raise NotImplementedError('Implementation removed in the public copy.')

    def entries(self):
        raise NotImplementedError('Implementation removed in the public copy.')
