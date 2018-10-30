import os
import unittest

from coalib.io.FileFactory import FileFactory


def get_path_components(filepath):
    """
    Splits the filepath into components to provide a unique
    test results that passes on all CIs.
    """
    return os.path.normpath(filepath).split(os.sep)


class FileFactoryTest(unittest.TestCase):

    def setUp(self):
        file_factory_test_dir = os.path.join(os.path.split(__file__)[0],
                                             'FileFactoryTestFiles')

        self.test_file = os.path.join(file_factory_test_dir, 'test1.txt')
        self.other_test_file = os.path.join(file_factory_test_dir, 'test2.txt')
        self.empty_file = os.path.join(file_factory_test_dir, 'empty.txt')
        self.multiline_file = os.path.join(
            file_factory_test_dir, 'multiline.txt')
        self.uut = FileFactory(self.test_file)
        self.other_file_factory = FileFactory(self.other_test_file)

    def test_equal(self):
        self.assertEqual(self.uut, FileFactory(self.test_file))
        self.assertNotEqual(self.uut, self.other_file_factory)

    def test_iter(self):
        self.assertEqual(list(self.uut), ['This is a test file.\n'])

    def test_line(self):
        self.assertEqual(self.uut.get_line(0), 'This is a test file.\n')
        with self.assertRaises(IndexError):
            self.uut.get_line(1)

    def test_deprecated_dict_getitem(self):
        self.assertEqual(self.uut[0], 'This is a test file.\n')
        with self.assertRaises(IndexError):
            self.uut[1]

    def test_lines(self):
        self.assertEqual(self.uut.lines, ('This is a test file.\n',))

    def test_lines_no_newline_mode(self):
        self.uut = FileFactory(self.test_file, newline=False)
        self.assertEqual(self.uut.lines,
                         ('This is a test file.',))

    def test_raw(self):
        self.assertEqual(self.uut.raw, b'This is a test file.')

    def test_string(self):
        self.assertEqual(self.uut.string, 'This is a test file.')

    def test_timestamp(self):
        self.assertEqual(self.uut.timestamp, os.path.getmtime(self.test_file))

    def test_name(self):
        self.assertEqual(get_path_components(self.uut.name)[-4:],
                         ['tests', 'io', 'FileFactoryTestFiles', 'test1.txt'])

    def test_empty_file(self):
        self.uut = FileFactory(self.empty_file, newline=True)
        self.assertEqual(list(self.uut), [''])
        self.uut = FileFactory(self.empty_file, newline=False)
        self.assertEqual(list(self.uut), [''])

    def test_multiline_file(self):
        self.uut = FileFactory(self.multiline_file, newline=True)
        self.assertEqual(list(self.uut), [
            'This is line 1.\n',
            'And here is line 2 without a EOL\n'
        ])
        self.uut = FileFactory(self.multiline_file, newline=False)
        self.assertEqual(list(self.uut), [
            'This is line 1.\n',
            'And here is line 2 without a EOL'
        ])
