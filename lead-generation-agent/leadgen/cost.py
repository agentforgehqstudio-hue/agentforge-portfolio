"""Skeleton only. Implementation removed in the public copy."""

def estimate_claude_usd(model, input_tokens, output_tokens):
    raise NotImplementedError('Implementation removed in the public copy.')

def estimate_serper_usd(maps_calls):
    raise NotImplementedError('Implementation removed in the public copy.')

class RunCost:

    def add_claude(self, input_tokens, output_tokens):
        raise NotImplementedError('Implementation removed in the public copy.')

    def add_maps(self, calls=...):
        raise NotImplementedError('Implementation removed in the public copy.')

    def add_make_request(self):
        raise NotImplementedError('Implementation removed in the public copy.')

    @property
    def claude_usd(self):
        raise NotImplementedError('Implementation removed in the public copy.')

    @property
    def serper_usd(self):
        raise NotImplementedError('Implementation removed in the public copy.')

    @property
    def estimated_usd(self):
        raise NotImplementedError('Implementation removed in the public copy.')

    @property
    def make_credits_estimate(self):
        raise NotImplementedError('Implementation removed in the public copy.')

    def cost_per_lead(self, leads):
        raise NotImplementedError('Implementation removed in the public copy.')

class BudgetGuard:

    def __init__(self, state, monthly_budget_usd):
        raise NotImplementedError('Implementation removed in the public copy.')

    def spent(self, day):
        raise NotImplementedError('Implementation removed in the public copy.')

    @property
    def limit(self):
        raise NotImplementedError('Implementation removed in the public copy.')

    def fraction(self, day):
        raise NotImplementedError('Implementation removed in the public copy.')

    def record(self, day, usd):
        raise NotImplementedError('Implementation removed in the public copy.')

    def status(self, day):
        raise NotImplementedError('Implementation removed in the public copy.')

    def exhausted(self, day):
        raise NotImplementedError('Implementation removed in the public copy.')
