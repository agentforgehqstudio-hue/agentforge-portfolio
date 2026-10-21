"""Skeleton only. Implementation removed in the public copy."""

class LenderError(Exception):
    pass

def check_lender(lender, mode):
    raise NotImplementedError('Implementation removed in the public copy.')

def add_lender(store, raw, mode=...):
    raise NotImplementedError('Implementation removed in the public copy.')

def approval_problems(lender, mode):
    raise NotImplementedError('Implementation removed in the public copy.')

def approve_lender(store, lender, mode=..., when=...):
    raise NotImplementedError('Implementation removed in the public copy.')

def lender_match_id(deal_id, investor_id, lender_id):
    raise NotImplementedError('Implementation removed in the public copy.')

def finance_matches(store, deal, investor):
    raise NotImplementedError('Implementation removed in the public copy.')

def record_share_consent(store, lm, investor, lender, note, when=...):
    raise NotImplementedError('Implementation removed in the public copy.')

class TemplateLenderWriter:
    pass

def default_lender_writer(settings=..., logger=...):
    raise NotImplementedError('Implementation removed in the public copy.')

def draft_lender_intro(store, lm, deal, investor, lender, memo, uw, settings, writer):
    raise NotImplementedError('Implementation removed in the public copy.')

def mark_lender_intro_sent(store, intro, lm, investor, by, when=...):
    raise NotImplementedError('Implementation removed in the public copy.')
