import random
import json
import time


from enemy import *
from team import *

from pico2d import *

import game_framework

name = "MainState"

background=None
bgm=None

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


Zombie_State= []
Vampire_State=[]
Skeleton_State=[]
Golem_State=[]

character1_State = "Walk"
character2_State="Walk"
character3_State="Walk"
character4_State="Walk"




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
    global bgm


    bgm=load_music('sound/main_BGM.mp3')
    bgm.set_volume(64)
    bgm.repeat_play()



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
    Zombie_State=[]
    zombie.append(Zombie())
    Zombie_State.append("Appear")
    vampire=[]
    Vampire_State=[]
    vampire.append(Vampire())
    Vampire_State.append("Appear")
    skeleton=[]
    Skeleton_State=[]
    skeleton.append(Skeleton())
    Skeleton_State.append("Appear")
    golem=[]
    Golem_State=[]
    golem.append(Golem())
    Golem_State.append("Appear")

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

    # zombie_checktime = int(zombie_EndTime - zombie_StartTime)
    if( int(zombie_EndTime - zombie_StartTime) == 2 ):
            zombie.append(Zombie())
            Zombie_State.append("Appear")
            enemy1_index += 1
            zombie_StartTime = time.time()
    # vampire_checktime = int(vampire_EndTime - vampire_StartTime)
    if( int(vampire_EndTime - vampire_StartTime) == 10):
            vampire.append(Vampire())
            Vampire_State.append("Appear")
            enemy2_index+=1
            vampire_StartTime = time.time()
    # skeleton_checktime = int(skeleton_EndTime - skeleton_StartTime)
    if( int(skeleton_EndTime - skeleton_StartTime) == 20 ):
             skeleton.append(Skeleton())
             Skeleton_State.append("Appear")
             enemy3_index += 1
             skeleton_StartTime = time.time()
    # golem_checktime = int(golem_EndTime - golem_StartTime)
    if( int(golem_EndTime - golem_StartTime) == 30 ):
            golem.append(Golem())
            Golem_State.append("Appear")
            enemy4_index += 1
            golem_StartTime = time.time()

    # print(enemy1_index)

def exit():
    global background,characterUI
    global character1,character2,character3,character4
    global zombie,vampire,golem,skeleton,bgm

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
    del(bgm)

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
            character_create2.append(character2)


    if 260<mouse_x<360 and 20<mouse_y<120:
        character3=Character3()
        if len(character_create3)<50:
            character_create3.append(character3)


    if 380<mouse_x<470 and 20<mouse_y<120:
        character4=Character4()
        if len(character_create4)<50:
            character_create4.append(character4)



def handle_events(frame_time):
    global mouse_x,mouse_y
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT or event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        elif event.type == SDL_MOUSEMOTION:
            mouse_x,mouse_y = event.x,event.y
        elif (event.type, event.button) == (SDL_MOUSEBUTTONDOWN, SDL_BUTTON_LEFT):
             mouse_click()



def update(frame_time):
    global enemy1_index,enemy2_index,enemy3_index,enemy4_index
    global Zombie_State,Vampire_State,Skeleton_State,Golem_State
    global character1_State,character2_State,character3_State,character4_State

    for x in range(0,enemy1_index):
        zombie[x].update(frame_time)
        Zombie_State[x] = zombie[x].Send_State()
    for y in range(0,enemy2_index):
        vampire[y].update(frame_time)
        Vampire_State[y] = vampire[y].Send_State()
    for w in range(0,enemy3_index):
        skeleton[w].update(frame_time)
        Skeleton_State[w] = skeleton[w].Send_State()
    for z in range(0,enemy4_index):
        golem[z].update(frame_time)
        Golem_State[z] = golem[z].Send_State()

    character1.update(frame_time)
    character2.update(frame_time)
    character3.update(frame_time)
    character4.update(frame_time)

    if (enemy1_index>=1):
        for x in range(0,enemy1_index):
            if collide(character1,zombie[x]):
                zombie[x].Receive_State("Attack")
                character1_State="Attack"
                character1.Receive_State(character1_State)
                if character1.damaged(zombie[x], frame_time) == True :
                        len[character_create1].remove(character1)
                elif zombie[x].damaged(character1, frame_time) == True :
                       enemy1_index.remove(zombie[x])
            if collide(character2,zombie[x]):
                zombie[x].Receive_State("Attack")
                character2_State="Attack"
                character2.Receive_State(character2_State)
            if collide(character3,zombie[x]):
                zombie[x].Receive_State("Attack")
                character3_State="Attack"
                character3.Receive_State(character3_State)
            if collide(character4,zombie[x]):
                zombie[x].Receive_State("Attack")
                character4_State="Attack"
                character4.Receive_State(character4_State)
    if (enemy2_index>=1):
        for y in range(0,enemy2_index):
             if collide(character1,vampire[y]):
                 vampire[y].Receive_State("Attack")
                 character1_State="Attack"
                 character1.Receive_State(character1_State)
             if collide(character2,vampire[y]):
                 vampire[y].Receive_State("Attack")
                 character2_State="Attack"
                 character2.Receive_State(character2_State)
             if collide(character3,vampire[y]):
                 vampire[y].Receive_State("Attack")
                 character3_State="Attack"
                 character3.Receive_State(character3_State)
             if collide(character4,vampire[y]):
                 vampire[y].Receive_State("Attack")
                 character4_State="Attack"
                 character4.Receive_State(character4_State)
    if (enemy3_index>=1):
        for w in range(0,enemy3_index):
            if collide(character1,skeleton[w]):
                skeleton[w].Receive_State("Attack")
                character1_State="Attack"
                character1.Receive_State(character1_State)
            if collide(character2,skeleton[w]):
                skeleton[w].Receive_State("Attack")
                character2_State="Attack"
                character2.Receive_State(character2_State)
            if collide(character3,skeleton[w]):
                skeleton[w].Receive_State("Attack")
                character3_State="Attack"
                character3.Receive_State(character3_State)
            if collide(character4,skeleton[w]):
                skeleton[w].Receive_State("Attack")
                character4_State="Attack"
                character4.Receive_State(character4_State)
    if (enemy4_index>=1):
        for z in range(0,enemy4_index):
            if collide(character1,golem[z]):
                golem[z].Receive_State("Attack")
                character1_State="Attack"
                character1.Receive_State(character1_State)
            if collide(character2,golem[z]):
                golem[z].Receive_State("Attack")
                character2_State="Attack"
                character2.Receive_State(character2_State)
            if collide(character3,golem[z]):
                golem[z].Receive_State("Attack")
                character3_State="Attack"
                character3.Receive_State(character3_State)
            if collide(character4,golem[z]):
                golem[z].Receive_State("Attack")
                character4_State="Attack"
                character4.Receive_State(character4_State)

    monster_create_Time()



def draw(frame_time):
    global enemy1_index,enemy2_index,enemy3_index,enemy4_index
    global Zombie_State,Vampire_State,Skeleton_State,Golem_State

    clear_canvas()
    background.draw()
    characterUI.draw(250,735)

    for x in range(0,enemy1_index):
        if Zombie_State[x]=="Appear":
            zombie[x].draw_appear()
        if Zombie_State[x]=="Walk":
            zombie[x].draw_walk()
            zombie[x].draw_bb()
        if Zombie_State[x]=="Attack":
            zombie[x].draw_attack()
    for y in range(0,enemy2_index):
        if Vampire_State[y] == "Appear":
            vampire[y].draw_appear()
        if Vampire_State[y] == "Walk":
            vampire[y].draw_walk()
            vampire[y].draw_bb()
        if Vampire_State[y]=="Attack":
            vampire[y].draw_attack()
    for w in range(0,enemy3_index):
        if Skeleton_State[w]=="Appear":
            skeleton[w].draw_appear()
        if Skeleton_State[w]=="Walk":
            skeleton[w].draw_walk()
            skeleton[w].draw_bb()
        if Skeleton_State[w]=="Attack":
            skeleton[w].draw_attack()
    for z in range(0,enemy4_index):
        if Golem_State[z]=="Appear":
            golem[z].draw_appear()
        if Golem_State[z]=="Walk":
            golem[z].draw_walk()
            golem[z].draw_bb()
        if Golem_State[z]=="Attack":
            golem[z].draw_attack()


    for character1 in character_create1:
         character1.update(frame_time)
         if character1_State == "Walk":
            character1.draw_walk()
         if character1_State == "Attack":
            character1.draw_attack()
         character1.draw_bb()
    for character2 in character_create2:
        character2.update(frame_time)
        if character2_State == "Walk":
            character2.draw_walk()
        if character2_State == "Attack":
            character2.draw_attack()
        character2.draw_bb()
    for character3 in character_create3:
        character3.update(frame_time)
        if character3_State == "Walk":
            character3.draw_walk()
        if character3_State == "Attack":
            character3.draw_attack()
        character3.draw_bb()
    for character4 in character_create4:
        character4.update(frame_time)
        if character4_State == "Walk":
            character4.draw_walk()
        if character4_State == "Attack":
            character4.draw_attack()
        character4.draw_bb()

    update_canvas()

def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()
    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False
    return True



