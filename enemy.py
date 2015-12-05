import random
import game_framework

from pico2d import *


class Zombie:
    PIXEL_PER_METER = (10.0 / 0.2)           # 10 pixel 20 cm
    RUN_SPEED_KMPH = 5.0                    # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 0.4
    ACTION_PER_TIME = 0.5 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 8

    now_state = "Appear"
    init_Start = 0

    def __init__(self):
        self.x=1400
        self.y=140
        self.now_state = "Appear"
        self.hp=20
        self.damage_time = 0
        self.damage=5


        self.die=load_image("resource\\enemy\\zombie\\z_die.png")
        self.walk=load_image("resource\\enemy\\zombie\\z_walk.png")
        self.attack=load_image("resource\\enemy\\zombie\\z_attack.png")
        self.appear=load_image("resource\\enemy\\zombie\\z_appear.png")

        self.start=1
        self.total_frames=0.0
        self.die_frame=0
        self.walk_frame=0
        self.attack_frame=0
        self.appear_frame=0
        self.init_Start = 0


    def Send_State(self):
        return self.now_state

    def Receive_State(self, now_state):
        self.now_state = now_state

    def Attack(self):
        return self.attack_frame

    def Die(self):
        return self.die_frame

    def update(self,frame_time):
        distance = Zombie.RUN_SPEED_PPS * frame_time
        self.total_frames += Zombie.FRAMES_PER_ACTION * Zombie.ACTION_PER_TIME * frame_time

        if self.now_state == "Appear":
            self.appear_frame = int(self.total_frames)%11
            if ( self.appear_frame == 10  and self.init_Start >= 2):
                self.now_state = "Walk"
            else:
                self.init_Start += 1

        if self.now_state == "Walk":
            self.start=1
            self.walk_frame = int(self.total_frames)%10
            self.x-=(self.start*distance)

        if self.now_state=="Attack":
            self.start=0
            self.attack_frame=int(self.total_frames)%7

        if self.now_state=="Die":
            self.die_frame=int(self.total_frames)%8
            # if ( self.die_frame == 8  and self.init_Start >= 4):
            #     self.now_state = "Die"
            # else:
            #     self.init_Start += 1


    def damaged(self, character1, frame_time):
        self.damage_time += frame_time

        if character1.attack_frame == 0:
            if self.damage_time > 1:
                self.damage_time = 0
                self.hp -= character1.damage
                if self.hp <= 0 : return True
        return False

    def damaged(self, character2, frame_time):
        self.damage_time += frame_time

        if character2.attack_frame == 0:
            if self.damage_time > 1:
                self.damage_time = 0
                self.hp -= character2.damage
                if self.hp <= 0 :return True
        return False

    def damaged(self, character3, frame_time):
        self.damage_time += frame_time

        if character3.attack_frame == 0:
            if self.damage_time > 1:
                self.damage_time = 0
                self.hp -= character3.damage
                if self.hp <= 0 : return True
        return False

    def damaged(self, character4, frame_time):
        self.damage_time += frame_time

        if character4.attack_frame == 0:
            if self.damage_time > 1:
                self.damage_time = 0
                self.hp -= character4.damage
                if self.hp <= 0 : return True
        return False

    def get_bb(self):
        return self.x-70,self.y-70,self.x+70,self.y+140
    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def draw_die(self):
        self.die.clip_draw(self.die_frame *325, 0, 325, 214,self.x, 170)
    def draw_walk(self):
        self.walk.clip_draw(self.walk_frame *140, 0, 140, 218, self.x,170)
    def draw_attack(self):
        self.attack.clip_draw(self.attack_frame *251, 0, 251, 219, self.x, 170)
    def draw_appear(self):
        self.appear.clip_draw(self.appear_frame *163, 0, 163, 214, self.x, 170)


class Vampire:
    PIXEL_PER_METER = (10.0 / 0.2)           # 10 pixel 20 cm
    RUN_SPEED_KMPH = 5.0                    # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 0.4
    ACTION_PER_TIME = 0.5 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 8

    now_state = "Appear"
    init_Start = 0

    def __init__(self):
        self.x=1400
        self.y=120
        self.hp=50
        self.damage_time = 0
        self.damage=10
        self.now_state = "Appear"

        self.die=load_image("resource\\enemy\\vampire\\v_die.png")
        self.walk=load_image("resource\\enemy\\vampire\\v_walk.png")
        self.attack=load_image("resource\\enemy\\vampire\\v_attack.png")
        self.appear=load_image("resource\\enemy\\vampire\\v_appear.png")

        self.start=1
        self.total_frames=0.0
        self.die_frame=0
        self.walk_frame=0
        self.attack_frame=0
        self.appear_frame=0
        self.init_Start = 0

    def Send_State(self):
        return self.now_state

    def Receive_State(self, now_state):
        self.now_state = now_state

    def Attack(self):
        return self.attack_frame

    def update(self,frame_time):
        distance = Vampire.RUN_SPEED_PPS * frame_time
        self.total_frames += Vampire.FRAMES_PER_ACTION * Vampire.ACTION_PER_TIME * frame_time

        if self.now_state == "Appear":
            self.appear_frame = int(self.total_frames)%8
            if ( self.appear_frame == 7  and self.init_Start >= 2):
                self.now_state = "Walk"
            else:
                self.init_Start += 1

        if self.now_state == "Walk":
            self.start=1
            self.walk_frame = int(self.total_frames)%5
            self.x-=(self.start*distance)

        if self.now_state=="Attack":
            self.start=0
            self.attack_frame=int(self.total_frames)%9

        if self.now_state=="Die":
            self.die_frame=int(self.total_frames)%8

    def damaged(self, character1, frame_time):
        self.damage_time += frame_time

        if character1.attack_frame == 0:
            if self.damage_time > 1:
                self.damage_time = 0
                self.hp -= character1.damage
                if self.hp <= 0 : return True
        return False

    def damaged(self, character2, frame_time):
        self.damage_time += frame_time

        if character2.attack_frame == 0:
            if self.damage_time > 1:
                self.damage_time = 0
                self.hp -= character2.damage
                if self.hp <= 0 : return True
        return False

    def damaged(self, character3, frame_time):
        self.damage_time += frame_time

        if character3.attack_frame == 0:
            if self.damage_time > 1:
                self.damage_time = 0
                self.hp -= character3.damage
                if self.hp <= 0 : return True
        return False

    def damaged(self, character4, frame_time):
        self.damage_time += frame_time

        if character4.attack_frame == 0:
            if self.damage_time > 1:
                self.damage_time = 0
                self.hp -= character4.damage
                if self.hp <= 0 : return True
        return False

    def get_bb(self):
        return self.x-60,self.y-60,self.x+60,self.y+140
    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def draw_die(self):
        self.die.clip_draw(self.die_frame *192 , 0, 192, 220, self.x, 170)
    def draw_walk(self):
        self.walk.clip_draw(self.walk_frame *120 , 0, 120, 215, self.x, 170)
    def draw_attack(self):
        self.attack.clip_draw(self.attack_frame *290 , 0, 290, 218, self.x, 170)
    def draw_appear(self):
        self.appear.clip_draw(self.appear_frame *191 , 0, 191, 219, self.x, 170)

class Skeleton:

    PIXEL_PER_METER = (10.0 / 0.2)           # 10 pixel 20 cm
    RUN_SPEED_KMPH = 5.0                    # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 0.4
    ACTION_PER_TIME = 0.5 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 8

    now_state = "Appear"
    init_Start = 0

    def __init__(self):
        self.x=1400
        self.y=120
        self.hp=100
        self.damage_time = 0
        self.damage=15
        self.now_state = "Appear"

        self.die=load_image("resource\\enemy\\skeleton\\s_die.png")
        self.walk=load_image("resource\\enemy\\skeleton\\s_walk.png")
        self.attack=load_image("resource\\enemy\\skeleton\\s_attack.png")
        self.appear=load_image("resource\\enemy\\skeleton\\s_appear.png")

        self.start=1
        self.total_frames=0.0
        self.die_frame=0
        self.walk_frame=0
        self.attack_frame=0
        self.appear_frame=0
        self.init_Start = 0

    def Send_State(self):
        return self.now_state

    def Receive_State(self, now_state):
        self.now_state = now_state

    def Attack(self):
        return self.attack_frame

    def update(self,frame_time):
        distance=Skeleton.RUN_SPEED_PPS*frame_time
        self.total_frames += Skeleton.FRAMES_PER_ACTION * Skeleton.ACTION_PER_TIME * frame_time

        if self.now_state == "Appear":
            self.appear_frame = int(self.total_frames)%10
            if ( self.appear_frame == 9  and self.init_Start >= 2):
                self.now_state = "Walk"
            else:
                self.init_Start += 1

        if self.now_state == "Walk":
            self.start=1
            self.walk_frame = int(self.total_frames)%8
            self.x-=(self.start*distance)

        if self.now_state == "Attack":
            self.start=0
            self.attack_frame = int(self.total_frames)%8

        if self.now_state=="Die":
            self.die_frame=int(self.total_frames)%8

    def damaged(self, character1, frame_time):
        self.damage_time += frame_time

        if character1.attack_frame == 0:
            if self.damage_time > 1:
                self.damage_time = 0
                self.hp -= character1.damage
                if self.hp <= 0 : return True
        return False

    def damaged(self, character2, frame_time):
        self.damage_time += frame_time

        if character2.attack_frame == 0:
            if self.damage_time > 1:
                self.damage_time = 0
                self.hp -= character2.damage
                if self.hp <= 0 : return True
        return False

    def damaged(self, character3, frame_time):
        self.damage_time += frame_time

        if character3.attack_frame == 0:
            if self.damage_time > 1:
                self.damage_time = 0
                self.hp -= character3.damage
                if self.hp <= 0 : return True
        return False

    def damaged(self, character4, frame_time):
        self.damage_time += frame_time

        if character4.attack_frame == 0:
            if self.damage_time > 1:
                self.damage_time = 0
                self.hp -= character4.damage
                if self.hp <= 0 : return True
        return False

    def get_bb(self):
        return self.x-70,self.y-70,self.x+70,self.y+140
    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def draw_die(self):
        self.die.clip_draw(self.die_frame *275 , 0,275, 220, self.x, 170)
    def draw_walk(self):
        self.walk.clip_draw(self.walk_frame *135 , 0, 135, 219, self.x, 170)
    def draw_attack(self):
        self.attack.clip_draw(self.attack_frame *185 , 0, 185, 217, self.x, 170)
    def draw_appear(self):
        self.appear.clip_draw(self.appear_frame *172 , 0, 172, 220, self.x, 170)

class Golem:

    PIXEL_PER_METER = (10.0 / 0.2)           # 10 pixel 20 cm
    RUN_SPEED_KMPH = 5.0                    # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 0.4
    ACTION_PER_TIME = 0.5 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 8

    now_state = "Appear"
    init_Start = 0

    def __init__(self):
        self.x=1400
        self.y=140
        self.hp=230
        self.damage_time = 0
        self.damage=20
        self.now_state = "Appear"

        self.die=load_image("resource\\enemy\\golem\\g_die.png")
        self.walk=load_image("resource\\enemy\\golem\\g_walk.png")
        self.attack=load_image("resource\\enemy\\golem\\g_attack.png")
        self.appear=load_image("resource\\enemy\\golem\\g_appear.png")

        self.start=1
        self.total_frames=0.0
        self.die_frame=0
        self.walk_frame=0
        self.attack_frame=0
        self.appear_frame=0
        self.init_Start = 0

    def Send_State(self):
        return self.now_state

    def Receive_State(self, now_state):
        self.now_state = now_state

    def Attack(self):
        return self.attack_frame


    def update(self,frame_time):
        distance = Golem.RUN_SPEED_PPS * frame_time
        self.total_frames += Golem.FRAMES_PER_ACTION * Golem.ACTION_PER_TIME * frame_time

        if self.now_state == "Appear":
            self.appear_frame = int(self.total_frames)%8
            if ( self.appear_frame == 7  and self.init_Start >= 2):
                self.now_state = "Walk"
            else:
                self.init_Start += 1

        if self.now_state == "Walk":
            self.start=1
            self.walk_frame = int(self.total_frames)%6
            self.x-=(self.start*distance)

        if self.now_state=="Attack":
            self.start=0
            self.attack_frame=int(self.total_frames)%6

        if self.now_state=="Die":
            self.die_frame==int(self.total_frames)%6

    def damaged(self, character1, frame_time):
        self.damage_time += frame_time

        if character1.attack_frame == 0:
            if self.damage_time > 1:
                self.damage_time = 0
                self.hp -= character1.damage
                if self.hp <= 0 : return True
        return False

    def damaged(self, character2, frame_time):
        self.damage_time += frame_time

        if character2.attack_frame == 0:
            if self.damage_time > 1:
                self.damage_time = 0
                self.hp -= character2.damage
                if self.hp <= 0 : return True
        return False

    def damaged(self, character3, frame_time):
        self.damage_time += frame_time

        if character3.attack_frame == 0:
            if self.damage_time > 1:
                self.damage_time = 0
                self.hp -= character3.damage
                if self.hp <= 0 : return True
        return False

    def damaged(self, character4, frame_time):
        self.damage_time += frame_time

        if character4.attack_frame == 0:
            if self.damage_time > 1:
                self.damage_time = 0
                self.hp -= character4.damage
                if self.hp <= 0 : return True
        return False

    def get_bb(self):
        return self.x-130,self.y-80,self.x+120,self.y+160
    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def draw_die(self):
        self.die.clip_draw(self.die_frame *300 , 0,300, 331, self.x, 190)
    def draw_walk(self):
        self.walk.clip_draw(self.walk_frame *320 , 0, 320, 245, self.x, 190)
    def draw_attack(self):
        self.attack.clip_draw(self.attack_frame *350 , 0, 350, 247, self.x, 190)
    def draw_appear(self):
        self.appear.clip_draw(self.appear_frame *322 , 0, 332, 246, self.x, 190)


