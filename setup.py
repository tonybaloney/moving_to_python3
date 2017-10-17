#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name='Wired Brain Coffee',
      version='1.0',
      packages=find_packages(),
      install_requires=['Flask==0.12.2', 'tinydb==3.6.0']
)
