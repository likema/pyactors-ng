# -*- coding: utf-8 -*-
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

packages = ['geventactor', 'processactor', 'threadactor', 'zmqactor',
            'actorfactory']

if sys.version_info >= (3, 5):
    packages.append('asyncactor')

setup(
    name='pyactors-ng',
    version='0.5',
    packages=packages,
    url='https://github.com/likema/pyactors-ng',
    license='GPLv3',
    author='Like Ma',
    author_email='likemartinma@gmail.com',
    description=(
        'Next generation python actors with gevent, async, process and '
        'zeromq implementations'),
    platforms='any',
    install_requires=[
        'gevent',
        'message>=0.2.2',
        'pyzmq>=2.2.0.1'
    ],
    dependency_links=[
        ('https://github.com/likema/python-message/archive/master.zip'
         '#egg=message-0.2.2')
    ],
    classifiers=[
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)'
    ]
)
# vim: set ts=4 sw=4 sts=4 et:
