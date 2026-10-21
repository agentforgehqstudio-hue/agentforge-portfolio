"""Skeleton only. Implementation removed in the public copy."""

def canonical_company_type(raw):
    raise NotImplementedError('Implementation removed in the public copy.')

def parse(raw):
    raise NotImplementedError('Implementation removed in the public copy.')

class CompaniesHouseError(Exception):
    pass

def http_get_json(url, params, auth):
    raise NotImplementedError('Implementation removed in the public copy.')

class CompaniesHouseClient:

    def __init__(self, api_key, get=...):
        raise NotImplementedError('Implementation removed in the public copy.')

    def search(self, sic_codes, location, size=...):
        raise NotImplementedError('Implementation removed in the public copy.')
