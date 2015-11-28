from pico2d import *

import game_framework


enemy_gate=None
team_gate=None

class Enemy_gate:
    def __init__(self):
        self.enemy_gate=load_image('resource\\enemy_gate.png')
        self.x=1495
        self.y=140
        self.hp=2000
        self.damage_time = 0

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x-70,self.y-70,self.x+70,self.y+140

    def draw(self):
        self.enemy_gate.clip_draw(0, 0, 230, 170,self.x, 150)


class Team_gate:
    def __init__(self):
        self.team_gate=load_image('resource\\team_gate.png')
        self.x=100
        self.y=140
        self.hp=100
        self.damage_time = 0

    def update(self,frame_time):
        pass

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x-100,self.y-75,self.x+100,self.y+140

    def draw(self):
        self.team_gate.clip_draw(0, 0, 230, 240,self.x, 185)

    def damaged(self, zombie, frame_time):
        self.damage_time += frame_time

        if zombie.attack_frame == 0:
            if self.damage_time > 0.1:
                self.damage_time = 0
                self.hp -= zombie.damage
                if self.hp <= 0 : return True
        return False
