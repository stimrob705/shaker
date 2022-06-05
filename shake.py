import pyautogui
import time
import sys
from datetime import datetime
pyautogui.FAILSAFE = False
numMin = 3
while(True):
    x=0
    while(x<numMin):
        time.sleep(60)
        x+=1
    for i in range(2):
      pyautogui.moveRel(1, 0, duration=0.1)
      pyautogui.moveRel(-1, 0, duration=0.1)

    for i in range(0,2):
        pyautogui.press("shift")
    print("{}".format(datetime.now().time()))
