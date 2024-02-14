##############################################
# Author; Keidy Lopez
# Filename: PROBLEM#5
# Description: moves circle diagnal on the screen,bounces back at corner, stops when user  clickes on circle
##############################################
from graphics import *
import math

def main():
    # set up of graphic objects
    w, h = 300, 300
    win = GraphWin('Problem 5', w, h)
    r = 20
    mycir = Circle(Point(w / 2, h / 2), r)
    mycir.setFill('blue')
    mycir.draw(win)

    message = Text(Point(w/2,h-40),'Click the circle')
    message.setSize(10)
    message.draw(win)

# waits for user to click somewhere
    mp = win.getMouse()

# directional variables
    x = 1
    y = 1
# while loop that moves circle until the user clicks on said circle
    run = True
    while run:
        if mp:
            time.sleep(.005)
            mycir.move(x, y)
            if mycir.getCenter().getX() + r >= w:
                x = x * -1
                y = y * -1
            if mycir.getCenter().getX() - r <= 0:
                x = x * -1
                y = y * -1
        stop = win.checkMouse()
        if stop and isClicked(stop,mycir):
            mycir.undraw()
            message.setText('You got it!')
            run = False

    time.sleep(2)
    win.close()


# checks is a point object is inside a circle object
def isClicked(p1: Point, myCirc: Circle) -> bool:
    r = myCirc.getRadius()
    p2 = myCirc.getCenter()

    x_p1 = p1.getX()
    y_p1 = p1.getY()
    x_p2 = p2.getX()
    y_p2 = p2.getY()

    if math.sqrt((x_p2 - x_p1)** 2 + (y_p2 - y_p1) ** 2) <= r:
        return True
    else:
        return False




if __name__=="__main__":
    main()