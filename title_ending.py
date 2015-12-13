import game_framework
from pico2d import *


name = "TitleEnding"
image = None
bgm=None



def enter():
    global image,bgm
    image=load_image('title_ending.png')
    bgm=load_music('sound/end_BGM.mp3')
    bgm.set_volume(64)
    bgm.repeat_play()



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
            elif event.type == SDL_MOUSEMOTION:
                mouse_x,mouse_y = event.x,800-event.y
            elif (event.type, event.button) == (SDL_MOUSEBUTTONDOWN, SDL_BUTTON_LEFT):
                if 700<mouse_x<980 and 220<mouse_y<300:
                    game_framework.quit()






def pause(): pass


def resume(): pass