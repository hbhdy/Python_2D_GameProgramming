import random
import game_framework

from pico2d import *


class Skill1:

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 0.8 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 7


    skill1_image=None

    def __init__(self):
        self.x=230
        self.y=120
        self.damage=25
        self.total_frames=0.0
        self.frame=0
        self.init=0
        self.state = False
        self.notAttack = False

        if self.skill1_image==None:
             self.skill1_image=load_image("resource\\skill\\c1_skill.png")

    def skill1_Attack(self):
        self.state = True

    def skill1_Allow(self):
        self.notAttack = False

    def skill1_Not(self):
        self.notAttack = True

    def get_Attack1(self):
        return self.notAttack

    def get_skill1(self):
        return self.state

    def update(self,frame_time):
        self.total_frames+=Skill1.FRAMES_PER_ACTION*Skill1.ACTION_PER_TIME*frame_time
        if self.state == True:
            self.frame=int(self.total_frames)%7
            self.init+=frame_time
        if self.init>=1:
            self.state = False
            self.init=0


    def draw(self):
        if self.state == True:
            self.skill1_image.clip_draw(self.frame *768 , 0,768, 768, 400, 350)

    def get_bb(self):
        return self.x-20,self.y-60,self.x+20,self.y+200

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

class Skill2:

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 0.8 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 7


    skill2_image=None

    def __init__(self):
        self.x=230
        self.y=120
        self.damage=50
        self.total_frames=0.0
        self.frame=0
        self.init=0
        self.state = False
        self.notAttack = False

        if self.skill2_image==None:
             self.skill2_image=load_image("resource\\skill\\c2_skill.png")

    def skill2_Attack(self):
        self.state = True

    def skill2_Allow(self):
        self.notAttack = False

    def skill2_Not(self):
        self.notAttack = True

    def get_Attack2(self):
        return self.notAttack

    def get_skill2(self):
        return self.state

    def update(self,frame_time):
        self.total_frames+=Skill2.FRAMES_PER_ACTION*Skill2.ACTION_PER_TIME*frame_time
        if self.state == True:
            self.frame=int(self.total_frames)%8
            self.init+=frame_time
        if self.init>=1:
            self.state = False
            self.init=0


    def draw(self):
        if self.state == True:
            self.skill2_image.clip_draw(self.frame *768, 0,768, 768, 400, 350)

    def get_bb(self):
        return self.x-210,self.y-60,self.x+210,self.y+200

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

class Skill3:

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 0.8 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 7


    skill3_image=None

    def __init__(self):
        self.x=230
        self.y=120
        self.damage=100
        self.total_frames=0.0
        self.frame=0
        self.init=0
        self.state = False
        self.notAttack = False

        if self.skill3_image==None:
             self.skill3_image=load_image("resource\\skill\\c3_skill.png")

    def skill3_Attack(self):
        self.state = True

    def skill3_Allow(self):
        self.notAttack = False

    def skill3_Not(self):
        self.notAttack = True

    def get_Attack3(self):
        return self.notAttack

    def get_skill3(self):
        return self.state

    def update(self,frame_time):
        self.total_frames+=Skill3.FRAMES_PER_ACTION*Skill3.ACTION_PER_TIME*frame_time
        if self.state == True:
            self.frame=int(self.total_frames)%7
            self.init+=frame_time
        if self.init>=1:
            self.state = False
            self.init=0


    def draw(self):
        if self.state == True:
            self.skill3_image.clip_draw(self.frame *768 , 0,768, 768, 400, 350)

    def get_bb(self):
        return self.x-210,self.y-60,self.x+210,self.y+200

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

class Skill4:

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 0.8 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 7


    skill4_image=None

    def __init__(self):
        self.x=230
        self.y=120
        self.damage=230
        self.total_frames=0.0
        self.frame=0
        self.init=0
        self.state = False
        self.notAttack = False

        if self.skill4_image==None:
             self.skill4_image=load_image("resource\\skill\\c4_skill.png")

    def skill4_Attack(self):
        self.state = True

    def skill4_Allow(self):
        self.notAttack = False

    def skill4_Not(self):
        self.notAttack = True

    def get_Attack4(self):
        return self.notAttack

    def get_skill4(self):
        return self.state

    def update(self,frame_time):
        self.total_frames+=Skill4.FRAMES_PER_ACTION*Skill4.ACTION_PER_TIME*frame_time
        if self.state == True:
            self.frame=int(self.total_frames)%6
            self.init+=frame_time
        if self.init>=1:
            self.state = False
            self.init=0


    def draw(self):
        if self.state == True:
            self.skill4_image.clip_draw(self.frame *768, 0,768, 768, 400,350)

    def get_bb(self):
        return self.x-210,self.y-60,self.x+100,self.y+200

    def draw_bb(self):
        draw_rectangle(*self.get_bb())


