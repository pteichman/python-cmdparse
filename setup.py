#!/usr/bin/env python

from ez_setup import use_setuptools
use_setuptools()

from setuptools import setup, find_packages
setup(
    name = "cmdparse",
    version = "0.9",
    author = "Peter Teichman",
    license = "MIT",
    package_data = {'':['*.*']},
    packages = find_packages(),
)
