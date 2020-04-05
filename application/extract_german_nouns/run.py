import sys

from .extractor import GermanNounsExtractor

FILE = sys.argv[1]
FIRST_CHAR = ['a', 'ä']  # TODO not hard-code the first char in the runner

GermanNounsExtractor(FILE, FIRST_CHAR).extract()
