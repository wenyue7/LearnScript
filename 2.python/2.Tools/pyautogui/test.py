#!/bin/python3
#########################################################################
# File Name: test.py
# Author: LiHongjin
# mail: 872648180@qq.com
# Created Time: Tue Sep 12 09:49:49 2023
#########################################################################

# references:
# https://pyautogui.readthedocs.io/en/latest/
# https://stackoverflow.com/questions/76361049/how-to-fix-typeerror-not-supported-between-instances-of-str-and-int-wh

try:
    import pyautogui
    import time
except Exception as err_info:
    print(err_info)
    exit(0)

print("==> screen size")
time.sleep(1)
# Get the size of the primary monitor.
screenWidth, screenHeight = pyautogui.size()
print(screenWidth, screenHeight)
time.sleep(1)
print()

print("==> cur mouse loc")
time.sleep(1)
# Get the XY position of the mouse.
currentMouseX, currentMouseY = pyautogui.position()
print("mouse loc", currentMouseX, currentMouseY)
time.sleep(1)
print()

print("==> move mouse to 100,150")
time.sleep(1)
# Move the mouse to XY coordinates.
pyautogui.moveTo(100, 150)
time.sleep(1)
print()

print("==> move to 100,200 and click button")
time.sleep(1)
print("move mouse to 100,200")
# Click the mouse.
pyautogui.click()
# Move the mouse to XY coordinates and click it.
pyautogui.click(100, 200)
# Find where button.png appears on the screen and click it.
try:
    pyautogui.click('button.png')
except Exception as err_info:
    print("errinfo:")
    print(err_info)
    print("maybe connot find button")
time.sleep(1)
pyautogui.press('esc')
time.sleep(1)
print()

print("==> move to 200,400 and click, then move to 500,500")
time.sleep(1)
# Move the mouse 400 pixels to the right of its current position.
pyautogui.move(200, 400)
# Double click the mouse.
# pyautogui.doubleClick()
pyautogui.click()
# Use tweening/easing function to move mouse over 2 seconds.
pyautogui.moveTo(500, 500, duration=2, tween=pyautogui.easeInOutQuad)
time.sleep(1)
print()

print("==> write hello world!")
time.sleep(1)
# type with quarter-second pause in between each key
pyautogui.write('Hello world!', interval=0.25)
# Press the Esc key. All key names are in pyautogui.KEY_NAMES
pyautogui.press('esc')
time.sleep(1)
print()

print("==> press shift and hold, move arrow")
time.sleep(1)
# Press the Shift key down and hold it.
with pyautogui.hold('shift'):
    # Press the left arrow key 4 times.
    pyautogui.press(['left', 'left', 'left', 'left'])
# Shift key is released automatically.
time.sleep(1)
print()

print("==> ctrl-c")
time.sleep(1)
# Press the Ctrl-C hotkey combination.
pyautogui.hotkey('ctrl', 'c')
time.sleep(1)
print()

print("==> alert")
time.sleep(1)
# Make an alert box appear and pause the program until OK is clicked.
pyautogui.alert('This is the message to display.')
