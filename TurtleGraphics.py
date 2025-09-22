#TurtleGraphics.py
#Name: Beau Pick
#Date: 9/21/25
#Assignment: Turtle Graphics

import turtle #needed generally but not in CodeHS
hideturtle() #hides the default turtle in CodeHS

def drawSquare(myTurtle, size):
    for i in range(4):
        myTurtle.forward(size)
        myTurtle.right(90)

def drawPolygon (joe, sides):
    for s in range(sides):
        joe.forward(50)
        joe.right(360/sides)
    
def fillCorner(sam, corner):
    drawSquare(sam, 100)
    
    if corner == 1:
        sam.begin_fill()
        drawSquare(sam, 50)
        sam.end_fill()
        
    elif corner == 2:
            sam.forward(50)
            sam.begin_fill()
            drawSquare(sam, 50)
            sam.end_fill()
    elif corner == 3:
            sam.right(90)
            sam.forward(50)
            sam.left(90)
            sam.begin_fill()
            drawSquare(sam, 50)
            sam.end_fill()

    elif corner == 4:
            sam.right(90)
            sam.forward(100)
            sam.left(90)
            sam.forward(50)
            sam.left(90)
            sam.forward(50)
            sam.right(90)
            sam.begin_fill()
            drawSquare(sam, 50)
            sam.end_fill()
            
def squaresInSquares(sally, squares):
    sally.up()
    sally.goto(-175,175)
    sally.down()
    drawSquare(sally, 250)
    x=1
    for q in range(squares - 1):
        x += 40
        sally.up()
        sally.forward(20)
        sally.right(90)
        sally.forward(20)
        sally.left(90)
        sally.down()
        drawSquare(sally, 250-x)
        

        

   
   
 






def main():
    myTurtle = turtle.Turtle()
    
    
    #drawPolygon(myTurtle, 5) #draws a pentagon
    
    # drawPolygon(myTurtle, 8) #draws an octogon

    #fillCorner(myTurtle, 2) #draws a square with top right corner filled in.
    #fillCorner(myTurtle, 3) #draws a square bottom left corner filled in.

    squaresInSquares(myTurtle, 5) #draws 5 concentric squares
    # squaresInSquares(myTurtle, 3) #draws 3 concentric squares


main()
