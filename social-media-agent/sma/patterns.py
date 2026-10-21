"""Skeleton only. Implementation removed in the public copy."""

class NoOutlierData(RuntimeError):
    pass

def latest_outlier_csv(directory=...):
    raise NotImplementedError('Implementation removed in the public copy.')

def load_outliers(path):
    raise NotImplementedError('Implementation removed in the public copy.')

def classify_rows(rows, classifier):
    raise NotImplementedError('Implementation removed in the public copy.')

class Group:
    pass

def aggregate(items, labels):
    raise NotImplementedError('Implementation removed in the public copy.')

class Gap:
    pass

def find_gaps(items, known_series, a2):
    raise NotImplementedError('Implementation removed in the public copy.')

class Idea:
    pass

def build_ideas(gaps, a2):
    raise NotImplementedError('Implementation removed in the public copy.')

class A2Result:

    @property
    def english(self):
        raise NotImplementedError('Implementation removed in the public copy.')

    @property
    def non_english(self):
        raise NotImplementedError('Implementation removed in the public copy.')

def run_a2(settings, source, classifier=...):
    raise NotImplementedError('Implementation removed in the public copy.')

def write_csv(items, path):
    raise NotImplementedError('Implementation removed in the public copy.')

def write_report(result, path, today):
    raise NotImplementedError('Implementation removed in the public copy.')

def write_outputs(result, today, out_dir=...):
    raise NotImplementedError('Implementation removed in the public copy.')
