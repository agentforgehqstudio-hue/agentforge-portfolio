"""Skeleton only. Implementation removed in the public copy."""

class InvalidMode(ValueError):
    pass

class LiveNotConfirmed(RuntimeError):
    pass

def resolve_mode(cli_mode=..., env=...):
    raise NotImplementedError('Implementation removed in the public copy.')

def kill_switch_reason(repo_root, env=...):
    raise NotImplementedError('Implementation removed in the public copy.')

class RunContext:
    pass

def make_context(mode, repo_root):
    raise NotImplementedError('Implementation removed in the public copy.')

def guard(ctx, action, kind, env=...):
    raise NotImplementedError('Implementation removed in the public copy.')
