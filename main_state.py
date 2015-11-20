import random
import json
import time


from enemy import *
from team import *

from pico2d import *

import game_framework
import start_state

name = "MainState"

background=None

enemy_index = 0
team_index=0
GameStart_Time = 0
GameEnd_Time = 0

Zombie_State= "Appear"
Vampire_State = "Appear"
Skeleton_State="Appear"
Golem_State="Appear"



class Background:
    def __init__(self):
        self.image=load_image('background.png')

    def draw(self):
        self.image.draw_to_origin(0,0,1600,800)




def enter():
    global background
    global zombie,vampire,skeleton,golem
    global GameStart_Time,enemy_index
    global character1,character2,character3,character4
    global characterUI
    global character_create1
    global character_create2
    global character_create3
    global character_create4


    character_create1=[]
    character_create2=[]
    character_create3=[]
    character_create4=[]
    background = Background()

    zombie=[]
    zombie.append(Zombie())
    vampire=[]
    vampire.append(Vampire())
    skeleton=[]
    skeleton.append(Skeleton())
    golem=[]
    golem.append(Golem())

    enemy_index = 0
    GameStart_Time = 0
    GameStart_Time = time.time()
    character1=Character1()
    character2=Character2()
    character3=Character3()
    character4=Character4()

    characterUI=load_image('UI\\characterUI.png')



def monster_create_Time():
    global GameStart_Time, GameEnd_Time, enemy_index
    global zombie,vampire,skeleton,golem
    GameEnd_Time = time.time()
    temp_Time = int(GameEnd_Time - GameStart_Time)
    if( int(GameEnd_Time - GameStart_Time) == 7 ):
        zombie.append(Golem())
        enemy_index += 1
        GameStart_Time = time.time()
    if(int(GameEnd_Time-GameStart_Time)==13):
        vampire.append(Vampire())
        enemy_index+=1
        GameStart_Time=present.time()
        print(temp_Time)
        print(enemy_index)

def exit():
    global background,characterU
    global character1,character2,character3,character4
    global vampire,golem,skeleton
    del(characterUI)
    del(background)
    del(character1)
    del(character2)
    del(character3)
    del(character4)
    del(zombie)
    del(skeleton)
    del(vampire)
    del(golem)

def pause():
    pass


def resume():
    pass

def mouse_click():
    global character1,character2,character3,character4
    if 20<mouse_x<120 and 20<mouse_y<120:
        character1=Character1()
        if len(character_create1)<50:
            character_create1.append(character1)


    if 140<mouse_x<230 and 20 <mouse_y<120:
        character2=Character2()
        if len(character_create2)<50:
            character_create1.append(character2)


    if 260<mouse_x<360 and 20<mouse_y<120:
        character3=Character3()
        if len(character_create3)<50:
            character_create2.append(character3)


    if 380<mouse_x<470 and 20<mouse_y<120:
        character4=Character4()
        if len(character_create4)<50:
            character_create3.append(character4)



def handle_events(frame_time):
    global mouse_x,mouse_y
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT or event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                game_framework.change_state(start_state)
        elif event.type == SDL_MOUSEMOTION:
            mouse_x,mouse_y = event.x,event.y
        elif (event.type, event.button) == (SDL_MOUSEBUTTONDOWN, SDL_BUTTON_LEFT):
             mouse_click()



def update(frame_time):
    global enemy_index, Vampire_State

    zombie.update(frame_time)
    vampire.update(frame_time)
    Vampire_State = vampire.Send_State()

    skeleton.update()
    for i in range(0,enemy_index):
        golem[i].update(frame_time)
    character1.update(frame_time)
    character2.update(frame_time)
    character3.update(frame_time)
    character4.update(frame_time)
    monster_create_Time()
    delay(0.05)
    pass


def draw(frame_time):
    global enemy_index, Vampire_State

    clear_canvas()
    background.draw()
    characterUI.draw(250,735)

    # zombie.draw()
    if Vampire_State == "Appear":
        vampire.draw_appear()
    if Vampire_State == "Walk":
        vampire.draw_walk()



    skeleton.draw_appear()
    for i in range(0,enemy_index):
        if Golem_State=="Appear":
            golem[i].draw_appear()
        if Golem_State=="Walk":
            golem[i].draw_walk()

    for character1 in character_create1:
        character1.update(frame_time)
        character1.draw_walk()
    for character2 in character_create2:
        character2.update(frame_time)
        character2.draw_walk()
    for character3 in character_create3:
        character3.update(frame_time)
        character3.draw_walk()
    for character4 in character_create4:
        character4.update(frame_time)
        character4.draw_walk()


    update_canvas()
    pass



