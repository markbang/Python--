#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import pyautogui
import cv2
import numpy as np
import time
# 做出开始界面
pyautogui.alert(text='钓鱼脚本', title='钓鱼脚本', button='OK')

# 找图 返回最近似的点
def search_returnPoint(img, template, template_size):
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    template_ = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
    result = cv2.matchTemplate(img_gray, template_, cv2.TM_CCOEFF_NORMED)
    threshold = 0.9
    # res大于70%
    loc = np.where(result >= threshold)
    # 使用灰度图像中的坐标对原始RGB图像进行标记
    point = ()
    for pt in zip(*loc[::-1]):
        cv2.rectangle(img, pt, (pt[0] + template_size[1], pt[1] + + template_size[0]), (7, 249, 151), 2)
        point = pt
    if point == ():
        return None, None, None
    return img, point[0] + template_size[1] / 2, point[1]
while True:
    pyautogui.screenshot('hooking.png')
    scale = 1
    img = cv2.imread('hooking.png')  # 要找的大图
    img = cv2.resize(img, (0, 0), fx=scale, fy=scale)
    template = cv2.imread('normal hook.png')  # 图中的小图
    template = cv2.resize(template, (0, 0), fx=scale, fy=scale)
    template_size = template.shape[:2]
    img, x, y = search_returnPoint(img, template, template_size)
    if img is None:
        print("没找到图片")
        pyautogui.doubleClick(1376,800,button='left')
        time.sleep(1)
    else:
        print("找到图片")
        time.sleep(0.5)