#!/usr/bin/env python
from setuptools import setup

setup(
    name="btrwin",
    version='0.1',
    py_modules=['hello'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        myhello=hello:cli
    ''',
)