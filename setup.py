#!/usr/bin/env python

from setuptools import setup

setup(name='enrichment_utils',
      version='0.0.3',
      # list folders, not files
      packages=['enrichment_utils'],
      package_data={'enrichment_utils': ['data/*.csv']},
      install_requires = ['anndata', 'pandas', 'numpy==1.20.0', 'goatools==1.1.12'],
      )
