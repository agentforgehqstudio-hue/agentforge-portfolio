"""Skeleton only. Implementation removed in the public copy."""

def tool_for(kind):
    raise NotImplementedError('Implementation removed in the public copy.')

def prompt_kind(market, mode):
    raise NotImplementedError('Implementation removed in the public copy.')

def build_user_message(candidate_text):
    raise NotImplementedError('Implementation removed in the public copy.')

class QualifyError(Exception):
    pass

def describe_error(exc, secrets=...):
    raise NotImplementedError('Implementation removed in the public copy.')

class Qualification:
    pass

def load_system_prompt(path):
    raise NotImplementedError('Implementation removed in the public copy.')

class Qualifier:

    def __init__(self, client, model, system_prompt):
        raise NotImplementedError('Implementation removed in the public copy.')

    def qualify(self, candidate_text, kind=...):
        raise NotImplementedError('Implementation removed in the public copy.')
