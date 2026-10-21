"""Skeleton only. Implementation removed in the public copy."""

class IntakeError(ValueError):
    pass

class ValidationResult:

    @property
    def ok(self):
        raise NotImplementedError('Implementation removed in the public copy.')

def validate_fields(raw, now=...):
    raise NotImplementedError('Implementation removed in the public copy.')

def new_deal_id(state=...):
    raise NotImplementedError('Implementation removed in the public copy.')

def build_deal(raw, *, entered_by, deal_id=..., listing_url=..., source_site=..., price_history=..., photos_reviewed=..., entered_at=..., extra_gaps=...):
    raise NotImplementedError('Implementation removed in the public copy.')
