#TurtleGraphics.py
#Name:Ryder Anderson
#Date:02/12/2025
#Assignment:Lab 3

import turtle #needed generally but not in CodeHS
hideturtle() #hides the default turtle in CodeHS
def drawSquare(myTurtle, size):
    for i in range(4):
        myTurtle.forward(size)
        myTurtle.right(90)
def drawPolygon(lebron, sides):
    for s in range(sides):
        lebron.forward(50)
        lebron.right(360/ sides)
def fillCorner(gelo, corner):
    drawSquare(gelo, 100)
    
    if corner == 1:
        gelo.begin_fill()
        drawSquare(gelo, 50)
        gelo.end_fill()
    if corner == 2:
        gelo.begin_fill()
        drawSquare(gelo, 50)
        gelo.end_fill()
def squaresInSquares(myTurtle, num):
    size = 100
    for i in range(num):
        myTurtle.penup()
        myTurtle.goto(-size / 2,size / 2)
        myTurtle.pendown()
        drawSquare(myTurtle, size)
        size -= 20
        myTurtle.penup()
        myTurtle.goto(-size / 2,size / 2)
        myTurtle.pendown()
        
    
    
    

def main():
    myTurtle = turtle.Turtle()
    
    #drawSquare(myTurtle, 100)
    
    
    # drawPolygon(myTurtle, 5) #draws a pentagon
    # drawPolygon(myTurtle, 8) #draws an octogon
    # drawPolygon(myTurtle, 3)
    # fillCorner(myTurtle, 2) #draws a square with top right corner filled in.
    # fillCorner(myTurtle, 3) #draws a square bottom left corner filled in.

    # squaresInSquares(myTurtle, 5) #draws 5 concentric squares
    # squaresInSquares(myTurtle, 3) #draws 3 concentric squares


main()
