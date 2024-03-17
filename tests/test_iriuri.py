import sys
import json
from collections import defaultdict

import regex as re

from iriuri.re import get_pattern

from . import URI_TESTS_OUT


def perror(string):
    print(string, file=sys.stderr)


def pytest_generate_tests(metafunc):
    data = json.loads(URI_TESTS_OUT.read_text(encoding='utf-8'))
    argnames = ('iriref', 'rule', 'matches')
    argvalues = []
    testids = []
    for uri, matches in data.items():
        testids.append(f'URI -> "{uri}"')
        argvalues.append((uri, 'URI', matches))

    metafunc.parametrize(argnames, argvalues, ids=testids)


def test_iriref_parsing(iriref, rule, matches):
    m = re.fullmatch(get_pattern(rule.lower().replace('-', '_')), iriref)
    assert m is not None
