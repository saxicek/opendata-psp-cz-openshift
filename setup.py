#!/usr/bin/env python
# coding=utf-8
from setuptools import setup

setup(
    name='OpendataPspCz',
    version='1.0',
    description='Opendata psp.cz OpenShift App',
    author='Libor Nenadál',
    author_email='libor.nenadal@gmail.com',
    url='http://pspcz-opendata.rhcloud.com/',
    install_requires=['Django>=1.3',
                      'djangorestframework',
                      'pytz'
    ],
)
