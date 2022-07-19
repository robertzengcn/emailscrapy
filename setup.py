#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
from setuptools import setup

version = re.search(
    "^__version__\s*=\s*'(.*)'",
    open('emailscrapy/version.py').read(),
    re.M).group(1)

requirements = [r for r in open('requirements.txt', 'r').read().split('\n') if r]

# https://dustingram.com/articles/2018/03/16/markdown-descriptions-on-pypi

setup(name='Scrapyemail',
      version=version,
      description='A module to scrape email from web site',
      long_description=open('README.md').read(),
      long_description_content_type="text/markdown",
      author='Robert Zeng',
      author_email='zengjianze@gmail.com',
      py_modules=['usage'],
      packages=['Scrapyemail'],
      package_dir={'examples': 'examples'},
      install_requires=requirements
)
