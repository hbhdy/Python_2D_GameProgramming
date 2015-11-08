import game_framework
import main_state
from pico2d import *


name = "StartState"
image = None
logo_time = 0.0


def enter():
    global image
    open_canvas(1600,800,sync=True)
    image=load_image('kpu_credit.png')



def exit():
    global image
    del(image)


def update(frame_time):
    global logo_time
    logo_time+=frame_time
    if(logo_time>1.0):
        logo_time=0
        #game_framework.quit()
        game_framework.change_state(main_state)




def draw(frame_time):
    global image
    clear_canvas()
    image.draw_to_origin(0,0,1600,800)

    update_canvas()





def handle_events(frame_time):
    events = get_events()



def pause(): pass


def resume(): pass