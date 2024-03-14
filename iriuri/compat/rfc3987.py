import regex as re

from ..re import get_pattern

def match(string, rule='IRI_reference'):
    return re.match(get_pattern(rule,lower()), string)

def parse(string, rule='IRI_reference'):
    p = get_pattern(rule.lower())
    print(p)
    m = re.fullmatch(p, string)
    if m is None:
        raise ValueError()
    return m.capturesdict()

def compose(**parts):
    return ""

def resolve(base, uriref, strict=True, return_parts=False):
    return {} if return_parts else ""




