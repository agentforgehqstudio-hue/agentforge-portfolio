"""Skeleton only. Implementation removed in the public copy."""

class Line:
    pass

class Scene:

    @property
    def facts(self):
        raise NotImplementedError('Implementation removed in the public copy.')

    @property
    def words(self):
        raise NotImplementedError('Implementation removed in the public copy.')

    @property
    def paragraphs(self):
        raise NotImplementedError('Implementation removed in the public copy.')

    @property
    def narration(self):
        raise NotImplementedError('Implementation removed in the public copy.')

    def estimated_seconds(self, voice, words_per_minute=...):
        raise NotImplementedError('Implementation removed in the public copy.')

    def to_dict(self, voice, words_per_minute=...):
        raise NotImplementedError('Implementation removed in the public copy.')

class ScriptDoc:

    def scene(self, scene_id):
        raise NotImplementedError('Implementation removed in the public copy.')

    def estimated_seconds(self, voice, words_per_minute=...):
        raise NotImplementedError('Implementation removed in the public copy.')

    def speech_only_seconds(self, words_per_minute=...):
        raise NotImplementedError('Implementation removed in the public copy.')

def clean_line(raw):
    raise NotImplementedError('Implementation removed in the public copy.')

def scene_id_for(heading):
    raise NotImplementedError('Implementation removed in the public copy.')

def parse_source_key(raw):
    raise NotImplementedError('Implementation removed in the public copy.')

def slug_for(path):
    raise NotImplementedError('Implementation removed in the public copy.')

def parse_script(path):
    raise NotImplementedError('Implementation removed in the public copy.')

def write_scenes_json(doc, out_path, voice, words_per_minute=...):
    raise NotImplementedError('Implementation removed in the public copy.')
