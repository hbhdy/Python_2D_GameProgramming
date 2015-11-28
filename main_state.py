import random
import json
import time


from enemy import *
from team import *
from gate import *

from pico2d import *

import game_framework

name = "MainState"

background=None
bgm=None

character1_index=0
character2_index=0
character3_index=0
character4_index=0

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

Character1_State=[]
Character2_State=[]
Character3_State=[]
Character4_State=[]




class Background:
    def __init__(self):
        self.image=load_image('background.png')

    def draw(self):
        self.image.draw_to_origin(0,0,1600,800)

def enter():
    global background
    global zombie,vampire,skeleton,golem
    global enemy1_index,enemy2_index,enemy3_index,enemy4_index
    global character1_index,character2_index,character3_index,character4_index
    global character1,character2,character3,character4
    global characterUI
    global zombie_StartTime,vampire_StartTime,skeleton_StartTime,golem_StartTime
    global bgm,enemy_gate,team_gate


    bgm=load_music('sound/main_BGM.mp3')
    bgm.set_volume(64)
    bgm.repeat_play()

    enemy_gate=Enemy_gate()
    team_gate=Team_gate()

    background = Background()

    character1 = []
    Character1_State = []
    character1.append(Character1())
    Character1_State.append("Walk")
    character2=[]
    Character2._State=[]
    character2.append(Character2())
    Character2_State.append("Walk")
    character3=[]
    Character3_State=[]
    character3.append(Character3())
    Character3_State.append("Walk")
    character4=[]
    Character4_State=[]
    character4.append(Character4())
    Character4_State.append("Walk")


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
    character1_index=0
    character2_index=0
    character3_index=0
    character4_index=0

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
    if( int(zombie_EndTime - zombie_StartTime) == 5 ):
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
    global enemy_gate,team_gate

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
    del(enemy_gate)
    del(team_gate)

def pause():
    pass


def resume():
    pass

def mouse_click():
    global character1,character2,character3,character4
    global character1_index,character2_index,character3_index,character4_index

    if 20<mouse_x<120 and 20<mouse_y<120:
        character1.append(Character1())
        Character1_State.append("Walk")
        character1_index += 1

    if 140<mouse_x<230 and 20 <mouse_y<120:
        character2.append(Character2())
        Character2_State.append("Walk")
        character2_index += 1


    if 260<mouse_x<360 and 20<mouse_y<120:
        character3.append(Character3())
        Character3_State.append("Walk")
        character3_index += 1


    if 380<mouse_x<470 and 20<mouse_y<120:
        character4.append(Character4())
        Character4_State.append("Walk")
        character4_index += 1



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
    global character1_index,character2_index,character3_index,character4_index
    global Zombie_State,Vampire_State,Skeleton_State,Golem_State
    global Character1_Statea,Character2_Statea,Character3_Statea,Character4_Statea
    global Character1_State,Character2_State,Character3_State,Character4_State
    global team_gate

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

    for a in range(0, character1_index):
        character1[a].update(frame_time)
        Character1_State[a] = character1[a].Send_State()
    for b in range(0, character2_index):
        character2[b].update(frame_time)
        Character2_State[b] = character2[b].Send_State()
    for c in range(0, character3_index):
        character3[c].update(frame_time)
        Character3_State[c] = character3[c].Send_State()
    for d in range(0, character4_index):
        character4[d].update(frame_time)
        Character4_State[d] = character4[d].Send_State()


    if (enemy1_index>=1):
        for x in range(0,enemy1_index):
            for a in range(0,character1_index):
               if collide(character1[a],zombie[x])==True:
                    zombie[x].Receive_State("Attack")
                    Character1_Statea = "Attack"
                    character1[a].Receive_State(str(Character1_Statea))
                    if character1[a].damaged(zombie[x], frame_time) == True :
                        character1.pop(a)
                        Character1_State.pop(a)
                        character1_index -= 1
                        zombie[x].Receive_State("Walk")
                    elif zombie[x].damaged(character1[a], frame_time) == True :
                        zombie.pop(x)
                        Zombie_State.pop(x)
                        enemy1_index-=1
                        Character1_Statea = "Walk"
                        character1[a].Receive_State(str(Character1_Statea))
               elif collide(character1[a],zombie[x])==False:
                      zombie[x].Receive_State("Walk")
                      Character1_Statea = "Walk"
                      character1[a].Receive_State(str(Character1_Statea))
            for b in range(0,character2_index):
               if collide(character2[b],zombie[x])==True:
                    zombie[x].Receive_State("Attack")
                    Character2_Statea = "Attack"
                    character2[b].Receive_State(str(Character2_Statea))
                    if character2[b].damaged(zombie[x], frame_time) == True :
                        character2.pop(b)
                        Character2_State.pop(b)
                        character2_index -= 1
                        zombie[x].Receive_State("Walk")
                    elif zombie[x].damaged(character2[b], frame_time) == True :
                        zombie.pop(x)
                        Zombie_State.pop(x)
                        enemy1_index-=1
                        Character2_Statea = "Walk"
                        character2[b].Receive_State(str(Character2_Statea))
               elif collide(character2[b],zombie[x])==False:
                    zombie[x].Receive_State("Walk")
                    Character2_Statea = "Walk"
                    character2[b].Receive_State(str(Character2_Statea))
            for c in range(0,character3_index):
               if collide(character3[c],zombie[x])==True:
                    zombie[x].Receive_State("Attack")
                    Character3_Statea = "Attack"
                    character3[c].Receive_State(str(Character3_Statea))
                    if character3[c].damaged(zombie[x], frame_time) == True :
                        character3.pop(c)
                        Character3_State.pop(c)
                        character3_index -= 1
                        zombie[x].Receive_State("Walk")
                    elif zombie[x].damaged(character3[c], frame_time) == True :
                        zombie.pop(x)
                        Zombie_State.pop(x)
                        enemy1_index-=1
                        Character3_Statea = "Walk"
                        character3[c].Receive_State(str(Character3_Statea))
               elif collide(character3[c],zombie[x])==False:
                    zombie[x].Receive_State("Walk")
                    Character3_Statea = "Walk"
                    character3[c].Receive_State(str(Character3_Statea))
            for d in range(0,character4_index):
               if collide(character4[d],zombie[x])==True:
                    zombie[x].Receive_State("Attack")
                    Character4_Statea = "Attack"
                    character4[d].Receive_State(str(Character4_Statea))
                    if character4[d].damaged(zombie[x], frame_time) == True :
                        character4.pop(d)
                        Character4_State.pop(d)
                        character4_index -= 1
                        zombie[x].Receive_State("Walk")
                    elif zombie[x].damaged(character4[d], frame_time) == True :
                        zombie.pop(x)
                        Zombie_State.pop(x)
                        enemy1_index-=1
                        Character4_Statea = "Walk"
                        character4[d].Receive_State(str(Character4_Statea))
               elif collide(character4[d],zombie[x])==False:
                    zombie[x].Receive_State("Walk")
                    Character4_Statea = "Walk"
                    character4[d].Receive_State(str(Character4_Statea))

    if (enemy2_index>=1):
        for y in range(0,enemy2_index):
            for a in range(0,character1_index):
               if collide(character1[a],vampire[y])==True:
                    vampire[y].Receive_State("Attack")
                    Character1_Statea = "Attack"
                    character1[a].Receive_State(str(Character1_Statea))
                    if character1[a].damaged(vampire[y], frame_time) == True :
                        character1.pop(a)
                        Character1_State.pop(a)
                        character1_index -= 1
                        vampire[y].Receive_State("Walk")
                    elif vampire[y].damaged(character1[a], frame_time) == True :
                        vampire.pop(y)
                        Vampire_State.pop(y)
                        enemy2_index-=1
                        Character1_Statea = "Walk"
                        character1[a].Receive_State(str(Character1_Statea))
               elif collide(character1[a],vampire[y])==False:
                    vampire[y].Receive_State("Walk")
                    Character1_Statea = "Walk"
                    character1[a].Receive_State(str(Character1_Statea))
            for b in range(0,character2_index):
               if collide(character2[b],vampire[y])==True:
                    vampire[y].Receive_State("Attack")
                    Character2_Statea = "Attack"
                    character2[b].Receive_State(str(Character2_Statea))
                    if character2[b].damaged(vampire[y], frame_time) == True :
                        character2.pop(b)
                        Character2_State.pop(b)
                        character2_index -= 1
                        vampire[y].Receive_State("Walk")
                    elif vampire[y].damaged(character2[b], frame_time) == True :
                        vampire.pop(y)
                        Vampire_State.pop(y)
                        enemy2_index-=1
                        Character2_Statea = "Walk"
                        character2[b].Receive_State(str(Character2_Statea))
               elif collide(character2[b],vampire[y])==False:
                    vampire[y].Receive_State("Walk")
                    Character2_Statea = "Walk"
                    character2[b].Receive_State(str(Character2_Statea))
            for c in range(0,character3_index):
               if collide(character3[c],vampire[y])==True:
                    vampire[y].Receive_State("Attack")
                    Character3_Statea = "Attack"
                    character3[c].Receive_State(str(Character3_Statea))
                    if character3[c].damaged(vampire[y], frame_time) == True :
                        character3.pop(c)
                        Character3_State.pop(c)
                        character3_index -= 1
                        vampire[y].Receive_State("Walk")
                    elif vampire[y].damaged(character3[c], frame_time) == True :
                        vampire.pop(y)
                        Vampire_State.pop(y)
                        enemy2_index-=1
                        Character3_Statea = "Walk"
                        character3[c].Receive_State(str(Character3_Statea))
               elif collide(character3[c],vampire[y])==False:
                    vampire[y].Receive_State("Walk")
                    Character3_Statea = "Walk"
                    character3[c].Receive_State(str(Character3_Statea))
            for d in range(0,character4_index):
               if collide(character4[d],vampire[y])==True:
                    vampire[y].Receive_State("Attack")
                    Character4_Statea = "Attack"
                    character4[d].Receive_State(str(Character4_Statea))
                    if character4[d].damaged(vampire[y], frame_time) == True :
                        character4.pop(d)
                        Character4_State.pop(d)
                        character4_index -= 1
                        vampire[y].Receive_State("Walk")
                    elif vampire[y].damaged(character4[d], frame_time) == True :
                        vampire.pop(y)
                        Vampire_State.pop(y)
                        enemy2_index-=1
                        Character4_Statea = "Walk"
                        character4[d].Receive_State(str(Character4_Statea))
               elif collide(character4[d],vampire[y])==False:
                    vampire[y].Receive_State("Walk")
                    Character4_Statea = "Walk"
                    character4[d].Receive_State(str(Character4_Statea))
    if (enemy3_index>=1):
        for w in range(0,enemy3_index):
            for a in range(0,character1_index):
               if collide(character1[a],skeleton[w])==True:
                    skeleton[w].Receive_State("Attack")
                    Character1_Statea = "Attack"
                    character1[a].Receive_State(str(Character1_Statea))
                    if character1[a].damaged(skeleton[w], frame_time) == True :
                        character1.pop(a)
                        Character1_State.pop(a)
                        character1_index -= 1
                        skeleton[w].Receive_State("Walk")
                    elif skeleton[w].damaged(character1[a], frame_time) == True :
                        skeleton.pop(w)
                        Skeleton_State.pop(w)
                        enemy3_index-=1
                        Character1_Statea = "Walk"
                        character1[a].Receive_State(str(Character1_Statea))
               elif collide(character1[a],skeleton[w])==False:
                    skeleton[w].Receive_State("Walk")
                    Character1_Statea = "Walk"
                    character1[a].Receive_State(str(Character1_Statea))
            for b in range(0,character2_index):
               if collide(character2[b],skeleton[w])==True:
                    skeleton[w].Receive_State("Attack")
                    Character2_Statea = "Attack"
                    character2[b].Receive_State(str(Character2_Statea))
                    if character2[b].damaged(skeleton[w], frame_time) == True :
                        character2.pop(b)
                        Character2_State.pop(b)
                        character2_index -= 1
                        skeleton[w].Receive_State("Walk")
                    elif skeleton[w].damaged(character2[b], frame_time) == True :
                        skeleton.pop(w)
                        Skeleton_State.pop(w)
                        enemy3_index-=1
                        Character2_Statea = "Walk"
                        character2[b].Receive_State(str(Character2_Statea))
               elif collide(character2[b],skeleton[w])==False:
                    skeleton[w].Receive_State("Walk")
                    Character2_Statea = "Walk"
                    character2[b].Receive_State(str(Character2_Statea))
            for c in range(0,character3_index):
               if collide(character3[c],skeleton[w])==True:
                    skeleton[w].Receive_State("Attack")
                    Character3_Statea = "Attack"
                    character3[c].Receive_State(str(Character3_Statea))
                    if character3[c].damaged(skeleton[w], frame_time) == True :
                        character3.pop(c)
                        Character3_State.pop(c)
                        character3_index -= 1
                        skeleton[w].Receive_State("Walk")
                    elif skeleton[w].damaged(character3[c], frame_time) == True :
                        skeleton.pop(w)
                        Skeleton_State.pop(w)
                        enemy3_index-=1
                        Character3_Statea = "Walk"
                        character3[c].Receive_State(str(Character3_Statea))
               elif collide(character3[c],skeleton[w])==False:
                    skeleton[w].Receive_State("Walk")
                    Character3_Statea = "Walk"
                    character3[c].Receive_State(str(Character3_Statea))
            for d in range(0,character4_index):
               if collide(character4[d],skeleton[w])==True:
                    skeleton[w].Receive_State("Attack")
                    Character4_Statea = "Attack"
                    character4[d].Receive_State(str(Character4_Statea))
                    if character4[d].damaged(skeleton[w], frame_time) == True :
                        character4.pop(d)
                        Character4_State.pop(d)
                        character4_index -= 1
                        skeleton[w].Receive_State("Walk")
                    elif skeleton[w].damaged(character4[d], frame_time) == True :
                        skeleton.pop(w)
                        Skeleton_State.pop(w)
                        enemy3_index-=1
                        Character4_Statea = "Walk"
                        character4[d].Receive_State(str(Character4_Statea))
               elif collide(character4[d],skeleton[w])==False:
                    skeleton[w].Receive_State("Walk")
                    Character4_Statea = "Walk"
                    character4[d].Receive_State(str(Character4_Statea))
    if (enemy4_index>=1):
        for z in range(0,enemy4_index):
            for a in range(0,character1_index):
               if collide(character1[a],golem[z])==True:
                    golem[z].Receive_State("Attack")
                    Character1_Statea = "Attack"
                    character1[a].Receive_State(str(Character1_Statea))
                    if character1[a].damaged(golem[z], frame_time) == True :
                        character1.pop(a)
                        Character1_State.pop(a)
                        character1_index -= 1
                        golem[z].Receive_State("Walk")
                    elif golem[z].damaged(character1[a], frame_time) == True :
                        golem.pop(z)
                        Golem_State.pop(z)
                        enemy4_index-=1
                        Character1_Statea = "Walk"
                        character1[a].Receive_State(str(Character1_Statea))
               elif collide(character1[a],golem[z])==False:
                    golem[z].Receive_State("Walk")
                    Character1_Statea = "Walk"
                    character1[a].Receive_State(str(Character1_Statea))
            for b in range(0,character2_index):
               if collide(character2[b],golem[z])==True:
                    golem[z].Receive_State("Attack")
                    Character2_Statea = "Attack"
                    character2[b].Receive_State(str(Character2_Statea))
                    if character2[b].damaged(golem[z], frame_time) == True :
                        character2.pop(b)
                        Character2_State.pop(b)
                        character2_index -= 1
                        golem[z].Receive_State("Walk")
                    elif golem[z].damaged(character2[b], frame_time) == True :
                        golem.pop(z)
                        Golem_State.pop(z)
                        enemy4_index-=1
                        Character2_Statea = "Walk"
                        character2[b].Receive_State(str(Character2_Statea))
               elif collide(character2[b],golem[z])==False:
                    golem[z].Receive_State("Walk")
                    Character2_Statea = "Walk"
                    character2[b].Receive_State(str(Character2_Statea))
            for c in range(0,character3_index):
               if collide(character3[c],golem[z])==True:
                    golem[z].Receive_State("Attack")
                    Character3_Statea = "Attack"
                    character3[c].Receive_State(str(Character3_Statea))
                    if character3[c].damaged(golem[z], frame_time) == True :
                        character3.pop(c)
                        Character3_State.pop(c)
                        character3_index -= 1
                        golem[z].Receive_State("Walk")
                    elif golem[z].damaged(character3[c], frame_time) == True :
                        golem.pop(z)
                        Golem_State.pop(z)
                        enemy4_index-=1
                        Character3_Statea = "Walk"
                        character3[c].Receive_State(str(Character3_Statea))
               elif collide(character3[c],golem[z])==False:
                    golem[z].Receive_State("Walk")
                    Character3_Statea = "Walk"
                    character3[c].Receive_State(str(Character3_Statea))
            for d in range(0,character4_index):
               if collide(character4[d],golem[z])==True:
                    golem[z].Receive_State("Attack")
                    Character4_Statea = "Attack"
                    character4[d].Receive_State(str(Character4_Statea))
                    if character4[d].damaged(golem[z], frame_time) == True :
                        character4.pop(d)
                        Character4_State.pop(d)
                        character4_index -= 1
                        golem[z].Receive_State("Walk")
                    elif golem[z].damaged(character4[d], frame_time) == True :
                        golem.pop(z)
                        Golem_State.pop(z)
                        enemy4_index-=1
                        Character4_Statea = "Walk"
                        character4[d].Receive_State(str(Character4_Statea))
               elif collide(character4[d],golem[z])==False:
                    golem[z].Receive_State("Walk")
                    Character4_Statea = "Walk"
                    character4[d].Receive_State(str(Character4_Statea))
    for x in range(0,enemy1_index):
        if collide(team_gate,zombie[x]):
                    zombie[x].Receive_State("Attack")
                    if team_gate.damaged(zombie[x], frame_time) == True :
                        close_canvas()
    for y in range(0,enemy2_index):
        if collide(team_gate,vampire[y]):
                    vampire[y].Receive_State("Attack")
                    if team_gate.damaged(vampire[y], frame_time) == True :
                        close_canvas()
    for w in range(0,enemy3_index):
        if collide(team_gate,skeleton[w]):
                    skeleton[w].Receive_State("Attack")
                    if team_gate.damaged(skeleton[w], frame_time) == True :
                        close_canvas()
    for z in range(0,enemy4_index):
        if collide(team_gate,golem[z]):
                    golem[z].Receive_State("Attack")
                    if team_gate.damaged(golem[z], frame_time) == True :
                        close_canvas()
    for a in range(0,character1_index):
        if collide(enemy_gate,character1[a])==True:
                    Character1_Statea = "Attack"
                    character1[a].Receive_State(str(Character1_Statea))
                    if enemy_gate.damaged(character1[a], frame_time) == True :
                        close_canvas()
    for b in range(0,character2_index):
        if collide(enemy_gate,character2[b])==True:
                    Character2_Statea = "Attack"
                    character2[b].Receive_State(str(Character2_Statea))
                    if enemy_gate.damaged(character2[b], frame_time) == True :
                        close_canvas()
    for c in range(0,character3_index):
        if collide(enemy_gate,character3[c])==True:
                    Character3_Statea = "Attack"
                    character3[c].Receive_State(str(Character3_Statea))
                    if enemy_gate.damaged(character3[c], frame_time) == True :
                        close_canvas()
    for d in range(0,character4_index):
        if collide(enemy_gate,character4[d])==True:
                    Character4_Statea = "Attack"
                    character4[d].Receive_State(str(Character4_Statea))
                    if enemy_gate.damaged(character4[d], frame_time) == True :
                        close_canvas()





    monster_create_Time()

def draw(frame_time):
    global enemy1_index,enemy2_index,enemy3_index,enemy4_index
    global character1_index,character2_index,character3_index,character4_index
    global Zombie_State,Vampire_State,Skeleton_State,Golem_State

    clear_canvas()
    background.draw()
    characterUI.draw(250,735)
    enemy_gate.draw()
    enemy_gate.draw_bb()
    team_gate.draw()
    team_gate.draw_bb()

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


    for a in range(0,character1_index):
        if Character1_State[a]=="Walk":
            character1[a].draw_walk()
            character1[a].draw_bb()
        if Character1_State[a]=="Attack":
            character1[a].draw_attack()

    for b in range(0,character2_index):
        if Character2_State[b]=="Walk":
            character2[b].draw_walk()
            character2[b].draw_bb()
        if Character2_State[b]=="Attack":
            character2[b].draw_attack()

    for c in range(0,character3_index):
        if Character3_State[c]=="Walk":
            character3[c].draw_walk()
            character3[c].draw_bb()
        if Character3_State[c]=="Attack":
            character3[c].draw_attack()

    for d in range(0,character4_index):
        if Character4_State[d]=="Walk":
            character4[d].draw_walk()
            character4[d].draw_bb()
        if Character4_State[d]=="Attack":
            character4[d].draw_attack()

    update_canvas()

def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()
    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False
    return True



