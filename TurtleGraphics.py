#TurtleGraphics.py
#Name:Cooper Kinnan
#Date:2/15/2025
#Assignment:Lab 4

import turtle #needed generally but not in CodeHS


def drawSquare(myTurtle, size):
    for i in range(4):
        myTurtle.forward(size)
        myTurtle.right(90)

def drawPolygon(bob, sides):
    for s in range(sides):
        bob.forward(100)
        bob.right(360/sides)

def fillCorner(bill, corner):
    drawSquare(bill, 100)
    if corner == 1:
        bill.begin_fill()
        drawSquare(bill, 50)
        bill.end_fill()
    elif corner == 2:
        bill.forward(50)
        bill.begin_fill()
        drawSquare(bill, 50)
        bill.end_fill()
    elif corner == 3:
        bill.forward(50)
        bill.penup()
        bill.right(90)
        bill.forward(50)
        bill.pendown()
        bill.begin_fill()
        drawSquare(bill,50)
        bill.end_fill()
    elif corner == 4:
        bill.forward(100)
        bill.right(90)
        bill.forward(50)
        bill.begin_fill()
        drawSquare(bill,50)
        bill.end_fill()
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
    #drawPolygon(myTurtle, 5) #draws a pentagon
    #drawPolygon(myTurtle, 8)
   
    #fillCorner(myTurtle, 2) #draws a square with top right corner filled in.

    #fillCorner(myTurtle, 3) #draws a square bottom left corner filled in.



    # squaresInSquares(myTurtle, 5) #draws 5 concentric squares

    # squaresInSquares(myTurtle, 3) #draws 3 concentric squares


main()
