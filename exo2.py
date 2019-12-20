# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 09:44:41 2019

@author: ilias
"""

from turtle import *

drawer = Turtle()

def drawSquare(bottomLeftX, bottomLeftY, size, color):
    drawer.up()
    drawer.goto(bottomLeftX, bottomLeftY)
    drawer.down()
    drawer.color(color)
    for i in range(0,4):
        drawer.forward(size)
        drawer.left(90)
   
def drawEqTriangle(bottomLeftX, bottomLeftY, size, color):
    drawer.up()
    drawer.goto(bottomLeftX, bottomLeftY)
    drawer.down()
    drawer.color(color)
    for i in range(0,3):
        drawer.forward(size)
        drawer.left(120)
     
drawer.reset()
        
drawSquare(20, 0, 40, "red")
drawEqTriangle(0, 80, 80, "green")
drawSquare(0,0, 80, "black")

drawer.hideturtle()
        