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

enemy1_index = 0
enemy2_index = 0
enemy3_index = 0
enemy4_index = 0
team_index = 0

zombie_StartTime =0
vampire_StartTime =0
skeleton_StartTime =0
golem_StartTime =0
zombie_EndTime =0
vampire_EndTime =0
skeleton_EndTime =0
golem_EndTime =0

Zombie_State= "Walk"
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
    global enemy1_index,enemy2_index,enemy3_index,enemy4_index
    global character1,character2,character3,character4
    global characterUI
    global character_create1
    global character_create2
    global character_create3
    global character_create4
    global zombie_StartTime,vampire_StartTime,skeleton_StartTime,golem_StartTime

    character_create1=[]
    character_create2=[]
    character_create3=[]
    character_create4=[]
    character1=Character1()
    character2=Character2()
    character3=Character3()
    character4=Character4()
    background = Background()

    zombie=[]
    zombie.append(Zombie())
    vampire=[]
    vampire.append(Vampire())
    skeleton=[]
    skeleton.append(Skeleton())
    golem=[]
    golem.append(Golem())

    zombie_StartTime =0
    vampire_StartTime =0
    skeleton_StartTime =0
    golem_StartTime =0
    enemy1_index = 0
    enemy2_index = 0
    enemy3_index = 0
    enemy4_index = 0

    zombie_StartTime = time.time()
    vampire_StartTime = time.time()
    skeleton_StartTime = time.time()
    golem_StartTime = time.time()


    characterUI=load_image('UI\\characterUI.png')



def monster_create_Time():
    global zombie_StartTime,vampire_StartTime,skeleton_StartTime,golem_StartTime
    global zombie_EndTime,vampire_EndTime,skeleton_EndTime,golem_EndTime
    global zombie,vampire,skeleton,golem
    global enemy1_index,enemy2_index,enemy3_index,enemy4_index

    zombie_EndTime = time.time()
    vampire_EndTime = time.time()
    skeleton_EndTime = time.time()
    golem_EndTime = time.time()

    zombie_checktime = int(zombie_EndTime - zombie_StartTime)
    if( int(zombie_EndTime - zombie_StartTime) == 2 ):
        zombie.append(Zombie())
        enemy1_index += 1
        zombie_StartTime = time.time()
    vampire_checktime = int(vampire_EndTime - vampire_StartTime)
    if( int(vampire_EndTime - vampire_StartTime) == 20):
        vampire.append(Vampire())
        enemy2_index+=1
        vampire_StartTime = time.time()
    skeleton_checktime = int(skeleton_EndTime - skeleton_StartTime)
    if( int(skeleton_EndTime - skeleton_StartTime) == 25 ):
        skeleton.append(Zombie())
        enemy3_index += 1
        skeleton_StartTime = time.time()
    golem_checktime = int(golem_EndTime - golem_StartTime)
    if( int(golem_EndTime - golem_StartTime) == 30 ):
        golem.append(Zombie())
        enemy4_index += 1
        golem_StartTime = time.time()
    print(enemy1_index)

def exit():
    global background,characterU
    global character1,character2,character3,character4
    global zombie,vampire,golem,skeleton
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

def collide(a, b):
    left_a,bottom_a,right_a,top_a=a.get_bb()
    left_b,bottom_b,right_b,top_b=b.get_bb()

    if left_a>right_b : return False
    if right_a<left_b : return False
    if top_a< bottom_b : return False
    if bottom_a>top_b : return False

    return True

def update(frame_time):
    global enemy1_index,enemy2_index,enemy3_index,enemy4_index
    global Zombie_State,Vampire_State,Skeleton_State,Golem_State

    for x in range(0,enemy1_index):
        zombie[x].update(frame_time)
        # Zombie_State = Zombie.Send_State()
    for y in range(0,enemy2_index):
        vampire[y].update(frame_time)
        # Vampire_State = vampire[y].Send_State()
        # Vampire_State = Vampire.Send_State()
    for w in range(0,enemy3_index):
        # Skeleton_State = Skeleton.Send_State()
        skeleton[w].update(frame_time)
    for z in range(0,enemy4_index):
        # Golem_State = Golem.Send_State()
        golem[z].update(frame_time)

    character1.update(frame_time)
    character2.update(frame_time)
    character3.update(frame_time)
    character4.update(frame_time)

    # for characters2 in character2:
    #     for zombies in zombie.append():
    #         if collide(zombies,characters2):
    #             characters2.collide=True
    #             zombies.collide=True


    monster_create_Time()
    pass


def draw(frame_time):
    global enemy1_index,enemy2_index,enemy3_index,enemy4_index
    global Zombie_State,Vampire_State,Skeleton_State,Golem_State

    clear_canvas()
    background.draw()
    characterUI.draw(250,735)

    for x in range(0,enemy1_index):
        if Zombie_State=="Appear":
            zombie[x].draw_appear()
        if Zombie_State=="Walk":
            zombie[x].draw_walk()
    for y in range(0,enemy2_index):
        if Vampire_State == "Appear":
            vampire[y].draw_appear()
        if Vampire_State == "Walk":
            vampire[y].draw_walk()
    for w in range(0,enemy3_index):
        if Skeleton_State=="Appear":
            skeleton[w].draw_appear()
        if Skeleton_State=="Walk":
            skeleton[w].draw_walk()
    for z in range(0,enemy4_index):
        if Golem_State=="Appear":
            golem[z].draw_appear()
        if Golem_State=="Walk":
            golem[z].draw_walk()

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



