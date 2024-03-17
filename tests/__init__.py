import pathlib

TEST_DATA_DIR = (pathlib.Path(__file__).parent / 'data').resolve()
URI_TESTS_OUT = TEST_DATA_DIR / 'uri-tests.json'
URI_REF_TESTS_OUT = TEST_DATA_DIR / 'uri-ref-tests.json'
IRI_TESTS_OUT = TEST_DATA_DIR / 'iri-tests.json'
IRI_REF_TESTS_OUT = TEST_DATA_DIR / 'iri-ref-tests.json'
