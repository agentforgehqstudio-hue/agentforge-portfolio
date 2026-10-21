"""Skeleton only. Implementation removed in the public copy."""

class ProfileError(Exception):
    pass

class Profile:

    @property
    def is_default(self):
        raise NotImplementedError('Implementation removed in the public copy.')

def load_profile_file(path, expected_id=...):
    raise NotImplementedError('Implementation removed in the public copy.')

def load_profile(profile_id, directory=...):
    raise NotImplementedError('Implementation removed in the public copy.')

def list_profiles(directory=..., errors=...):
    raise NotImplementedError('Implementation removed in the public copy.')

class StatusDecision:
    pass

def month_of(day):
    raise NotImplementedError('Implementation removed in the public copy.')

def profile_today(now, timezone):
    raise NotImplementedError('Implementation removed in the public copy.')

def check_status(profile, today):
    raise NotImplementedError('Implementation removed in the public copy.')
