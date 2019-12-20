# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 11:55:16 2019

@author: ilias
"""

from pyDatalog import pyDatalog
from easygui import *

pyDatalog.clear()

pyDatalog.load("""
    italian_origin(X) <= has_sauce(X)
    french_origin(X) <=  pastay(X)
    french_origin(X) <=  bread(X)
    western(X) <= french_origin(X)
    western(X) <= italian_origin(X)
    
    + pastay(croissant)
    + bread(baguette)
    + has_sauce(penne)
""")

def convertTuple(tup): 
    str =  ''.join(tup) 
    return str

title = "Restaurent western"
msg = "Que désirez vous comme aliment ?"
choices = "western", "bread", "french_origin"
choice = choicebox(msg, title, choices)
answers = pyDatalog.ask(choice+'(X)').answers
result = ""
for i in range(0,len(answers)):
    result += convertTuple(answers[i]) + " "
msgbox("Nous vous proposons les aliments suivents\n"+result, title, "OKE LOL")

#pas besoin de faire la suite de l'exercice qui est répétitif