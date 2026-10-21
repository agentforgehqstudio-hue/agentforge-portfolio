"""Skeleton only. Implementation removed in the public copy."""

class ProfileBudget:

    def __init__(self, state, monthly_budget_usd, spent_elsewhere, overall_limit):
        raise NotImplementedError('Implementation removed in the public copy.')

    def overall_spent(self, day):
        raise NotImplementedError('Implementation removed in the public copy.')

    def overall_exceeded(self, day):
        raise NotImplementedError('Implementation removed in the public copy.')

    def own_exhausted(self, day):
        raise NotImplementedError('Implementation removed in the public copy.')

    def status(self, day):
        raise NotImplementedError('Implementation removed in the public copy.')

def spend_elsewhere(current, directory, env, client_factory, mode, day):
    raise NotImplementedError('Implementation removed in the public copy.')
