#!/usr/bin/python

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

with open('README-pypi.rst', 'r') as inp:
  sdict = {
    'long_description' : inp.read()
  }

execfile('pycept/version.py', {}, sdict)

sdict.update({
    'name' : 'pycept',
    'description' : 'Python client for CEPT API',
    'url': 'http://github.com/rhyolight/pycept',
    'download_url' : 'https://pypi.python.org/packages/source/g/pycept/pycept-%s.tar.gz' % sdict['version'],
    'author' : 'Matthew Taylor',
    'author_email' : 'matt@numenta.org',
    'keywords' : ['sdr', 'nlp', 'cept'],
    'license' : 'MIT',
    'install_requires': [
        'requests',
        'nose'],
    'test_suite': 'tests.unit',
    'packages' : ['pycept'],
    'classifiers' : [
        'Development Status :: 1 - Planning',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python'],
})

setup(**sdict)