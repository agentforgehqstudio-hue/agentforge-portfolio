"""Skeleton only. Implementation removed in the public copy."""

class MissingSetting(Exception):
    pass

class Deps:
    pass

def production_deps(env=...):
    raise NotImplementedError('Implementation removed in the public copy.')

def build_parser():
    raise NotImplementedError('Implementation removed in the public copy.')

def decide_real(args, env):
    raise NotImplementedError('Implementation removed in the public copy.')

class SourceStatus:
    pass

class RunReport:

    def budget_lines(self):
        raise NotImplementedError('Implementation removed in the public copy.')

    def add_market_run(self, market, tally):
        raise NotImplementedError('Implementation removed in the public copy.')

    @property
    def status_word(self):
        raise NotImplementedError('Implementation removed in the public copy.')

    def summary_pairs(self):
        raise NotImplementedError('Implementation removed in the public copy.')

    def cost_line(self):
        raise NotImplementedError('Implementation removed in the public copy.')

    def summary_text(self):
        raise NotImplementedError('Implementation removed in the public copy.')

    def lines(self):
        raise NotImplementedError('Implementation removed in the public copy.')

def format_row(headers, row):
    raise NotImplementedError('Implementation removed in the public copy.')

def run_leadgen(args, env, deps):
    raise NotImplementedError('Implementation removed in the public copy.')

def run_drafts_command(args, env, client_factory=..., ai_factory=...):
    raise NotImplementedError('Implementation removed in the public copy.')

def main(argv=..., env=..., deps=...):
    raise NotImplementedError('Implementation removed in the public copy.')
