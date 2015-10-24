import random
import json
import os
os.chdir('C:\\Temp\\2DGP\\hbhdy')

from enemy import *
from team import *

from pico2d import *

import game_framework
import start_state

name = "MainState"


background=None

class Background:
    def __init__(self):
        self.image=load_image('background.png')
        pass#
    def draw(self):
        self.image.draw_to_origin(0,0,1600,800)
        pass





def enter():
    global background
    global zombie,vampire,skeleton,golem
    global ch1,ch2,ch3,ch4
    background = Background()
    zombie = Zombie()
    vampire = Vampire()
    skeleton=Skeleton()
    golem=Golem()
    ch1=Ch1()
    ch2=Ch2()
    ch3=Ch3()
    ch4=Ch4()
    pass


def exit():
    global background
    del(background)
    pass

def pause():
    pass


def resume():
    pass

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT or event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                game_framework.change_state(start_state)



def update():
    zombie.update()
    vampire.update()
    skeleton.update()
    golem.update()
    ch1.update()
    ch2.update()
    ch3.update()
    ch4.update()
    pass


def draw():

    clear_canvas()
    background.draw()
    zombie.draw()
    vampire.draw()
    skeleton.draw()
    golem.draw()
    ch1.draw()
    ch2.draw()
    ch3.draw()
    ch4.draw()

    update_canvas()
    delay(0.08)
    pass



