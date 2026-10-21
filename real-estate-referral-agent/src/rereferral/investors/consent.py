"""Skeleton only. Implementation removed in the public copy."""

class ConsentError(Exception):
    pass

def log_consent(store, person_id, source, note=..., when=...):
    raise NotImplementedError('Implementation removed in the public copy.')

def log_contact(store, investor, note, when=...):
    raise NotImplementedError('Implementation removed in the public copy.')

def opt_out(store, investor, note=..., when=...):
    raise NotImplementedError('Implementation removed in the public copy.')

def renew_consent(store, investor, source, consent_date, note=..., when=...):
    raise NotImplementedError('Implementation removed in the public copy.')

def contact_log(store, person_id):
    raise NotImplementedError('Implementation removed in the public copy.')
