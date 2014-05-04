#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
    name = "tictactoe",
    version = "1.0",
    url = 'http://github.com/krislion/sandbox',
    license = 'MIT',
    description = "Tic-Tac-Toe implementation in python",
    author = 'Kris Lion',
    packages = find_packages('src'),
    package_dir = {'': 'src'},
    install_requires = ['setuptools'],
)

