"""Skeleton only. Implementation removed in the public copy."""

class NicheStats:

    @property
    def share(self):
        raise NotImplementedError('Implementation removed in the public copy.')

    @property
    def small_rate(self):
        raise NotImplementedError('Implementation removed in the public copy.')

    @property
    def small_share_of_outliers(self):
        raise NotImplementedError('Implementation removed in the public copy.')

def measure(name, result, small_subs):
    raise NotImplementedError('Implementation removed in the public copy.')

def judge(stats, baseline, p):
    raise NotImplementedError('Implementation removed in the public copy.')

class ProbeResult:
    pass

def run_probe(settings, client, *, today=...):
    raise NotImplementedError('Implementation removed in the public copy.')

def write_report(result, path, today, p):
    raise NotImplementedError('Implementation removed in the public copy.')

def write_outputs(result, today, p, out_dir=...):
    raise NotImplementedError('Implementation removed in the public copy.')
