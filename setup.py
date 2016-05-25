#!/usr/bin/env python


from codecs import open
from os import path
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand
import sys


class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = ['test_safeint.py']
        self.test_suite = True

    def run_tests(self):
        # import here, because outside the eggs aren't loaded
        import pytest
        errno = pytest.main(self.test_args)
        sys.exit(errno)


here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='safeint',
    version='0.0.3',
    description='Create an integer within a range.',
    long_description=long_description,
    url='https://github.com/pelotoncycle/safeint',
    author='Dan Sokolsky',
    author_email='dan@pelotoncycle.com',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
    ],
    keywords='int development security',
    py_modules=['safeint'],
    install_requires=['six'],
    extras_require={
        'dev': ['check-manifest'],
        'test': ['coverage', 'pytest', 'pytest-cov', 'flake8'],
    },
    cmdclass={'test': PyTest},
)
