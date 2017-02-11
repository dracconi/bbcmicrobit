from microbit import *

xy = [[9,9,9,9,9],[0,0,0,0,0],[9,3,9,3,9],[9,9,9,9,9],[1,1,1,1,1]]

for yi, y in enumerate(xy):
    for xi, x in enumerate(y):
        #print "x:"+str(x)
        #print "y:"+str(y)

        display.set_pixel(xi,yi,x)
