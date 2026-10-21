"""Skeleton only. Implementation removed in the public copy."""

class DryRunSheets:

    def __init__(self, inner):
        raise NotImplementedError('Implementation removed in the public copy.')

    def read_values(self, tab):
        raise NotImplementedError('Implementation removed in the public copy.')

    def read_typed(self, tab):
        raise NotImplementedError('Implementation removed in the public copy.')

    def row_count(self, tab):
        raise NotImplementedError('Implementation removed in the public copy.')

    def read_rows_from(self, tab, start_row, end_row=...):
        raise NotImplementedError('Implementation removed in the public copy.')

    def tab_titles(self):
        raise NotImplementedError('Implementation removed in the public copy.')

    def append_rows(self, tab, rows):
        raise NotImplementedError('Implementation removed in the public copy.')

    def update_row(self, tab, row_number, values):
        raise NotImplementedError('Implementation removed in the public copy.')

    def update_cell(self, tab, row_number, column_number, value):
        raise NotImplementedError('Implementation removed in the public copy.')

    def delete_rows(self, tab, row_numbers):
        raise NotImplementedError('Implementation removed in the public copy.')

    def would_write_rows(self):
        raise NotImplementedError('Implementation removed in the public copy.')

    def would_write(self):
        raise NotImplementedError('Implementation removed in the public copy.')
