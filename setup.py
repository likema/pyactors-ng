# -*- coding: utf-8 -*-
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='pyactors-ng',
    version='0.1',
    packages=['geventactor'],
    url='https://github.com/likema/pyactors-ng',
    license='GPLv3',
    author='Like Ma',
    author_email='likemartinma@gmail.com',
    description='Next generation python actors.',
    platforms='any',
    install_requires=['gevent']
)
# vim: set ts=4 sw=4 sts=4 et:
