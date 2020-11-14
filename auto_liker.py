import pyautogui
import time
pyautogui.FAILSAFE = False
while True:
    time.sleep(3)
    pyautogui.press("j")
    time.sleep(2)
    pyautogui.press("l")
    time.sleep(1)
    pyautogui.press("enter")
