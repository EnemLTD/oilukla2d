from oilukla.oilukla import *

import keyboard
import threading

res_x = 640
res_y = 480
title = 'Oilukla Window Render Example'
resizable = True
icon = 'sprites/hero.png'

lx = 0
ly = 0

win = oilwin(res_x, res_y, title, resizable, icon)

my_object = oilentity(icon, 80 ,80)
my_object.add_object()

def keyboardAndMovement():
    while True:
        if keyboard.is_pressed('w'):
            my_object.y -= 0.1
        elif keyboard.is_pressed('s'):
            my_object.y += 0.1
        elif keyboard.is_pressed('d'):
            my_object.x += 0.1
        elif keyboard.is_pressed('a'):
            my_object.x -= 0.1
        elif keyboard.is_pressed('escape'):
            sys.exit()

        my_object.transform()

threading.Thread(target=keyboardAndMovement).start()

win.draw_obj()
win.ena_window()

