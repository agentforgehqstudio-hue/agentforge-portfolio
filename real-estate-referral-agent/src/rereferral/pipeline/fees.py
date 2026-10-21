"""Skeleton only. Implementation removed in the public copy."""

class FeeError(Exception):
    pass

def add_fee(store, deal_id, payer, agreement_ref, model, expected):
    raise NotImplementedError('Implementation removed in the public copy.')

def record_received(store, fee, amount, when):
    raise NotImplementedError('Implementation removed in the public copy.')

def fee_summary(store):
    raise NotImplementedError('Implementation removed in the public copy.')
