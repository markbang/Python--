import time
import math


class Projectile:
    def __init__(self, jiao, vel, high, gtime):
        self.time = gtime
        self.xpos = 0
        self.ypos = high
        self.xvel = vel*math.cos(jiao)
        self.yvel = vel*math.sin(jiao)

    def getposition(self):
        while self.ypos>0:
            self.xpos += self.xvel*self.time
            self.ypos += self.yvel*self.time-0.5*9.8*self.time**2
            self.yvel -= 9.8*self.time
            print('坐标：({0},{1})'.format(self.xpos,self.ypos))
            if self.ypos + self.yvel*self.time-0.5*9.8*self.time**2<0:
                a = -0.5*9.8
                b = self.yvel
                c = self.ypos
                delta = b * b - 4 * a * c
                x1 = (-1 * b + math.sqrt(delta)) / (2 * a)
                x2 = (-1 * b - math.sqrt(delta)) / (2 * a)
                self.xpos += self.xvel * x2
                self.ypos += self.yvel * x2 - 0.5 * 9.8 * x2 ** 2
                print('最后一次纠正的坐标：({0},{1})'.format(self.xpos, self.ypos))
            time.sleep(self.time)


self_jiao = float(input('抛出角度(整数，自动单位°):'))
self_vel = float(input('抛出速度(m/s):'))
self_time = float(input('更新坐标间隔时间(s):'))
self_high = float(input('运动员身高(m):'))
bal = Projectile(self_jiao,self_vel,self_high,self_time)
bal.getposition()

