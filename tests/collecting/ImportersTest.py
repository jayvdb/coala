import os
import unittest
from collections import OrderedDict

from importlib.machinery import (
    ModuleSpec,
    SourceFileLoader,
)
from inspect import isclass

from coalib.collecting.Importers import import_objects


class ImportObjectsTest(unittest.TestCase):

    def setUp(self):
        current_dir = os.path.split(__file__)[0]
        self.test_dir = os.path.join(current_dir, 'importers_test_dir')
        self.testfile1_path = os.path.join(self.test_dir,
                                           'file_one.py')
        self.testfile2_path = os.path.join(self.test_dir,
                                           'file_two.py')

    def test_no_file(self):
        self.assertEqual(import_objects([]), [])

    def test_no_data(self):
        obj = import_objects(self.testfile1_path)
        self.assertIsInstance(obj, list)
        self.assertEqual(len(obj), 12)

        self.assertIsInstance(obj[0], dict)
        self.assertIn('__name__', obj[0])
        self.assertEqual(obj[0]['__name__'], 'builtins')
        self.assertIn('copyright', obj[0])
        self.assertIsInstance(obj[1], str)
        self.assertTrue(obj[1].endswith('.pyc'))
        self.assertTrue(obj[1].startswith(self.test_dir))
        self.assertIsNone(obj[2])
        self.assertIsInstance(obj[3], str)
        self.assertEqual(obj[3], self.testfile1_path)
        self.assertIsInstance(obj[4], SourceFileLoader)
        self.assertIsInstance(obj[5], str)
        self.assertEqual(obj[5], 'file_one')
        self.assertIsInstance(obj[6], str)
        self.assertEqual(obj[6], '')
        self.assertIsInstance(obj[7], ModuleSpec)
        self.assertIsInstance(obj[8], list)
        self.assertEqual(obj[8], [1, 2, 3])
        self.assertIsInstance(obj[9], list)
        self.assertEqual(obj[9], [1, 2, 4])
        self.assertIsInstance(obj[10], bool)
        self.assertIs(obj[10], True)

        sub_obj = obj[11]
        self.assertTrue(isclass(sub_obj))

        self.assertEqual(sub_obj.__name__, 'test')
        self.assertEqual(sub_obj.__module__, 'file_one')

        sub_obj_instance = sub_obj()
        self.assertIsInstance(sub_obj_instance, list)

    def test_name_import(self):
        self.assertEqual(
            len(import_objects((self.testfile1_path, self.testfile2_path),
                               names='name')),
            2)
        self.assertEqual(
            len(import_objects((self.testfile1_path, self.testfile2_path),
                               names='last_name')),
            0)

    def test_type_import(self):
        objs = import_objects(self.testfile1_path, types=list, verbose=True)
        self.assertEqual(len(objs), 2)
        self.assertIsInstance(objs[0], list)
        self.assertEqual(objs[0], [1, 2, 3])
        self.assertIsInstance(objs[1], list)
        self.assertEqual(objs[1], [1, 2, 4])

        self.assertEqual(
            len(import_objects((self.testfile1_path, self.testfile2_path),
                               names='name',
                               types=OrderedDict,
                               verbose=True)),
            0)

    def test_class_import(self):
        objs = import_objects((self.testfile1_path, self.testfile2_path),
                              supers=list, verbose=True)
        self.assertEqual(len(objs), 1)

        sub_obj = objs[0]
        self.assertTrue(isclass(sub_obj))

        self.assertEqual(sub_obj.__name__, 'test')
        self.assertEqual(sub_obj.__module__, 'file_one')

        sub_obj_instance = sub_obj()
        self.assertIsInstance(sub_obj_instance, list)

        self.assertEqual(
            len(import_objects((self.testfile1_path, self.testfile2_path),
                               supers=str,
                               verbose=True)),
            0)

    def test_attribute_import(self):
        self.assertEqual(
            len(import_objects((self.testfile1_path, self.testfile2_path),
                               attributes='method',
                               local=True,
                               verbose=True)),
            1)
        self.assertEqual(
            len(import_objects((self.testfile1_path, self.testfile2_path),
                               attributes='something',
                               verbose=True)),
            0)

    def test_local_definition(self):
        self.assertEqual(
            len(import_objects((self.testfile1_path, self.testfile2_path),
                               attributes='method',
                               verbose=True)),
            2)
        self.assertEqual(
            len(import_objects((self.testfile1_path, self.testfile2_path),
                               attributes='method',
                               local=True,
                               verbose=True)),
            1)

    def test_invalid_file(self):
        with self.assertRaises(ImportError):
            import_objects('some/invalid/path',
                           attributes='method',
                           local=True,
                           verbose=True)

        with self.assertRaises(ImportError):
            import_objects('some/invalid/path',
                           attributes='method',
                           local=True,
                           verbose=False)
