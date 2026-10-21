"""Skeleton only. Implementation removed in the public copy."""

class ExtractedField:
    pass

class ExtractedPriceEvent:
    pass

class ListingExtraction:
    pass

def normalise(text):
    raise NotImplementedError('Implementation removed in the public copy.')

def numbers_in(text):
    raise NotImplementedError('Implementation removed in the public copy.')

def check_field(name, value, quote, text_norm):
    raise NotImplementedError('Implementation removed in the public copy.')

def check_price_event(event, text_norm):
    raise NotImplementedError('Implementation removed in the public copy.')

class Rejection:
    pass

class ParsedListing:

    @property
    def gaps(self):
        raise NotImplementedError('Implementation removed in the public copy.')

def verify_extraction(extraction, text, source):
    raise NotImplementedError('Implementation removed in the public copy.')

class ExtractionError(RuntimeError):
    pass

class Extractor:
    pass

def text_key(text):
    raise NotImplementedError('Implementation removed in the public copy.')

class FixtureExtractor:

    def __init__(self, recordings_dir=...):
        raise NotImplementedError('Implementation removed in the public copy.')

class ClaudeExtractor:

    def __init__(self, model, spend, estimate_usd, client=...):
        raise NotImplementedError('Implementation removed in the public copy.')

def default_extractor(settings=..., logger=...):
    raise NotImplementedError('Implementation removed in the public copy.')

def parse_listing(text, extractor=..., logger=..., cache_dir=...):
    raise NotImplementedError('Implementation removed in the public copy.')
