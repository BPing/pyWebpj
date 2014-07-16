# __author__ = 'ming'
# coding=utf-8

import re

EngAndNum = re.compile('^[a-zA-Z0-9]+$')
NumOnly = re.compile('^[0-9]+$')
EngAndNumAndOt = re.compile('^[a-zA-Z0-9\?\+\^\*\(\)\[\]\.\{\}\|\+\$!@#%&~`,=/\\\]+$')

