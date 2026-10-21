"""Skeleton only. Implementation removed in the public copy."""

class SpendNotApprovedError(Exception):
    pass

class SpendTracker:

    def __init__(self, approval_threshold_usd, logger, ledger_path=...):
        raise NotImplementedError('Implementation removed in the public copy.')

    def total_usd(self):
        raise NotImplementedError('Implementation removed in the public copy.')

    def authorize(self, description, estimated_usd, approval=...):
        raise NotImplementedError('Implementation removed in the public copy.')
