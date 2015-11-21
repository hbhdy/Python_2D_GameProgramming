import game_framework
import main_state
from pico2d import *


name = "TitleState1"
image = None
bgm=None



def enter():
    global image,bgm
    image=load_image('title_state1.png')
    bgm=load_music('sound/title_BGM.mp3')
    bgm.set_volume(64)
    bgm.play(1)



def exit():
    global image,bgm
    del(image)
    del(bgm)


def update(frame_time):
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