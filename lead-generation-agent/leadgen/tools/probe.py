"""Skeleton only. Implementation removed in the public copy."""

class BlockResult:
    pass

def detect_block(status, headers, body):
    raise NotImplementedError('Implementation removed in the public copy.')

class Source:
    pass

class ProbeConfigError(Exception):
    pass

def load_sources(path):
    raise NotImplementedError('Implementation removed in the public copy.')

def check_sample_site(url):
    raise NotImplementedError('Implementation removed in the public copy.')

def http_get(url, headers, auth=...):
    raise NotImplementedError('Implementation removed in the public copy.')

class ProbeResult:
    pass

def count_rows(status, body):
    raise NotImplementedError('Implementation removed in the public copy.')

def probe_one(source, env, get, out_dir, sample_site=...):
    raise NotImplementedError('Implementation removed in the public copy.')

def run_probe(sources, env, get=..., out_dir=..., sample_site=..., sleep=..., gap_seconds=..., emit=...):
    raise NotImplementedError('Implementation removed in the public copy.')

def format_line(r):
    raise NotImplementedError('Implementation removed in the public copy.')

def summary_text(results):
    raise NotImplementedError('Implementation removed in the public copy.')

def write_summary(results, out_dir):
    raise NotImplementedError('Implementation removed in the public copy.')
