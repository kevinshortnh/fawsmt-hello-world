#!/usr/bin/env python
# -*- coding: utf-8 -*-


from os import getenv

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup

NAME = 'fawsmt-hello-world'
PACKAGE = 'fawsmt_hello_world'

DESCRIPTION = 'Hello World package'
AUTHOR = 'Kevin Short'
AUTHOR_EMAIL = 'kevin.short@rackspace.com'
URL = 'https://github.rackspace.com/kevi9532/fawsmt-hello-world/'

VERSION = '0.0.2'

SCRIPT = '{}={}.{}:{}'.format(NAME, PACKAGE, 'hello', 'main')

setup(
    name=NAME,
    version=VERSION,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    maintainer=AUTHOR,
    maintainer_email=AUTHOR_EMAIL,
    url=URL,
    description=DESCRIPTION,
    include_package_data=True,
    package_dir={NAME: PACKAGE},
    platforms=(
        'Linux',
        'Mac OS X',
    ),
    classifiers=(
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7'
    ),
    entry_points={
        'console_scripts': [
            SCRIPT,
        ],
    },
    packages=find_packages(),
    )
