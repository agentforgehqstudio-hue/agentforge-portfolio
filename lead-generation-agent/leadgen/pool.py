"""Skeleton only. Implementation removed in the public copy."""

class PoolError(Exception):
    pass

def lead_id_for(phone_e164, website_url, name):
    raise NotImplementedError('Implementation removed in the public copy.')

def pool_row_from_lead(lead, today):
    raise NotImplementedError('Implementation removed in the public copy.')

def lead_from_pool_row(row):
    raise NotImplementedError('Implementation removed in the public copy.')

def candidate_from_pool_row(row):
    raise NotImplementedError('Implementation removed in the public copy.')

class Pool:

    @classmethod
    def open(cls, client, today):
        raise NotImplementedError('Implementation removed in the public copy.')

    def candidates(self, profile_id, market, segment, city):
        raise NotImplementedError('Implementation removed in the public copy.')

    def add_leads(self, leads):
        raise NotImplementedError('Implementation removed in the public copy.')

    def mark_shown(self, lead_ids, profile_id):
        raise NotImplementedError('Implementation removed in the public copy.')

def usable_for_client(row):
    raise NotImplementedError('Implementation removed in the public copy.')
