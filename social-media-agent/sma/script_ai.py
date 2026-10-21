"""Skeleton only. Implementation removed in the public copy."""

class ClaudeClient:
    pass

class ScriptResult:

    @property
    def word_count(self):
        raise NotImplementedError('Implementation removed in the public copy.')

    def summary(self):
        raise NotImplementedError('Implementation removed in the public copy.')

def build_request(packet, outline, b1):
    raise NotImplementedError('Implementation removed in the public copy.')

def check_script(text, packet, outline, b1):
    raise NotImplementedError('Implementation removed in the public copy.')

def write_script(packet, outline, b1, client):
    raise NotImplementedError('Implementation removed in the public copy.')

def write_script_file(result, outline, out_dir):
    raise NotImplementedError('Implementation removed in the public copy.')
