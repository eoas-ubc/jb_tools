#!/usr/bin/env python

# Setup script for PyPI; use CMakeFile.txt to build extension modules

from setuptools import setup


setup(
    name='jbtools',
    packages=['jbscripts'],
    classifiers=[
        'License :: OSI Approved :: BSD License'
    ],
    entry_points={
          'console_scripts': [
              'buildjb = jbscripts.buildjb:main',
          ]
    },
    long_description=""" """)
