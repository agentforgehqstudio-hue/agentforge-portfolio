"""Skeleton only. Implementation removed in the public copy."""

class SheetsError(Exception):
    pass

def error_text(exc):
    raise NotImplementedError('Implementation removed in the public copy.')

class HeaderMismatch(Exception):
    pass

class SheetsClient:

    def read_values(self, tab):
        raise NotImplementedError('Implementation removed in the public copy.')

    def row_count(self, tab):
        raise NotImplementedError('Implementation removed in the public copy.')

    def read_rows_from(self, tab, start_row, end_row=...):
        raise NotImplementedError('Implementation removed in the public copy.')

    def append_rows(self, tab, rows):
        raise NotImplementedError('Implementation removed in the public copy.')

    def update_row(self, tab, row_number, values):
        raise NotImplementedError('Implementation removed in the public copy.')

    def update_cell(self, tab, row_number, column_number, value):
        raise NotImplementedError('Implementation removed in the public copy.')

    def delete_rows(self, tab, row_numbers):
        raise NotImplementedError('Implementation removed in the public copy.')

def local_now():
    raise NotImplementedError('Implementation removed in the public copy.')

def text_cell(value):
    raise NotImplementedError('Implementation removed in the public copy.')

def safe_cell(value):
    raise NotImplementedError('Implementation removed in the public copy.')

def match_headers(headers, spec):
    raise NotImplementedError('Implementation removed in the public copy.')

def find_columns(headers, spec, label=...):
    raise NotImplementedError('Implementation removed in the public copy.')

class LogEntry:
    pass

class LogWriter:

    def __init__(self, client, now=...):
        raise NotImplementedError('Implementation removed in the public copy.')

    @property
    def pending(self):
        raise NotImplementedError('Implementation removed in the public copy.')

    def add(self, entry):
        raise NotImplementedError('Implementation removed in the public copy.')

    def flush(self):
        raise NotImplementedError('Implementation removed in the public copy.')
