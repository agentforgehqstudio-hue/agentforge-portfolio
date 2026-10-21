"""Skeleton only. Implementation removed in the public copy."""

class PipelineError(Exception):
    pass

def events_for(store, deal_id):
    raise NotImplementedError('Implementation removed in the public copy.')

def current_status(store, deal_id):
    raise NotImplementedError('Implementation removed in the public copy.')

def record_status(store, deal_id, status, note=..., when=...):
    raise NotImplementedError('Implementation removed in the public copy.')

def sync_from_records(store, when=...):
    raise NotImplementedError('Implementation removed in the public copy.')

def pipeline_table(store):
    raise NotImplementedError('Implementation removed in the public copy.')
