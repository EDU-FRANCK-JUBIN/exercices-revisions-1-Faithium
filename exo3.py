# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 10:05:03 2019

@author: ilias
"""
import turtle

drawer = turtle.Turtle()
drawer.speed(20)

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

def getTurtleCurrentPoint():
    return Point(drawer.xcor(), drawer.ycor())

def resetAngle():
    drawer.setheading(0)

def drawLine(point, size, leftAngle):
    drawer.up()
    drawer.goto(point.x, point.y)
    drawer.down()
    resetAngle()
    drawer.left(leftAngle)
    drawer.forward(size)
    
def drawEqTriangle(point, size, leftAngle):
    drawer.up()
    drawer.goto(point.x, point.y)
    drawer.down()
    resetAngle()
    drawer.left(leftAngle)
    for i in range(0,3):
        if i != 0:
            drawer.left(120)
        drawer.forward(size)
        
def drawSixTrangles(firstPoint, size, leftAngle):
    drawer.up()
    drawer.goto(firstPoint.x, firstPoint.y)
    resetAngle()
    drawer.left(leftAngle)
    for i in range(0,3):
        if i != 0:
            drawer.left(120)
        drawer.down()
        drawer.forward(size*2)
        drawer.up()
        drawer.left(120)
        drawer.forward(size)
    drawer.down()
    for i in range(0,6):
        drawer.left(60)
        drawer.forward(size)
    
drawer.width(3)
    
drawer.color("grey")
drawLine(Point(-200,0), 400, 0)

drawer.color("brown")
drawLine(Point(135, 0), 150, 90)
drawer.color("green")
drawSixTrangles(getTurtleCurrentPoint(), 50, 90)
drawer.color("brown")
drawLine(Point(135, 50), 30, 160)
drawer.color("green")
drawSixTrangles(getTurtleCurrentPoint(), 30, 160)
drawer.color("brown")
drawLine(Point(135, 110), 30, 160)
drawer.color("green")
drawSixTrangles(getTurtleCurrentPoint(), 30, 160)

drawer.color("blue")
drawSixTrangles(Point(-150, 210), 15, 90)
drawSixTrangles(Point(-85, 215), 15, 90)
drawSixTrangles(Point(-25, 220), 15, 90)
drawSixTrangles(Point(-125, 150), 15, 90)
drawSixTrangles(Point(-35, 160), 15, 90)

drawer.color("yellow")
drawSixTrangles(Point(-150,0), 40, 90)
drawer.color("orange")
drawLine(Point(-150, 40), 80, 60)
guidonPoint = getTurtleCurrentPoint()
sellePoint = Point(guidonPoint.x + 80, guidonPoint.y)
drawEqTriangle(sellePoint, 80, 180)
drawEqTriangle(sellePoint, 80, 240)
drawer.color("red")
drawLine(sellePoint, 35, 30)
drawLine(getTurtleCurrentPoint(), 30, 180)
drawLine(guidonPoint, 35, 30)

drawer.up()
drawer.goto(sellePoint.x, sellePoint.y)
resetAngle()
drawer.right(60)
drawer.forward(80)
centreRoux2 = getTurtleCurrentPoint()
drawer.color("yellow")
drawSixTrangles(Point(centreRoux2.x ,centreRoux2.y - 40), 40, 90)

drawer.hideturtle()
drawer.done()