import random
import game_framework

from pico2d import *



class Character1:
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
        distance=Character1.RUN_SPEED_PPS*frame_time
        self.total_frames+=Character1.FRAMES_PER_ACTION*Character1.ACTION_PER_TIME*frame_time
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


    def draw_die(self):
        self.die.clip_draw(self.frame *384 , 0,384, 384, self.x, 300)
    def draw_attack(self):
        self.attack.clip_draw(self.frame *288 , 0, 288, 288, self.x, 600)
    def draw_walk(self):
        self.walk.clip_draw(self.frame *288 , 0,  288, 288, self.x, 206)

class Character2:
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
        distance = Character2.RUN_SPEED_PPS * frame_time
        self.total_frames+=Character2.FRAMES_PER_ACTION*Character2.ACTION_PER_TIME*frame_time
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
    def draw_die(self):
        self.die.clip_draw(self.frame *384 , 0,384, 384, self.x, 300)
    def draw_walk(self):
        self.walk.clip_draw(self.frame *288 , 0,  288, 288, self.x, 205)
    def draw_attack(self):
        self.attack.clip_draw(self.frame *288 , 0, 288, 288, self.x, 600)

class Character3:
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
        distance=Character3.RUN_SPEED_PPS*frame_time
        self.walk_frame+=Character3.FRAMES_PER_ACTION*Character3.ACTION_PER_TIME*frame_time
        self.attack_frame+=Character3.FRAMES_PER_ACTION*Character3.ACTION_PER_TIME*frame_time
        self.die_frame+=Character3.FRAMES_PER_ACTION*Character3.ACTION_PER_TIME*frame_time
        if self.state==self.WALK:
            self.frame = int(self.walk_frame)%10
        if self.state==self.ATTACK:
            self.frame=int(self.attack_frame)%13
        if self.state==self.DIE:
            self.frame=int(self.die_frame)%7
        self.x+=(self.start*distance)

        if self.x > 1000:
            self.start=0



    def draw_die(self):
        self.die.clip_draw(self.frame *384 , 0,384, 384, self.x, 300)
    def draw_walk(self):
        self.walk.clip_draw(self.frame *288 , 0,  288, 288, self.x, 205)
    def draw_attack(self):
        self.attack.clip_draw(self.frame *288 , 0, 288, 288, self.x, 205)

class Character4:
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
        distance = Character4.RUN_SPEED_PPS * frame_time
        self.total_frames += Character4.FRAMES_PER_ACTION * Character4.ACTION_PER_TIME * frame_time
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
    def draw_die(self):
        self.die.clip_draw(self.frame *384 , 0,384, 384, self.x,300)
    def draw_walk(self):
        self.walk.clip_draw(self.frame *288 , 0,  288, 288, self.x, 200)
    def draw_attack(self):
        self.attack.clip_draw(self.frame *288 , 0, 288, 288, self.x, 600)
