#!/usr/bin/env python

from ez_setup import use_setuptools
use_setuptools()

from setuptools import setup, find_packages
setup(
    name = "cmdparse",
    version = "0.9",
    author = "Peter Teichman",
    author_email = "peter@teichman.org",
    url = "http://wiki.github.com/pteichman/python-cmdparse/",
    description = "A command line parser for CVS-style subcommands",
    packages = ["cmdparse"],
    test_suite = "tests.cmdparse_suite",
    classifiers = [
        "Programming Language :: Python",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: User Interfaces"
    ]
)
