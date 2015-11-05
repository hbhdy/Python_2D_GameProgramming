import random
import game_framework
import os
os.chdir('C:\\Temp\\2DGP\\hbhdy')
from pico2d import *



class Ch1:
    def __init__(self):
        self.x=100
        self.die=load_image("resource\\team\\ch1\\die.png")
        self.walk=load_image("resource\\team\\ch1\\walk.png")
        self.attack=load_image("resource\\team\\ch1\\attack.png")

        self.die_frame=0
        self.walk_frame=0
        self.attack_frame=0

    def update(self):
        self.die_frame=(self.die_frame+1)%7
        self.walk_frame = (self.walk_frame+1)%8
        self.x +=10
        self.attack_frame=(self.attack_frame+1)%5

    def draw(self):
        #self.die.clip_draw(self.die_frame *384 , 0,384, 384, 200, 300)
        self.walk.clip_draw(self.walk_frame *288 , 0,  288, 288, self.x, 206)
        #self.attack.clip_draw(self.attack_frame *288 , 0, 288, 288, 200, 600)

class Ch2:
    def __init__(self):
        self.x=120
        self.die = load_image("resource\\team\\ch2\\die.png")
        self.walk = load_image("resource\\team\\ch2\\walk.png")
        self.attack = load_image("resource\\team\\ch2\\attack.png")

        self.die_frame=0
        self.walk_frame=0
        self.attack_frame=0

    def update(self):
        self.die_frame=(self.die_frame+1)%7
        self.walk_frame = (self.walk_frame+1)%10
        self.x +=10
        self.attack_frame=(self.attack_frame+1)%13

    def draw(self):
       # self.die.clip_draw(self.die_frame *384 , 0,384, 384, 300, 300)
        self.walk.clip_draw(self.walk_frame *288 , 0,  288, 288, self.x, 205)
        #self.attack.clip_draw(self.attack_frame *288 , 0, 288, 288, 300, 600)

class Ch3:
    def __init__(self):
        self.x=140
        self.die=load_image("resource\\team\\ch3\\die.png")
        self.walk=load_image("resource\\team\\ch3\\walk.png")
        self.attack=load_image("resource\\team\\ch3\\attack.png")

        self.die_frame=0
        self.walk_frame=0
        self.attack_frame=0

    def update(self):
        self.die_frame=(self.die_frame+1)%6
        self.walk_frame = (self.walk_frame+1)%10
        self.x +=10
        self.attack_frame=(self.attack_frame+1)%10

    def draw(self):
        #self.die.clip_draw(self.die_frame *384 , 0,384, 384, 500, 300)
        self.walk.clip_draw(self.walk_frame *288 , 0,  288, 288, self.x, 205)
        #self.attack.clip_draw(self.attack_frame *288 , 0, 288, 288, 500, 600)

class Ch4:
    def __init__(self):
        self.x=160
        self.die=load_image("resource\\team\\ch4\\die.png")
        self.walk=load_image("resource\\team\\ch4\\walk.png")
        self.attack=load_image("resource\\team\\ch4\\attack.png")

        self.die_frame=0
        self.walk_frame=0
        self.attack_frame=0

    def update(self):
        self.die_frame=(self.die_frame+1)%8
        self.walk_frame = (self.walk_frame+1)%10
        self.x +=10
        self.attack_frame=(self.attack_frame+1)%7

    def draw(self):
        #self.die.clip_draw(self.die_frame *384 , 0,384, 384, 200,300)
        self.walk.clip_draw(self.walk_frame *288 , 0,  288, 288, self.x, 200)
        #self.attack.clip_draw(self.attack_frame *288 , 0, 288, 288, 600, 600)
