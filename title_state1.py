import game_framework
import main_state
from pico2d import *


name = "TitleState1"
image = None


def enter():
    global image
    image=load_image('title_state1.png')



def exit():
    global image
    del(image)


def update(frame_time):
    # global logo_time
    # logo_time+=frame_time
    # if(logo_time>1.0):
    #     logo_time=0
    #     game_framework.quit()
    #     game_framework.change_state(main_state)
    pass



def draw(frame_time):
    global image
    clear_canvas()
    image.draw_to_origin(0,0,1600,800)

    update_canvas()




def handle_events(frame_time):
    global mouse_x,mouse_y
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            # elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
            #     game_framework.change_state(main_state)
            elif event.type == SDL_MOUSEMOTION:
                mouse_x,mouse_y = event.x,800-event.y
            elif (event.type, event.button) == (SDL_MOUSEBUTTONDOWN, SDL_BUTTON_LEFT):
                if 600<mouse_x<800 and 265<mouse_y<380:
                     game_framework.change_state(main_state)
                if 600<mouse_x<800 and 135<mouse_y<250:
                    game_framework.quit()







def pause(): pass


def resume(): pass