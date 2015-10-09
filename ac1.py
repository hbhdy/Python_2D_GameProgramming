import os
os.chdir('c:\\temp\\2DGP\\hbhdy\\resource')
from pico2d import *

gRunning = True

def handle_events():
    global gRunning
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            gRunning = False

class DrawImage:
    def __init__(self):
        self.image = load_image("ch1\\죽음1.png")
    def Draw(self, Num):
        self.image.clip_draw(Num *325 , 0, 325, 214, 400, 280)
    pass

class Background:
    def __init__(self):
        self.image = load_image("background\\background.png")
    def Draw(self):
        self.image.draw_to_origin(0,0,1600,800)
    pass

def main():
    frame = 0
    open_canvas(1600,800)
    drawImage = DrawImage()
    background = Background()

    while(gRunning):
        clear_canvas()


        background.Draw()
        drawImage.Draw(frame)
        frame += 1
        if frame >=8:
            frame = 0
        update_canvas()
        handle_events()
        delay(0.5)

    close_canvas()




if __name__ == '__main__':
    main()

