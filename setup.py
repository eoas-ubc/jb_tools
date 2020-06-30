#!/usr/bin/env python

# Setup script for PyPI; use CMakeFile.txt to build extension modules

from setuptools import setup


setup(
    name='jbtools',
    packages=['jbscripts'],
    classifiers=[
        'License :: OSI Approved :: BSD License'
    ],
    install_requires=[
        "watchdog"
    ],
    entry_points={
          'console_scripts': [
              'buildit = jbscripts.buildjb:main',
              'watchit = jbscripts.watch_build:main'
          ]
    },
    long_description="""description""")
