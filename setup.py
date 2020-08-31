#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages;
for f in ['README.md','LICENSE']:
    try:
        nam=f[:f.index(".")];
    except:
        nam=f;
    exec(nam.lower()+"=open('"+f+"').read();");

setup(
    name='walsoc',
    version='0.7.33',
    description='walsoc - Write Any Language SOurce Code',
    long_description=readme,
    author='William Martinez Bas',
    author_email='metfar@gmail.com',
    url='https://github.com/metfar/walsoc',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

