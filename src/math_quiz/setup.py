#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
    name = "math_quiz",
    version = "1.0",
    url = 'http://github.com/krislion/sandbox',
    license = 'MIT',
    description = "Math quiz in python and TKinter",
    author = 'Kris Lion',
    packages = find_packages('.'),
    package_dir = {'': '.'},
    install_requires = ['setuptools'],
)


