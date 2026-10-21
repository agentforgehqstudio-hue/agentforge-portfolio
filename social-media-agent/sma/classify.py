"""Skeleton only. Implementation removed in the public copy."""

def detect_language(title):
    raise NotImplementedError('Implementation removed in the public copy.')

class Classification:
    pass

class Classifier:

    def classify(self, title, query):
        raise NotImplementedError('Implementation removed in the public copy.')

class RuleBasedClassifier:

    def __init__(self, series_aliases, conditional_aliases=...):
        raise NotImplementedError('Implementation removed in the public copy.')

    def matches_series(self, text):
        raise NotImplementedError('Implementation removed in the public copy.')

    def classify(self, title, query=...):
        raise NotImplementedError('Implementation removed in the public copy.')
