##############################################
# Author; Keidy Lopez
# Filename: PROBLEM#2
# Description: moves circle diagnal on the screen and stops at corner
##############################################
from graphics import *
import time

def main():
    # set up of graphic objects
    w, h = 300, 300
    win = GraphWin('Problem 2', w, h)
    r = 20
    mycir = Circle(Point(w / 2, h / 2), r)
    mycir.setFill('blue')
    mycir.draw(win)

# waits for user to press a key
    mp = win.getKey()

    # moves circle diagonal down the screen and stops at corner
    if mp:
        for i in range(w // 2 - r):
            time.sleep(.025)
            mycir.move(1, 1)

    time.sleep(2)
    win.close()


if __name__=="__main__":
    main()