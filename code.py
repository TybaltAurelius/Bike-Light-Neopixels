# CircuitPython code for bike light with turn signal and stoplight functions #
# Left and right signals are triggered with buttons #
# Stoplight is triggered with hall sensor #

import time
import board
import neopixel
from digitalio import DigitalInOut, Direction, Pull

numpix = 38

leftturnpix = (37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26)  # Left-hand pixels
rightturnpix = (14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25)  # Right-hand pixels

strip = neopixel.NeoPixel(board.GP0, numpix, brightness=1, auto_write=False)

leftjewel = (0, 1, 2, 3, 4, 5, 6)
rightjewel = (7, 8, 9, 10, 11, 12, 13)

color_left = (0, 50, 0)  # Green
color_right = (0, 0, 50)  # Blue
color_stop = (50, 0, 0)  # Red
color_off = (0, 0, 0)

btnL = DigitalInOut(board.GP2)
btnL.direction = Direction.INPUT
btnL.pull = Pull.UP

btnR = DigitalInOut(board.GP4)
btnR.direction = Direction.INPUT
btnR.pull = Pull.UP

btnSTOP = DigitalInOut(board.GP6)
btnSTOP.direction = Direction.INPUT
btnSTOP.pull = Pull.UP

prev_stateSTOP = btnSTOP.value

leftturnstate = 0


def scroll(turnsignal, color, speed):
    for i in turnsignal:
        strip[i] = color
        strip.show()
        time.sleep(speed)
        if i == turnsignal[11]:
            strip[i] = color
            strip.show()
            time.sleep(0.1)
            strip.fill(color_off)
            strip.show()


while True:
    while not btnL.value:
        for i in leftjewel:
            strip[i] = color_left
            strip.show()
        scroll(leftturnpix, color_left, 0.03)
        print("BTNL is down")

    while not btnR.value:
        for i in rightjewel:
            strip[i] = color_right
            strip.show()
        scroll(rightturnpix, color_right, 0.03)
        print("BTNR is down")

    cur_stateSTOP = btnSTOP.value
    if cur_stateSTOP != prev_stateSTOP:
        if not cur_stateSTOP:
            strip.fill(color_stop)
            strip.show()
            print("STOP is down")
        else:
            strip.fill(color_off)
            strip.show()
            print("STOP is up")

    prev_stateSTOP = cur_stateSTOP
