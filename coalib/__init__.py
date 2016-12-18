"""
The coalib package is a collection of various subpackages regarding
writing, executing and editing bears. Various other packages such as
formatting and settings are also included in coalib.
"""


import sys

from distutils.version import StrictVersion
from os.path import join, dirname


PYTHON_VERSION_34 = StrictVersion('3.4')

VERSION_FILE = join(dirname(__file__), 'VERSION')


def get_version():
    with open(VERSION_FILE, 'r') as ver:
        return ver.readline().strip()


VERSION = get_version()
__version__ = VERSION


def assert_supported_version():  # pragma: no cover
    if sys.version_info < PYTHON_VERSION_34:
        print('coala supports only python 3.4 or later.')
        exit(4)
