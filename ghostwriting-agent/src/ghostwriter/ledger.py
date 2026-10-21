"""Skeleton only. Implementation removed in the public copy."""

class LedgerError(Exception):
    pass

class Op:
    pass

def parse_ops(data):
    raise NotImplementedError('Implementation removed in the public copy.')

def dump_ops(ops):
    raise NotImplementedError('Implementation removed in the public copy.')

def load_ops(path):
    raise NotImplementedError('Implementation removed in the public copy.')

class ApplyResult:
    pass

def apply_ops(ledger_text, ops, tag):
    raise NotImplementedError('Implementation removed in the public copy.')

def phrase_counter_op(ledger_text, counts):
    raise NotImplementedError('Implementation removed in the public copy.')

class Hook:

    @property
    def payoff_chapter(self):
        raise NotImplementedError('Implementation removed in the public copy.')

    @property
    def is_open(self):
        raise NotImplementedError('Implementation removed in the public copy.')

def has_hooks_section(ledger_text):
    raise NotImplementedError('Implementation removed in the public copy.')

def parse_hooks(ledger_text):
    raise NotImplementedError('Implementation removed in the public copy.')

def overdue_hooks(hooks, chapter):
    raise NotImplementedError('Implementation removed in the public copy.')

def snapshots_dir(project_dir):
    raise NotImplementedError('Implementation removed in the public copy.')

def ensure_baseline(project_dir):
    raise NotImplementedError('Implementation removed in the public copy.')

def snapshot_before(project_dir, tag):
    raise NotImplementedError('Implementation removed in the public copy.')

class Snapshot:
    pass

def list_snapshots(project_dir):
    raise NotImplementedError('Implementation removed in the public copy.')

class RollbackResult:
    pass

def rollback(project_dir, label, runs_dir, phrase):
    raise NotImplementedError('Implementation removed in the public copy.')
