import pyautogui
from PIL import Image
import time
import random

width, height = pyautogui.size()
currentMouseX, currentMouseY = pyautogui.position()
for i in range(2):
    pyautogui.moveTo(100, 100, duration=0.25)
    pyautogui.moveTo(200, 100, duration=0.25)
    pyautogui.moveTo(200, 200, duration=0.25)
    pyautogui.moveTo(100, 200, duration=0.25)
    pyautogui.moveTo(width/2, height/2, duration=0.25)
