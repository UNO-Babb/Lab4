#TurtleGraphics.py
#Name:EricTeko
#Date:9/22/2024
#Assignment:Turtles Graphics

import turtle 

def drawPolygon(myTurtle, size):
    for i in range(4):
        myTurtle.forward(side)
        myTurtle.right(90)
#needed generally but not in CodeHS
hideturtle() #hides the default turtle in CodeHS

def drawSquare(myTurtle, size):
    for i in range(4):
        myTurtle.forward(size)
        myTurtle.right(90)

def drawPolygon(myTurtle, num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        myTurtle.forward(50) # Adjust side length as needed
        myTurlte.right(angle)
        
def fillConner(myTurtle, corner):
    myTurtle.begin_fill()
    drawSquare(myTurtle, 50)    # Adjust square size as needed
    myTurtle.end_fill()
    
    #move to the specific conner without drawing
    if corner == 1:   # Top right
        myTurtle.penu()
        myTurtle.goto(50, 50)
        myTurtle.pendown()
    elif corner == 2:  # Bottom left
        myTurtle.penup()
        myturtle.goto(0, 0)
        myTurtle.pendown()
    # corner 4 (top left) is the default position after drawing
    
def squaresInSquares(myTurtle, num_squares):
    size = 20  #  Initial square size
    for _ in range(num_squares):
        drawSquare(myTurtle, size)
        size += 20  # Increase size for the next square
        myTurtle.penup()
        myTurtle.goto(-10, -10)  # Adjust position for centering
        myTurtle.pendown()
        
def main():
    myTurtle = turtle.Turtle()

    # Uncomment the function calls you want to see
    drawSquare(myTurtle, 100) 
    # drawPolygon(myTurtle, 5)  # Draws a pentagon
    # drawPolygon(myTurtle, 8)  # Draws an octagon
    # fillCorner(myTurtle, 2)  # Draws a square with the top right corner filled in
    # fillCorner(myTurtle, 3)  # Draws a square with the bottom left corner filled in
    # squaresInSquares(myTurtle, 5)  # Draws 5 concentric squares
    # squaresInSquares(myTurtle, 3)  # Draws 3 concentric squares   


    turtle.done()  # Keep the window open until closed manually

main()
