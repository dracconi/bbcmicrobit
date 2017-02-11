from microbit import *
import random

opt = [[9,9,9,9,9],[9,9,0,9,9]]

while True:
    if button_a.is_pressed():
        xy = []
        for i in range(5):
            xy.append(random.choice(opt))
        for yi, y in enumerate(xy):
            for xi, x in enumerate(y):
                display.set_pixel(xi, yi, x)
        sleep(1000)
