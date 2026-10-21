"""Skeleton only. Implementation removed in the public copy."""

def wait(seconds):
    raise NotImplementedError('Implementation removed in the public copy.')

class ReadOnlyError(Exception):
    pass

def open_spreadsheet(scopes, env=...):
    raise NotImplementedError('Implementation removed in the public copy.')

class GspreadReadOnlySheets:

    @classmethod
    def from_environment(cls, env=...):
        raise NotImplementedError('Implementation removed in the public copy.')

    def append_rows(self, tab, rows):
        raise NotImplementedError('Implementation removed in the public copy.')

    def update_row(self, tab, row_number, values):
        raise NotImplementedError('Implementation removed in the public copy.')

    def update_cell(self, tab, row_number, column_number, value):
        raise NotImplementedError('Implementation removed in the public copy.')

    def delete_rows(self, tab, row_numbers):
        raise NotImplementedError('Implementation removed in the public copy.')
