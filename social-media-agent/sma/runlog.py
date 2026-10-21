"""Skeleton only. Implementation removed in the public copy."""

class Status:
    pass

class RunLog:

    def __init__(self, run_date=..., runs_dir=...):
        raise NotImplementedError('Implementation removed in the public copy.')

    def path(self, job_id):
        raise NotImplementedError('Implementation removed in the public copy.')

    def read(self, job_id):
        raise NotImplementedError('Implementation removed in the public copy.')

    def start(self, job_id):
        raise NotImplementedError('Implementation removed in the public copy.')

    def finish(self, job_id, output):
        raise NotImplementedError('Implementation removed in the public copy.')

    def fail(self, job_id, error):
        raise NotImplementedError('Implementation removed in the public copy.')

    def is_finished(self, job_id):
        raise NotImplementedError('Implementation removed in the public copy.')

    def resume_from(self, sequence):
        raise NotImplementedError('Implementation removed in the public copy.')
