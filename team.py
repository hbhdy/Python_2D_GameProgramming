import random
import game_framework
import os
os.chdir('C:\\Temp\\2DGP\\hbhdy')
from pico2d import *



class Ch1:
    PIXEL_PER_METER = (10.0 / 0.1)           # 10 pixel 10 cm
    RUN_SPEED_KMPH = 5.0                    # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    WALK,ATTACK,DIE=1,2,3

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 0.5 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 6


    def __init__(self):
        self.x=100
        self.frame=0
        self.total_frames=0.0
        self.start=1
        self.state=self.WALK
        self.die=load_image("resource\\team\\ch1\\die.png")
        self.walk=load_image("resource\\team\\ch1\\walk.png")
        self.attack=load_image("resource\\team\\ch1\\attack.png")


    def update(self,frame_time):
        distance=Ch1.RUN_SPEED_PPS*frame_time
        self.total_frames+=Ch1.FRAMES_PER_ACTION*Ch1.ACTION_PER_TIME*frame_time
        if self.state==self.WALK:
            self.frame= int(self.total_frames)%8
        if self.state==self.ATTACK:
            self.frame= int(self.total_frames)%5
        if self.state==self.DIE:
            self.frame= int(self.total_frames)%7
        self.x+=(self.start*distance)

        if self.x > 1500:
            self.start = 0
            self.x = random.randint(1100, 1103)
            self.state = self.ATTACK
        elif self.x < 100:
            self.dir = 1
            self.x = 100
            self.state = self.WALK


    def draw(self):
        #self.die.clip_draw(self.die_frame *384 , 0,384, 384, 200, 300)
        self.walk.clip_draw(self.frame *288 , 0,  288, 288, self.x, 206)
        #self.attack.clip_draw(self.attack_frame *288 , 0, 288, 288, 200, 600)

class Ch2:
    PIXEL_PER_METER = (10.0 / 0.1)           # 10 pixel 10 cm
    RUN_SPEED_KMPH = 5.0                    # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    WALK,ATTACK,DIE=1,2,3

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 0.5 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 6

    def __init__(self):
        self.x=120
        self.frame=0
        self.total_frames=0.0
        self.start=1
        self.state=self.WALK
        self.die = load_image("resource\\team\\ch2\\die.png")
        self.walk = load_image("resource\\team\\ch2\\walk.png")
        self.attack = load_image("resource\\team\\ch2\\attack.png")

    def update(self,frame_time):
        distance = Ch2.RUN_SPEED_PPS * frame_time
        self.total_frames+=Ch1.FRAMES_PER_ACTION*Ch1.ACTION_PER_TIME*frame_time
        if self.state==self.WALK:
            self.frame=int(self.total_frames)%10
        if self.state==self.ATTACK:
            self.frame=int(self.total_frames)%7
        if self.state==self.DIE:
            self.frame=int(self.total_frames)&8


        if self.x > 1500:
            self.start = 0
            self.x = random.randint(1100, 1103)
            self.state = self.ATTACK
        elif self.x < 100:
            self.start = 0.8
            self.x = 100
            self.state = self.WALK
    def draw(self):
       # self.die.clip_draw(self.die_frame *384 , 0,384, 384, 300, 300)
        self.walk.clip_draw(self.frame *288 , 0,  288, 288, self.x, 205)
        #self.attack.clip_draw(self.attack_frame *288 , 0, 288, 288, 300, 600)

class Ch3:
    PIXEL_PER_METER = (10.0 / 0.1)           # 10 pixel 10 cm
    RUN_SPEED_KMPH = 5.0                    # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    WALK,ATTACK,DIE=1,2,3

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 0.5 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 6

    def __init__(self):
        self.x=140
        self.frame=0
        self.attack_frame=0.0
        self.die_frame=0.0
        self.walk_frame=0.0
        self.start=1
        self.state=self.WALK
        self.die=load_image("resource\\team\\ch3\\die.png")
        self.walk=load_image("resource\\team\\ch3\\walk.png")
        self.attack=load_image("resource\\team\\ch3\\attack.png")

    def update(self,frame_time):
        distance=Ch3.RUN_SPEED_PPS*frame_time
        self.walk_frame+=Ch3.FRAMES_PER_ACTION*Ch3.ACTION_PER_TIME*frame_time
        self.attack_frame+=Ch3.FRAMES_PER_ACTION*Ch3.ACTION_PER_TIME*frame_time
        self.die_frame+=Ch3.FRAMES_PER_ACTION*Ch3.ACTION_PER_TIME*frame_time
        if self.state==self.WALK:
            self.frame = int(self.walk_frame+1)%10
        if self.state==self.ATTACK:
            self.frame=int(self.attack_frame+1)%13
        if self.state==self.DIE:
            self.frame=int(self.die_frame+1)%7
        self.x+=(self.start*distance)

        if self.x > 1000:
            self.start=0
            self.state = self.ATTACK


    def draw(self):
        #self.die.clip_draw(self.die_frame *384 , 0,384, 384, 500, 300)
        self.walk.clip_draw(self.frame *288 , 0,  288, 288, self.x, 205)
        self.attack.clip_draw(self.frame *288 , 0, 288, 288, self.x, 205)

class Ch4:
    PIXEL_PER_METER = (10.0 / 0.1)           # 10 pixel 10 cm
    RUN_SPEED_KMPH = 5.0                    # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    WALK,ATTACK,DIE=1,2,3

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 0.5 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 6

    def __init__(self):
        self.x=160
        self.frame=0
        self.total_frames=0.0
        self.start=1
        self.state=self.WALK
        self.die=load_image("resource\\team\\ch4\\die.png")
        self.walk=load_image("resource\\team\\ch4\\walk.png")
        self.attack=load_image("resource\\team\\ch4\\attack.png")

    def update(self,frame_time):
        distance = Ch4.RUN_SPEED_PPS * frame_time
        self.total_frames += Ch4.FRAMES_PER_ACTION * Ch4.ACTION_PER_TIME * frame_time
        if self.state==self.WALK:
            self.frame==int(self.total_frames)%10
        if self.state==self.ATTACK:
            self.frame==int(self.total_frames)%10
        if self.state==self.DIE:
            self.frame=int(self.total_frames)%6
        self.x+=(self.start*distance)

        if self.x > 1500:
            self.start = 0
            self.x = random.randint(1100, 1103)
            self.state = self.ATTACK
        elif self.x < 100:
            self.start=0.8
            self.x = 100
            self.state = self.WALK
    def draw(self):
        #self.die.clip_draw(self.die_frame *384 , 0,384, 384, 200,300)
        self.walk.clip_draw(self.frame *288 , 0,  288, 288, self.x, 200)
        #self.attack.clip_draw(self.attack_frame *288 , 0, 288, 288, 600, 600)
