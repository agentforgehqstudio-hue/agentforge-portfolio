"""Skeleton only. Implementation removed in the public copy."""

class MemoSections:
    pass

class MemoWriter:
    pass

class MemoError(RuntimeError):
    pass

def facts_section(deal):
    raise NotImplementedError('Implementation removed in the public copy.')

def numbers_section(deal, uw, score):
    raise NotImplementedError('Implementation removed in the public copy.')

def screening_text(score):
    raise NotImplementedError('Implementation removed in the public copy.')

def neutral_reason(reason):
    raise NotImplementedError('Implementation removed in the public copy.')

def assumptions_section(uw):
    raise NotImplementedError('Implementation removed in the public copy.')

def context_text(deal, uw, score):
    raise NotImplementedError('Implementation removed in the public copy.')

def assemble(deal, uw, score, sections, when):
    raise NotImplementedError('Implementation removed in the public copy.')

class TemplateMemoWriter:

    def __init__(self, deal, uw, score):
        raise NotImplementedError('Implementation removed in the public copy.')

class ClaudeMemoWriter:

    def __init__(self, model, spend, estimate_usd, client=...):
        raise NotImplementedError('Implementation removed in the public copy.')

def default_memo_writer(deal, uw, score, settings=..., logger=...):
    raise NotImplementedError('Implementation removed in the public copy.')

def check_body(body, deal, uw, score, checker):
    raise NotImplementedError('Implementation removed in the public copy.')

def next_memo_version(store, deal_id):
    raise NotImplementedError('Implementation removed in the public copy.')

def write_memo(deal, uw, score, *, writer, checker=..., store=..., now=...):
    raise NotImplementedError('Implementation removed in the public copy.')

def recheck_edited(memo, body, editor, deal, uw, score, *, checker=..., store=...):
    raise NotImplementedError('Implementation removed in the public copy.')
