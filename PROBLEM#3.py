##############################################
# Author; Keidy Lopez
# Filename: PROBLEM#3
# Description: moves circle diagnal on the screen, bounces back at corner, stops when user clickes on a key
##############################################
from graphics import *

def main():
    # set up of graphic objects
    w, h = 300, 300
    win = GraphWin('Problem 3', w, h)
    r = 20
    mycir = Circle(Point(w / 2, h / 2), r)
    mycir.setFill('blue')
    mycir.draw(win)

# waits for user to press key
    mp = win.getKey()

# directional variables
    x = 1
    y = 1

    # while loop that moves circle and stops when user presses another key
    run = True
    while run:
        if mp:
            time.sleep(.005)
            mycir.move(x, y)
            if mycir.getCenter().getX()+r >=w:
                x = x * -1
                y = y * -1
            if mycir.getCenter().getX() - r <= 0:
                x = x * -1
                y = y * -1
        stop = win.checkKey()
        if stop:
            run = False

    time.sleep(2)
    win.close()

if __name__=="__main__":
    main()