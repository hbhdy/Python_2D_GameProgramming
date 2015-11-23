import random
import game_framework

from pico2d import *



class Character1:
    PIXEL_PER_METER = (10.0 / 0.2)           # 10 pixel 20 cm
    RUN_SPEED_KMPH = 5.0                    # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 0.4
    ACTION_PER_TIME = 0.5 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 8

    now_state="Walk"


    def __init__(self):
        self.x=100
        self.y=140
        self.hp=30
        self.damage=5
        self.damage_time = 0

        self.total_frames=0.0
        self.die_frame=0
        self.walk_frame=0
        self.attack_frame=0
        self.start=1
        self.now_state = "Walk"

        self.die=load_image("resource\\team\\ch1\\die.png")
        self.walk=load_image("resource\\team\\ch1\\walk.png")
        self.attack=load_image("resource\\team\\ch1\\attack.png")

    def Send_State(self):
        return str(self.now_state)

    def Receive_State(self, now_state):
        self.now_state = now_state

    def Attack(self):
        return self.attack_frame

    def update(self,frame_time):
        distance=Character1.RUN_SPEED_PPS*frame_time
        self.total_frames+=Character1.FRAMES_PER_ACTION*Character1.ACTION_PER_TIME*frame_time

        if self.now_state == "Walk":
            self.walk_frame= int(self.total_frames)%8
            self.x+=(self.start*distance)

        if self.now_state == "Attack":
            self.attack_frame= int(self.total_frames)%5

        if self.now_state=="Die":
            self.die_frame= int(self.total_frames)%7

    def damaged(self, zombie, frame_time):
        self.damage_time += frame_time

        if zombie.attack_frame == 0:
            if self.damage_time > 0.1:
                self.damage_time = 0
                self.hp -= zombie.damage
                if self.hp <= 0 : return True
        return False

    def damaged(self, vampire, frame_time):
        self.damage_time += frame_time

        if vampire.attack_frame == 0:
            if self.damage_time > 0.1:
                self.damage_time = 0
                self.hp -= vampire.damage
                if self.hp <= 0 : return True
        return False

    def damaged(self, skeleton, frame_time):
        self.damage_time += frame_time

        if skeleton.attack_frame == 0:
            if self.damage_time > 0.1:
                self.damage_time = 0
                self.hp -= skeleton.damage
                if self.hp <= 0 : return True
        return False

    def damaged(self, golem, frame_time):
        self.damage_time += frame_time

        if golem.attack_frame == 0:
            if self.damage_time > 0.1:
                self.damage_time = 0
                self.hp -= golem.damage
                if self.hp <= 0 : return True
        return False


    def get_bb(self):
        return self.x-50,self.y-70,self.x+50,self.y+20
    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def draw_die(self):
        self.die.clip_draw(self.die_frame *384 , 0,384, 384, self.x, 206)
    def draw_attack(self):
        self.attack.clip_draw(self.attack_frame *288 , 0, 288, 288, self.x, 206)
    def draw_walk(self):
        self.walk.clip_draw(self.walk_frame *288 , 0,  288, 288, self.x, 206)

class Character2:
    PIXEL_PER_METER = (10.0 / 0.2)           # 10 pixel 20 cm
    RUN_SPEED_KMPH = 5.0                    # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 0.4
    ACTION_PER_TIME = 0.5 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 8

    now_state="Walk"

    def __init__(self):
        self.x=120
        self.y=120
        self.hp=30
        self.damage=5
        self.damage_time = 0
        self.now_state="Walk"


        self.total_frames=0.0
        self.die_frame=0
        self.walk_frame=0
        self.attack_frame=0
        self.start=1

        self.die = load_image("resource\\team\\ch2\\die.png")
        self.walk = load_image("resource\\team\\ch2\\walk.png")
        self.attack = load_image("resource\\team\\ch2\\attack.png")

    def Send_State(self):
        return self.now_state

    def Receive_State(self, now_state):
        self.now_state = now_state

    def Attack(self):
        return self.attack_frame

    def update(self,frame_time):
        distance = Character2.RUN_SPEED_PPS * frame_time
        self.total_frames+=Character2.FRAMES_PER_ACTION*Character2.ACTION_PER_TIME*frame_time

        if self.now_state=="Walk":
            self.walk_frame=int(self.total_frames)%10
            self.x+=(self.start*distance)
        if self.now_state=="Attack":
            self.start=0
            self.attack_frame=int(self.total_frames)%7
        if self.now_state=="Die":
            self.die_frame=int(self.total_frames)&8

    def damaged(self, zombie, frame_time):
        self.damage_time += frame_time

        if zombie.attack_frame == 0:
            if self.damage_time > 0.1:
                self.damage_time = 0
                self.hp -= zombie.damage
                if self.hp <= 0 : return True
        return False

    def damaged(self, vampire, frame_time):
        self.damage_time += frame_time

        if vampire.attack_frame == 0:
            if self.damage_time > 0.1:
                self.damage_time = 0
                self.hp -= vampire.damage
                if self.hp <= 0 : return True
        return False

    def damaged(self, skeleton, frame_time):
        self.damage_time += frame_time

        if skeleton.attack_frame == 0:
            if self.damage_time > 0.1:
                self.damage_time = 0
                self.hp -= skeleton.damage
                if self.hp <= 0 : return True
        return False

    def damaged(self, golem, frame_time):
        self.damage_time += frame_time

        if golem.attack_frame == 0:
            if self.damage_time > 0.1:
                self.damage_time = 0
                self.hp -= golem.damage
                if self.hp <= 0 : return True
        return False


    def get_bb(self):
        return self.x-60,self.y-60,self.x+60,self.y+100
    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def draw_die(self):
        self.die.clip_draw(self.die_frame *384 , 0,384, 384, self.x, 205)
    def draw_walk(self):
        self.walk.clip_draw(self.walk_frame *288 , 0,  288, 288, self.x, 205)
    def draw_attack(self):
        self.attack.clip_draw(self.attack_frame *288 , 0, 288, 288, self.x, 205)

class Character3:
    PIXEL_PER_METER = (10.0 / 0.2)           # 10 pixel 20 cm
    RUN_SPEED_KMPH = 5.0                    # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 0.4
    ACTION_PER_TIME = 0.5 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 8

    now_state="Walk"

    def __init__(self):
        self.x=140
        self.y=120
        self.hp=30
        self.damage=5
        self.damage_time = 0
        self.now_state="Walk"

        self.total_frames=0.0
        self.die_frame=0
        self.walk_frame=0
        self.attack_frame=0
        self.start=1

        self.die=load_image("resource\\team\\ch3\\die.png")
        self.walk=load_image("resource\\team\\ch3\\walk.png")
        self.attack=load_image("resource\\team\\ch3\\attack.png")

    def Send_State(self):
        return self.now_state

    def Receive_State(self, now_state):
        self.now_state = now_state

    def Attack(self):
        return self.attack_frame

    def update(self,frame_time):
        distance=Character3.RUN_SPEED_PPS*frame_time
        self.total_frames+=Character3.FRAMES_PER_ACTION*Character3.ACTION_PER_TIME*frame_time

        if self.now_state=="Walk":
            self.walk_frame = int(self.total_frames)%10
            self.x+=(self.start*distance)
        if self.now_state=="Attack":
            self.start=0
            self.attack_frame=int(self.total_frames)%13
        if self.now_state=="Die":
            self.die_frame=int(self.total_frames)%7

    def damaged(self, zombie, frame_time):
        self.damage_time += frame_time

        if zombie.attack_frame == 0:
            if self.damage_time > 0.1:
                self.damage_time = 0
                self.hp -= zombie.damage
                if self.hp <= 0 : return True
        return False

    def damaged(self, vampire, frame_time):
        self.damage_time += frame_time

        if vampire.attack_frame == 0:
            if self.damage_time > 0.1:
                self.damage_time = 0
                self.hp -= vampire.damage
                if self.hp <= 0 : return True
        return False

    def damaged(self, skeleton, frame_time):
        self.damage_time += frame_time

        if skeleton.attack_frame == 0:
            if self.damage_time > 0.1:
                self.damage_time = 0
                self.hp -= skeleton.damage
                if self.hp <= 0 : return True
        return False

    def damaged(self, golem, frame_time):
        self.damage_time += frame_time

        if golem.attack_frame == 0:
            if self.damage_time > 0.1:
                self.damage_time = 0
                self.hp -= golem.damage
                if self.hp <= 0 : return True
        return False

    def get_bb(self):
        return self.x-70,self.y-70,self.x+70,self.y+120
    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def draw_die(self):
        self.die.clip_draw(self.die_frame *384 , 0,384, 384, self.x, 205)
    def draw_walk(self):
        self.walk.clip_draw(self.walk_frame *288 , 0,  288, 288, self.x, 205)
    def draw_attack(self):
        self.attack.clip_draw(self.attack_frame *288 , 0, 288, 288, self.x, 205)

class Character4:
    PIXEL_PER_METER = (10.0 / 0.2)           # 10 pixel 20 cm
    RUN_SPEED_KMPH = 5.0                    # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 0.4
    ACTION_PER_TIME = 0.5 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 8

    now_state="Walk"

    def __init__(self):
        self.x=160
        self.y=120
        self.hp=30
        self.damage=50
        self.damage_time = 0

        self.total_frames=0.0
        self.die_frame=0
        self.walk_frame=0
        self.attack_frame=0
        self.start=1

        self.die=load_image("resource\\team\\ch4\\die.png")
        self.walk=load_image("resource\\team\\ch4\\walk.png")
        self.attack=load_image("resource\\team\\ch4\\attack.png")

    def Send_State(self):
        return self.now_state

    def Receive_State(self, now_state):
        self.now_state = now_state

    def Attack(self):
        return self.attack_frame

    def update(self,frame_time):
        distance = Character4.RUN_SPEED_PPS * frame_time
        self.total_frames += Character4.FRAMES_PER_ACTION * Character4.ACTION_PER_TIME * frame_time

        if self.now_state=="Walk":
            self.walk_frame=int(self.total_frames)%10
            self.x+=(self.start*distance)
        if self.now_state=="Attack":
            self.start=0
            self.attack_frame=int(self.total_frames)%10
        if self.now_state=="Die":
            self.die_frame=int(self.total_frames)%6

    def damaged(self, zombie, frame_time):
        self.damage_time += frame_time

        if zombie.attack_frame == 0:
            if self.damage_time > 0.1:
                self.damage_time = 0
                self.hp -= zombie.damage
                if self.hp <= 0 : return True
        return False

    def damaged(self, vampire, frame_time):
        self.damage_time += frame_time

        if vampire.attack_frame == 0:
            if self.damage_time > 0.1:
                self.damage_time = 0
                self.hp -= vampire.damage
                if self.hp <= 0 : return True
        return False

    def damaged(self, skeleton, frame_time):
        self.damage_time += frame_time

        if skeleton.attack_frame == 0:
            if self.damage_time > 0.1:
                self.damage_time = 0
                self.hp -= skeleton.damage
                if self.hp <= 0 : return True
        return False

    def damaged(self, golem, frame_time):
        self.damage_time += frame_time

        if golem.attack_frame == 0:
            if self.damage_time > 0.1:
                self.damage_time = 0
                self.hp -= golem.damage
                if self.hp <= 0 : return True
        return False

    def get_bb(self):
        return self.x-60,self.y-60,self.x+60,self.y+80
    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def draw_die(self):
        self.die.clip_draw(self.die_frame *384 , 0,384, 384, self.x,205)
    def draw_walk(self):
        self.walk.clip_draw(self.walk_frame *288 , 0,  288, 288, self.x, 205)
    def draw_attack(self):
        self.attack.clip_draw(self.attack_frame *288 , 0, 288, 288, self.x, 205)
