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
              'ebp-build = jbscripts.buildjb:main',
              'ebp-watch = jbscripts.watch_build:main'
          ]
    },
    long_description="""description""")
