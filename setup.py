#!/usr/bin/env python

from distutils.core import setup
from setuptools import find_packages


setup\
    ( name='Zabbix battery'
    , version='1.0'
    , description='Simple JSON Server as temporary zabbix metrics storage'
    , author='Sergey Nikitin'
    , author_email='nikitinsm@gmail.com'
    , url='https://github.com/nikitinsm/zabbix-battery'
    , packages = find_packages('src')
    , package_dir = {'': 'src'}
    , include_package_data = True
    , install_requires =
      [ "tornado"
      , "tornadorpc"
      ]
    )