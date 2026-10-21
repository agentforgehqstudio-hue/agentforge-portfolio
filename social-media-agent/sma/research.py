"""Skeleton only. Implementation removed in the public copy."""

def slugify(text):
    raise NotImplementedError('Implementation removed in the public copy.')

class IdeaNotFound(ValueError):
    pass

def resolve_idea(checks, query, shortlist_size=...):
    raise NotImplementedError('Implementation removed in the public copy.')

def spoiler_rank(label):
    raise NotImplementedError('Implementation removed in the public copy.')

def has_unanchored_pronoun(sentence, subject_page=...):
    raise NotImplementedError('Implementation removed in the public copy.')

def is_note_not_sentence(sentence):
    raise NotImplementedError('Implementation removed in the public copy.')

def has_unbalanced_quote(sentence):
    raise NotImplementedError('Implementation removed in the public copy.')

def looks_like_sentence(sentence):
    raise NotImplementedError('Implementation removed in the public copy.')

def split_sentences(paragraph):
    raise NotImplementedError('Implementation removed in the public copy.')

def chapters_in(text):
    raise NotImplementedError('Implementation removed in the public copy.')

def volume_for(chapter, ranges):
    raise NotImplementedError('Implementation removed in the public copy.')

def spoiler_label(sentence, paragraph, page, wcfg, ranges):
    raise NotImplementedError('Implementation removed in the public copy.')

def keywords_for(title, series, settings):
    raise NotImplementedError('Implementation removed in the public copy.')

def core_groups(title, series, settings, wcfg):
    raise NotImplementedError('Implementation removed in the public copy.')

def core_terms(title, series, settings, wcfg):
    raise NotImplementedError('Implementation removed in the public copy.')

def wide_groups(series, settings):
    raise NotImplementedError('Implementation removed in the public copy.')

def core_entities(lower, core):
    raise NotImplementedError('Implementation removed in the public copy.')

def candidates_from(page, keywords, wcfg, ranges, max_words, min_words, core=..., skip_sections=..., skip_words=..., min_entities=..., subject_page=..., wide=...):
    raise NotImplementedError('Implementation removed in the public copy.')

def source_url(page, section):
    raise NotImplementedError('Implementation removed in the public copy.')

def extract_facts(pages, keywords, wcfg, ranges, settings, core=..., wide=...):
    raise NotImplementedError('Implementation removed in the public copy.')

def is_hedged(fact):
    raise NotImplementedError('Implementation removed in the public copy.')

def pick_pages(wiki, wcfg, series, fmt, extra_terms, settings):
    raise NotImplementedError('Implementation removed in the public copy.')

def build_packet(check, title, slug, wiki, wcfg, settings, extra_terms=..., today=...):
    raise NotImplementedError('Implementation removed in the public copy.')

def coverage_notes(titles):
    raise NotImplementedError('Implementation removed in the public copy.')

def render_packet(packet):
    raise NotImplementedError('Implementation removed in the public copy.')

def write_packet(packet, out_dir=...):
    raise NotImplementedError('Implementation removed in the public copy.')

def load_packet(path):
    raise NotImplementedError('Implementation removed in the public copy.')
