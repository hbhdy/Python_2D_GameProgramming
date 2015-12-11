import random
import game_framework

from pico2d import *


class Skill1:
    #
    # TIME_PER_ACTION = 0.5
    # ACTION_PER_TIME = 5 / TIME_PER_ACTION
    # FRAMES_PER_ACTION = 7


    skill1=None

    def __init__(self):
        self.x=200
        self.y=120
        self.total_frames=0.0
        self.frame=0


        if self.skill1==None:
             self.skill1=load_image("resource\\skill\\c1_skill.png")

    def update(self):
        # self.total_frames+=Skill1.FRAMES_PER_ACTION*Skill1.ACTION_PER_TIME*frame_time
        self.total_frames=(self.frame+1)%7


    def draw(self):
        self.skill1.clip_draw(self.total_frames *384 , 0,384, 384, self.x, 206)


    def get_bb(self):
        return self.x-60,self.y-60,self.x+60,self.y+80
    def draw_bb(self):
        draw_rectangle(*self.get_bb())
