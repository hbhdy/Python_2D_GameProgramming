import random
import game_framework
import os
os.chdir('C:\\Temp\\2DGP\\hbhdy')
from pico2d import *



class Zombie():
    def __init__(self):
        self.x=1400
        self.die = load_image("resource\\enemy\\zombie\\die.png")
        self.walk = load_image("resource\\enemy\\zombie\\walk.png")
        self.attack = load_image("resource\\enemy\\zombie\\attack.png")
        self.appear = load_image("resource\\enemy\\zombie\\appear.png")

        self.die_frame=0
        self.walk_frame=0
        self.attack_frame=0
        self.appear_frame=0

    def update(self):
        self.appear_frame=(self.appear_frame+1)%11
        self.die_frame=(self.die_frame+1)%8
        self.walk_frame =(self.walk_frame+1)%10
        self.x-=10
        self.attack_frame=(self.attack_frame+1)%7



    def draw(self):
        self.appear.clip_draw(self.appear_frame *163, 0, 163, 214, 1500, 300)
        self.die.clip_draw(self.die_frame *325, 0, 325, 214,1500, 500)
        self.walk.clip_draw(self.walk_frame *140, 0, 140, 218, self.x,170)
        self.attack.clip_draw(self.attack_frame *251, 0, 251, 219, 1500, 700)


class Vampire:
    def __init__(self):
        self.x=1300
        self.die=load_image("resource\\enemy\\vampire\\die.png")
        self.walk=load_image("resource\\enemy\\vampire\\walk.png")
        self.attack=load_image("resource\\enemy\\vampire\\attack.png")
        self.appear=load_image("resource\\enemy\\vampire\\appear.png")

        self.die_frame=0
        self.walk_frame=0
        self.attack_frame=0
        self.appear_frame=0

    def update(self):
        self.die_frame=(self.die_frame+1)%8
        self.walk_frame = (self.walk_frame+1)%5
        self.x-=10
        self.attack_frame=(self.attack_frame+1)%9
        self.appear_frame=(self.appear_frame+1)%8

    def draw(self):
        self.die.clip_draw(self.die_frame *192 , 0, 192, 220, 1300, 500)
        self.walk.clip_draw(self.walk_frame *120 , 0, 120, 215, self.x, 170)
        self.attack.clip_draw(self.attack_frame *290 , 0, 290, 218, 1300, 700)
        self.appear.clip_draw(self.appear_frame *191 , 0, 191, 219, 1300, 300)

class Skeleton:
    def __init__(self):
        self.x=1100
        self.die=load_image("resource\\enemy\\skeleton\\die.png")
        self.walk=load_image("resource\\enemy\\skeleton\\walk.png")
        self.attack=load_image("resource\\enemy\\skeleton\\attack.png")
        self.appear=load_image("resource\\enemy\\skeleton\\appear.png")

        self.die_frame=0
        self.walk_frame=0
        self.attack_frame=0
        self.appear_frame=0

    def update(self):
        self.die_frame=(self.die_frame+1)%8
        self.walk_frame = (self.walk_frame+1)%8
        self.x-=10
        self.attack_frame=(self.attack_frame+1)%8
        self.appear_frame=(self.appear_frame+1)%10

    def draw(self):
        self.die.clip_draw(self.die_frame *275 , 0,275, 220, 1100, 500)
        self.walk.clip_draw(self.walk_frame *135 , 0, 135, 219, self.x, 170)
        self.attack.clip_draw(self.attack_frame *185 , 0, 185, 217, 1100, 700)
        self.appear.clip_draw(self.appear_frame *172 , 0, 172, 220, 1100, 300)

class Golem:
    def __init__(self):
        self.x=900
        self.die=load_image("resource\\enemy\\golem\\die.png")
        self.walk=load_image("resource\\enemy\\golem\\walk.png")
        self.attack=load_image("resource\\enemy\\golem\\attack.png")
        self.appear=load_image("resource\\enemy\\golem\\appear.png")

        self.die_frame=0
        self.walk_frame=0
        self.attack_frame=0
        self.appear_frame=0

    def update(self):
        self.die_frame=(self.die_frame+1)%6
        self.walk_frame = (self.walk_frame+1)%6
        self.x -=10
        self.attack_frame=(self.attack_frame+1)%6
        self.appear_frame=(self.appear_frame+1)%8

    def draw(self):
        self.die.clip_draw(self.die_frame *300 , 0,300, 331, 900, 500)
        self.walk.clip_draw(self.walk_frame *320 , 0, 320, 245, self.x, 190)
        self.attack.clip_draw(self.attack_frame *350 , 0, 350, 247, 900, 700)
        self.appear.clip_draw(self.appear_frame *322 , 0, 332, 246, 900, 300)


