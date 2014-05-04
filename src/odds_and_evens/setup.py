#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
    name = "odds_and_evens",
    version = "1.0",
    url = 'http://github.com/krislion/sandbox',
    license = 'MIT',
    description = "Odds and Evens implementation in python",
    author = 'Kris Lion',
    packages = find_packages('.'),
    package_dir = {'': '.'},
    install_requires = ['setuptools'],
)


