"""Skeleton only. Implementation removed in the public copy."""

class Audio:
    pass

class TTSEngine:

    def synthesize(self, texts):
        raise NotImplementedError('Implementation removed in the public copy.')

class EngineRefused(RuntimeError):
    pass

class SapiEngine:

    def __init__(self, voice, rate_percent=..., run=...):
        raise NotImplementedError('Implementation removed in the public copy.')

    def synthesize(self, texts):
        raise NotImplementedError('Implementation removed in the public copy.')

class EdgeTTSEngine:

    def __init__(self, voice, rate_percent=..., allowed=..., retries=..., run_async=...):
        raise NotImplementedError('Implementation removed in the public copy.')

    def synthesize(self, texts):
        raise NotImplementedError('Implementation removed in the public copy.')

def make_engine(voice, engine=..., voice_name=..., allow_edge=...):
    raise NotImplementedError('Implementation removed in the public copy.')
