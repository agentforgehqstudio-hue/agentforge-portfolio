"""Skeleton only. Implementation removed in the public copy."""

class YouTubeError(RuntimeError):
    pass

class QuotaStop:
    pass

class QuotaTracker:

    def __init__(self, limit, cache_dir=..., now=...):
        raise NotImplementedError('Implementation removed in the public copy.')

    @property
    def path(self):
        raise NotImplementedError('Implementation removed in the public copy.')

    @property
    def used(self):
        raise NotImplementedError('Implementation removed in the public copy.')

    def check(self, cost):
        raise NotImplementedError('Implementation removed in the public copy.')

    def add(self, cost):
        raise NotImplementedError('Implementation removed in the public copy.')

class YouTubeClient:

    def __init__(self, api_key=..., *, quota, cache_dir=..., cache_ttl_hours=..., use_cache=..., fetch=...):
        raise NotImplementedError('Implementation removed in the public copy.')

    def search_page(self, query, *, order, published_after=..., max_results=...):
        raise NotImplementedError('Implementation removed in the public copy.')

    def search(self, query, *, order, published_after, max_results=...):
        raise NotImplementedError('Implementation removed in the public copy.')

    def videos(self, video_ids):
        raise NotImplementedError('Implementation removed in the public copy.')

    def channels(self, channel_ids):
        raise NotImplementedError('Implementation removed in the public copy.')

    def recent_upload_ids(self, uploads_playlist_id, max_results=...):
        raise NotImplementedError('Implementation removed in the public copy.')
