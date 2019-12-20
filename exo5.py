# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 12:56:39 2019

@author: ilias
"""

from pyDatalog import pyDatalog

pyDatalog.clear()

pyDatalog.create_terms()

place1(X) <= ~verte(X)