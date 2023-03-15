# -*- coding: utf-8 -*-
from setuptools import find_packages
from setuptools import setup

setup(
    name='p_suncalc',
    version='0.1.0-beta',
    packages=find_packages(),
    install_requires=[
        'pysolar @ git+ssh://git@github.com/pingswept/pysolar.git',
    ],
)
