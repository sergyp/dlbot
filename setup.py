#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

import os


setup(
    name='dlbot',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        #'virtualenv',
        'flask',
        'youtube-dl',
        #'PyYAML',
        #'click',
        #'pymongo',
        #'psutil',
        #'coloredlogs',
        #'hgapi',
        #'pillow',
        #'humanfriendly',
        #'colorama',
        #'requests',
    ],
    #entry_points='''
    #    [console_scripts]
    #    {cli_tool_name}=cli.main:main
    #'''.format(cli_tool_name=cli_tool_name),
)
