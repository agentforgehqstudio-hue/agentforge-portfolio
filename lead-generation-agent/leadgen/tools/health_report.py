"""Skeleton only. Implementation removed in the public copy."""

class HealthResult:

    def add(self, level, text):
        raise NotImplementedError('Implementation removed in the public copy.')

    @property
    def fails(self):
        raise NotImplementedError('Implementation removed in the public copy.')

    @property
    def warns(self):
        raise NotImplementedError('Implementation removed in the public copy.')

    @property
    def exit_code(self):
        raise NotImplementedError('Implementation removed in the public copy.')

    def lines(self):
        raise NotImplementedError('Implementation removed in the public copy.')

def run_health(env, client_factory, now, profile=...):
    raise NotImplementedError('Implementation removed in the public copy.')
