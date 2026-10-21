"""Skeleton only. Implementation removed in the public copy."""

def lead_tab(mode):
    raise NotImplementedError('Implementation removed in the public copy.')

def sample_tab(mode):
    raise NotImplementedError('Implementation removed in the public copy.')

class LeadRow:
    pass

class SampleRow:
    pass

class LegalFinanceRow:
    pass

def validate_lead(lead):
    raise NotImplementedError('Implementation removed in the public copy.')

def validate_sample(row):
    raise NotImplementedError('Implementation removed in the public copy.')

class RowWriter:

    def __init__(self, client, mode=..., now=...):
        raise NotImplementedError('Implementation removed in the public copy.')

    def write_leads(self, leads):
        raise NotImplementedError('Implementation removed in the public copy.')

    def write_samples(self, samples):
        raise NotImplementedError('Implementation removed in the public copy.')

    def write_legal_finance(self, items):
        raise NotImplementedError('Implementation removed in the public copy.')
