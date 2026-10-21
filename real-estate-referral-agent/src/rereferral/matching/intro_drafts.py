"""Skeleton only. Implementation removed in the public copy."""

class IntroError(Exception):
    pass

class IntroOpening:
    pass

class IntroWriter:
    pass

def sender(settings):
    raise NotImplementedError('Implementation removed in the public copy.')

def intro_context(deal, investor, match):
    raise NotImplementedError('Implementation removed in the public copy.')

class TemplateIntroWriter:

    def __init__(self, deal, match):
        raise NotImplementedError('Implementation removed in the public copy.')

class ClaudeIntroWriter:

    def __init__(self, model, spend, estimate_usd, client=..., prompt_path=...):
        raise NotImplementedError('Implementation removed in the public copy.')

def default_intro_writer(deal, match, settings=..., logger=...):
    raise NotImplementedError('Implementation removed in the public copy.')

def numbers_lines(deal, uw):
    raise NotImplementedError('Implementation removed in the public copy.')

def draft_intro(store, match, deal, investor, memo, uw, settings, writer, mode=...):
    raise NotImplementedError('Implementation removed in the public copy.')

def approve_intro(store, intro, when=...):
    raise NotImplementedError('Implementation removed in the public copy.')

def mark_sent(store, intro, match, investor, by, when=...):
    raise NotImplementedError('Implementation removed in the public copy.')
