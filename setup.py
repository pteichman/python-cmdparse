#!/usr/bin/env python

import sys

from setuptools import Command, find_packages, setup


class CheckCommand(Command):
    description = "Run tests."
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        import subprocess

        print "Running pep8..."
        if subprocess.call(["pep8", "cmdparse", "tests"]):
            sys.exit("ERROR: failed pep8 checks")

        print "Running pyflakes..."
        if subprocess.call(["pyflakes", "cmdparse", "tests"]):
            sys.exit("ERROR: failed pyflakes checks")

        print "Running tests..."
        if subprocess.call(["coverage", "run", "--source=cmdparse,tests",
                            "./setup.py", "test"]):
            sys.exit("ERROR: failed unit tests")

        subprocess.call(['coverage', 'report', '-m'])


setup(
    name = "cmdparse",
    version = "0.9",
    author = "Peter Teichman",
    author_email = "peter@teichman.org",
    url = "http://wiki.github.com/pteichman/python-cmdparse/",
    description = "A command line parser for CVS-style subcommands",

    packages = ["cmdparse"],
    test_suite = "tests",

    classifiers = [
        "Programming Language :: Python",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: User Interfaces"
    ],

    cmdclass = {
        "check": CheckCommand
    }
)
