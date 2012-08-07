#!/usr/bin/env python

try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()

from setuptools import setup, find_packages
setup(
    name = "cmdparse",
    version = "0.9",
    author = "Peter Teichman",
    license = "MIT",
    packages = find_packages(exclude=["tests"]),
    test_suite = "tests.cmdparse_suite",
)
