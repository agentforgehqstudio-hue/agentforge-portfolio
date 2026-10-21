"""Skeleton only. Implementation removed in the public copy."""

class LLMError(Exception):
    pass

class SpendNotApproved:
    pass

class ContextTooLarge:
    pass

class Estimate:

    def label(self):
        raise NotImplementedError('Implementation removed in the public copy.')

class LLMResult:
    pass

class LLM:

    def __init__(self, cfg, runs_dir, client=..., has_credentials=..., input_fn=..., print_fn=...):
        raise NotImplementedError('Implementation removed in the public copy.')

    def for_job(self, job):
        raise NotImplementedError('Implementation removed in the public copy.')

    @property
    def client(self):
        raise NotImplementedError('Implementation removed in the public copy.')

    def estimate(self, system, user, max_tokens=..., stable=...):
        raise NotImplementedError('Implementation removed in the public copy.')

    def run(self, job, project, system, user, spend_cap_usd, output_path=..., dry_run=..., max_tokens=..., stable=..., writer=..., run_id=..., sections=..., manifest_path=..., context_budget_tokens=...):
        raise NotImplementedError('Implementation removed in the public copy.')

    def gate_reason(self, est, run_cap):
        raise NotImplementedError('Implementation removed in the public copy.')
