import pathlib
import json
from collections import defaultdict

import yaml
import abnf
import abnf.grammars.rfc3986
import abnf.grammars.rfc3987

from tests import (
    TEST_DATA_DIR,
    URI_TESTS_OUT,
    URI_REF_TESTS_OUT,
    IRI_TESTS_OUT,
    IRI_REF_TESTS_OUT,
)

TEST_IRIS_IN = TEST_DATA_DIR / 'in.yaml'

RULES_TO_IGNORE = frozenset({
    'ALPHA',
    'DIGIT',
    'literal',
    'h16',
    'ls32',
    'dec-octet',
    'pchar',
    'pct-encoded',
    'unreserved',
    'reserved',
    'gen-delims',
    'sub-delims',
})


def node_to_dict(node, ignore=frozenset()):
    data = defaultdict(list)
    data[node.name].append(node.value)
    for child in node.children:
        if child.name not in ignore:
            for rule, value in node_to_dict(child, ignore).items():
                data[rule].extend(value)
    return data


def main():
    rule_uri = abnf.grammars.rfc3986.Rule.get('URI')
    rule_uri_ref = abnf.grammars.rfc3986.Rule.get('URI-reference')
    rule_iri = abnf.grammars.rfc3987.Rule.get('IRI')
    rule_iri_ref = abnf.grammars.rfc3987.Rule.get('IRI-reference')

    data_in = yaml.safe_load(TEST_IRIS_IN.read_text(encoding='utf-8'))
    uri_tests_out = defaultdict(dict)
    uri_ref_tests_out = defaultdict(dict)
    iri_tests_out = defaultdict(dict)
    iri_ref_tests_out = defaultdict(dict)

    ignore = frozenset() # RULES_TO_IGNORE
    for spec in data_in:
        for iri in data_in[spec]:
            if iri.isascii():
                uri_tests_out[iri] = node_to_dict(
                    rule_uri.parse_all(iri),
                    ignore,
                )
                uri_ref_tests_out[iri] = node_to_dict(
                    rule_uri_ref.parse_all(iri),
                    ignore,
                )
            iri_tests_out[iri] = node_to_dict(
                rule_iri.parse_all(iri),
                ignore,
            )
            iri_ref_tests_out[iri] = node_to_dict(
                rule_iri_ref.parse_all(iri),
                ignore,
            )
    URI_TESTS_OUT.write_text(json.dumps(uri_tests_out, indent=2), encoding='utf-8')
    URI_REF_TESTS_OUT.write_text(json.dumps(uri_ref_tests_out, indent=2), encoding='utf-8')
    IRI_TESTS_OUT.write_text(json.dumps(iri_tests_out, indent=2), encoding='utf-8')
    IRI_REF_TESTS_OUT.write_text(json.dumps(iri_ref_tests_out, indent=2), encoding='utf-8')

if __name__ == '__main__':
    main()
