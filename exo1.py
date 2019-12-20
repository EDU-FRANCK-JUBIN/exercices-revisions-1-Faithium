# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 09:27:36 2019

@author: ilias
"""

def drawSapin(lines):
    currentStr = "^"
    maxLength = 1 + (2 * (lines - 1))
    toformat = "{:^"+str(maxLength)+"}"
    for i in range(0,lines):
        print(toformat.format(currentStr))
        currentStr = "^" + currentStr + "^"

print(drawSapin(12))
    