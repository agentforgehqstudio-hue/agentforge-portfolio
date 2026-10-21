"""Skeleton only. Implementation removed in the public copy."""

class Gate:
    pass

class GateRefused:
    pass

class ApprovalStore:

    def __init__(self, root=...):
        raise NotImplementedError('Implementation removed in the public copy.')

    def path(self, gate, subject_id):
        raise NotImplementedError('Implementation removed in the public copy.')

    def record(self, gate, subject_id, approved_by, note=...):
        raise NotImplementedError('Implementation removed in the public copy.')

    def has(self, gate, subject_id):
        raise NotImplementedError('Implementation removed in the public copy.')

def spend_approved(phrase):
    raise NotImplementedError('Implementation removed in the public copy.')

def check_job_allowed(job_id, *, spend_phrase=..., paid_tier=..., publish=..., subject_id=..., approvals=...):
    raise NotImplementedError('Implementation removed in the public copy.')
