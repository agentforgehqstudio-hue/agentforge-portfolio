"""Skeleton only. Implementation removed in the public copy."""

def load_email_config(path=...):
    raise NotImplementedError('Implementation removed in the public copy.')

def load_suppression(client):
    raise NotImplementedError('Implementation removed in the public copy.')

def template_for(segment, cfg):
    raise NotImplementedError('Implementation removed in the public copy.')

class Lead:

    def as_mapping(self):
        raise NotImplementedError('Implementation removed in the public copy.')

class Sample:
    pass

def read_leads(client):
    raise NotImplementedError('Implementation removed in the public copy.')

def read_samples(client):
    raise NotImplementedError('Implementation removed in the public copy.')

def read_drafted(client):
    raise NotImplementedError('Implementation removed in the public copy.')

def pick_leads(leads, drafted, suppression, cfg, today, since_days):
    raise NotImplementedError('Implementation removed in the public copy.')

def reply_by(today):
    raise NotImplementedError('Implementation removed in the public copy.')

def sample_lines(samples, city, n=...):
    raise NotImplementedError('Implementation removed in the public copy.')

def render(tpl, cfg, lead, angle, samples, today):
    raise NotImplementedError('Implementation removed in the public copy.')

def check_draft(subject, body, tpl, cfg):
    raise NotImplementedError('Implementation removed in the public copy.')

def clean_angle(text, cfg):
    raise NotImplementedError('Implementation removed in the public copy.')

class AngleWriter:

    def __init__(self, ai, model, get_page):
        raise NotImplementedError('Implementation removed in the public copy.')

    def fallback(self, lead, tpl):
        raise NotImplementedError('Implementation removed in the public copy.')

    def write(self, lead, tpl, cfg=...):
        raise NotImplementedError('Implementation removed in the public copy.')

class DraftsReport:

    def lines(self):
        raise NotImplementedError('Implementation removed in the public copy.')

def run_drafts(client, angle_writer, now, real, cfg=..., limit=..., since_days=...):
    raise NotImplementedError('Implementation removed in the public copy.')
