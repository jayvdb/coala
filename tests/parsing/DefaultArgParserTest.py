import argparse
import re
import unittest

from coalib.collecting.Collectors import get_all_bears_names
from coalib.parsing.DefaultArgParser import (
    _autocomplete_bears_names,
    CustomFormatter,
)


class CustomFormatterTest(unittest.TestCase):

    def setUp(self):
        arg_parser = argparse.ArgumentParser(formatter_class=CustomFormatter)
        arg_parser.add_argument('-a',
                                '--all',
                                nargs='?',
                                const=True,
                                metavar='BOOL')
        arg_parser.add_argument('TARGETS',
                                nargs='*')
        self.output = arg_parser.format_help()

    def test_metavar_in_usage(self):
        match = re.search(r'usage:.+(-a \[BOOL\]).+\n\n',
                          self.output,
                          flags=re.DOTALL)
        self.assertIsNotNone(match)
        self.assertEqual(match.group(1), '-a [BOOL]')

    def test_metavar_not_in_optional_args_sections(self):
        match = re.search('optional arguments:.+(-a, --all).*',
                          self.output,
                          flags=re.DOTALL)
        self.assertIsNotNone(match)
        self.assertEqual(match.group(1), '-a, --all')

    def test_autocomplete_bear_names(self):
        self.assertEqual(
            _autocomplete_bears_names(),
            get_all_bears_names()
        )
