##############################################
# Author; Keidy Lopez
# Filename: PROBLEM#4
#Description: closes window when circle is clicked
##############################################
import time

from graphics import *
import random
import math

def main():
    # set up of graphic objects
    w,h=300,300
    win = GraphWin("problem 4",w,h)
    color = (color_rgb(random.randint(0,255),random.randint(0,255),random.randint(0,255)))

    mycir = Circle(Point(w/2,h/2),20)
    mycir.setFill(color)
    mycir.draw(win)

    # waits for user to click somewhere and checks if its inside drawn circle
    mp = win.getMouse()
    if isClicked(mp,mycir):
        mycir.undraw()

    time.sleep(2)
    win.close()

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