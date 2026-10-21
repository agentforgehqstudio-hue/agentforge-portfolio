"""Skeleton only. Implementation removed in the public copy."""

class Mode:
    pass

class ModeError(Exception):
    pass

class NetworkBlockedError:
    pass

def get_mode():
    raise NotImplementedError('Implementation removed in the public copy.')

def require_network(action):
    raise NotImplementedError('Implementation removed in the public copy.')

def require_live(action):
    raise NotImplementedError('Implementation removed in the public copy.')

def network_guard():
    raise NotImplementedError('Implementation removed in the public copy.')
