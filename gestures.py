from microbit import *

while True:
    gesture = accelerometer.current_gesture()
    if gesture == "face up":
        display.scoll("FACE UP")
    else:
        display.scroll("I DON'T UNDERSTAND YOU")
    display.scroll(", DUDE")
