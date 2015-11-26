#!/usr/bin/env python


#!/usr/bin/env python

import os
import sys
from setuptools import setup, find_packages


def execute_tests():
    failures = os.system('python ./nlbqx/tests.py')
    sys.exit(failures)


with open('README.rst') as file:
    long_description = file.read()

config = {
    'name' : 'Markdown-No-Lazy-BlockQuote-Extension',
    'version' : '0.1',
    'packages' : find_packages(),
    'author' : 'Alexander Todorov',
    'author_email' : 'atodorov@nospam.otb.bg',
    'license' : 'BSD',
    "description" : 'Disable lazy blockquotes for Markdown.',
    'long_description' : long_description,
    'url' : 'https://github.com/atodorov/Markdown-No-Lazy-BlockQuote-Extension',
    'classifiers' : [
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Communications :: Email :: Filters',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content :: CGI Tools/Libraries',
        'Topic :: Internet :: WWW/HTTP :: Site Management',
        'Topic :: Software Development :: Documentation',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Text Processing :: Filters',
        'Topic :: Text Processing :: Markup :: HTML',
    ],
    'install_requires' : ['Markdown'],
    'test_suite' : '__main__.execute_tests',
}

setup(**config)
