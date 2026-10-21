"""Skeleton only. Implementation removed in the public copy."""

def hex_rgb(value):
    raise NotImplementedError('Implementation removed in the public copy.')

def mix(a, b, t):
    raise NotImplementedError('Implementation removed in the public copy.')

def timecode(seconds):
    raise NotImplementedError('Implementation removed in the public copy.')

class Style:

    def __init__(self, v):
        raise NotImplementedError('Implementation removed in the public copy.')

    def px(self, n):
        raise NotImplementedError('Implementation removed in the public copy.')

    def font(self, bold, size):
        raise NotImplementedError('Implementation removed in the public copy.')

def background(style, seed, crystals=...):
    raise NotImplementedError('Implementation removed in the public copy.')

def crystal(d, cx, cy, size, rng, style, alpha=...):
    raise NotImplementedError('Implementation removed in the public copy.')

def parchment(style, size, seed):
    raise NotImplementedError('Implementation removed in the public copy.')

def place_panel(img, style, box, seed):
    raise NotImplementedError('Implementation removed in the public copy.')

def wrap(draw, text, font, max_width):
    raise NotImplementedError('Implementation removed in the public copy.')

def fit_block(draw, style, text, box_w, box_h, bold, max_size, min_size=..., spacing=...):
    raise NotImplementedError('Implementation removed in the public copy.')

def draw_centered(draw, style, lines, font, cx, top, line_h, fill):
    raise NotImplementedError('Implementation removed in the public copy.')

def gem(d, cx, cy, r, style, filled, alpha=...):
    raise NotImplementedError('Implementation removed in the public copy.')

def gem_row(d, style, cx, cy, r, filled, total=...):
    raise NotImplementedError('Implementation removed in the public copy.')

def rule(d, style, cx, y, half):
    raise NotImplementedError('Implementation removed in the public copy.')

def render_title(style, title):
    raise NotImplementedError('Implementation removed in the public copy.')

def render_spoiler(style, level):
    raise NotImplementedError('Implementation removed in the public copy.')

def render_scale(style, low, high):
    raise NotImplementedError('Implementation removed in the public copy.')

def render_theory(style, number, claim):
    raise NotImplementedError('Implementation removed in the public copy.')

def render_badge(style, n):
    raise NotImplementedError('Implementation removed in the public copy.')

def render_source(style, credit, pages):
    raise NotImplementedError('Implementation removed in the public copy.')

def render_end(style, question, next_line):
    raise NotImplementedError('Implementation removed in the public copy.')

class CardSpec:
    pass

def plan_cards(doc, style):
    raise NotImplementedError('Implementation removed in the public copy.')

class CardResult:
    pass

def run_cards(doc, out_dir, settings, manifest, force=...):
    raise NotImplementedError('Implementation removed in the public copy.')

def estimated_timeline(doc, settings, words_per_minute=...):
    raise NotImplementedError('Implementation removed in the public copy.')

def load_timeline(doc, out_dir, settings):
    raise NotImplementedError('Implementation removed in the public copy.')

def match_idea(text, rules):
    raise NotImplementedError('Implementation removed in the public copy.')

def caption(terms):
    raise NotImplementedError('Implementation removed in the public copy.')

def build_shots(doc, timeline, cards, settings, out_dir):
    raise NotImplementedError('Implementation removed in the public copy.')

def write_assets_report(doc, scenes, path, estimated):
    raise NotImplementedError('Implementation removed in the public copy.')

class VisualsResult:
    pass

def run_visuals(doc, out_dir, settings, force=...):
    raise NotImplementedError('Implementation removed in the public copy.')
