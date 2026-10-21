"""Skeleton only. Implementation removed in the public copy."""

class SheetSchemaError(Exception):
    pass

def open_spreadsheet():
    raise NotImplementedError('Implementation removed in the public copy.')

class SheetsStore:

    def __init__(self, spreadsheet):
        raise NotImplementedError('Implementation removed in the public copy.')

    def ensure_tabs(self, models=...):
        raise NotImplementedError('Implementation removed in the public copy.')

    def save(self, record):
        raise NotImplementedError('Implementation removed in the public copy.')

    def get(self, model, key):
        raise NotImplementedError('Implementation removed in the public copy.')

    def list(self, model):
        raise NotImplementedError('Implementation removed in the public copy.')
