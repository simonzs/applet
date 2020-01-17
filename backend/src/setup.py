#!/usr/bin/env python

# -*- coding: utf-8 -*-

import os.path

# creat zip
# os.system("bash ./pypi_bootstrap2zip.sh")

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


classifiers = """
'Development Status :: 2 - Alpha',
'Intended Audience :: Developers',
'License :: OSI Approved :: MIT License',
'Natural Language :: English',
'Programming Language :: Python :: 2',
'Programming Language :: Python :: 2.7',
'Programming Language :: Python :: 3',
'Programming Language :: Python :: 3.2',
'Programming Language :: Python :: 3.3',
'Programming Language :: Python :: 3.4',
'Programming Language :: Python :: 3.5',
"""


links = []  # for repo urls (dependency_links)
requires = []  # for package names
try:
    from pip._internal.req import parse_requirements
    from pip._internal.download import PipSession
except:
    from pip.req import parse_requirements
    from pip.download import PipSession
requirements = parse_requirements('requirements.txt', session=PipSession())
for item in requirements:
    if getattr(item, 'url', None):  # older pip has url
        links.append(str(item.url))
    if getattr(item, 'link', None):  # newer pip has link
        links.append(str(item.link))
    if item.req:
        requires.append(str(item.req))  # always the package name

tests_require = [
    'coverage',
    'flake8',
    'pydocstyle',
    'pylint',
    'pytest-pep8',
    'pytest-cov',
    # for pytest-runner to work, it is important that pytest comes last in
    # this list: https://github.com/pytest-dev/pytest-runner/issues/11
    'pytest'
]

version = '0.0.7'

setup(name='guard_backend',
      version=version,
      description='JiangXing EdgeBox Platform GUARD Backend',
      long_description=read('README.rst'),
      author='simon',
      author_email='simon@jiangxing.ai',
      url='http://gitlab.jiangxingai.com/applications/guard-rebot/guard-backend.git',
      classifiers=[c.strip() for c in classifiers.splitlines()
                   if c.strip() and not c.startswith('#')],
      packages=[
          'guard_backend',
          'guard_backend.handlers',
          'guard_backend.driver',
          'guard_backend.misc',
          'guard_backend.model',
          'guard_backend.remote',
      ],
      package_data={'guard_backend': ['*.zip']},
      test_suite='tests',
      install_requires=requires,
      dependency_links=links,
      entry_points={
          'console_scripts': ["guard_backend=guard_backend.run:main"]
      },
      setup_requires=['pytest-runner'],
      tests_require=tests_require)
