"""Skeleton only. Implementation removed in the public copy."""

class BudgetNotConfigured(RuntimeError):
    pass

class BudgetExceeded(RuntimeError):

    def __init__(self, kind, limit, unit=...):
        raise NotImplementedError('Implementation removed in the public copy.')

def load_budget_config(path):
    raise NotImplementedError('Implementation removed in the public copy.')

class Budget:

    def __init__(self, ctx, store, config, clock=..., env=...):
        raise NotImplementedError('Implementation removed in the public copy.')

    @property
    def caps(self):
        raise NotImplementedError('Implementation removed in the public copy.')

    def today_usd(self):
        raise NotImplementedError('Implementation removed in the public copy.')

    def month_to_date_usd(self):
        raise NotImplementedError('Implementation removed in the public copy.')

    def allow_job(self):
        raise NotImplementedError('Implementation removed in the public copy.')

    def job_cap_reason(self):
        raise NotImplementedError('Implementation removed in the public copy.')

    def reserve_llm(self, model, est_input_tokens, max_output_tokens):
        raise NotImplementedError('Implementation removed in the public copy.')

    def reserve_serper(self, queries=...):
        raise NotImplementedError('Implementation removed in the public copy.')

    def record_llm(self, model, usage):
        raise NotImplementedError('Implementation removed in the public copy.')

    def record_serper(self, queries=...):
        raise NotImplementedError('Implementation removed in the public copy.')
