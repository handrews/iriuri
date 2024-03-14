from . import (
    rfc3986,
    rfc3987,
    rfc6874,
    rfc8141,
)

SEARCH_ORDER = (
    rfc3986,
    rfc3987,
    rfc6874,
    rfc8141,
)

def get_pattern(rule):
    for module in SEARCH_ORDER:
        try:
            return getattr(module, rule)
        except AttributeError:
            pass
    raise ValueError()
