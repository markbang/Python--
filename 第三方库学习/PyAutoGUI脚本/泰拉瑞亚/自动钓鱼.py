import pyautogui
from PIL import Image
import time
import random
time.sleep(2)
pyautogui.moveTo(1440, 800, duration=0.25)
pyautogui.click(1440,800,button='left')
time.sleep(0.5)
while True:
    if not pyautogui.pixelMatchesColor(1376,864,(60,52,56),tolerance=10):
        pyautogui.doubleClick()
