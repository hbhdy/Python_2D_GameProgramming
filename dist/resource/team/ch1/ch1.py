from pico2d import *

gRunning = True

def handle_events():
    global x
    global gRunning
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            gRunning = False


class DieImage:
    def __init__(self):
        self.image = load_image("die.png")
        self.frame1=0
    def update(self):
        self.frame1=(self.frame1+1)%7
    def Draw(self):
        self.image.clip_draw(self.frame1 *384 , 0,384, 384, 200, 240)

class WalkImage:
    def __init__(self):
        self.x, self.y = 200,600
        self.frame2=0
        self.image = load_image("walk.png")
    def update(self):
        self.frame2 = (self.frame2+1)%8
        self.x +=10
    def Draw(self):
        self.image.clip_draw(self.frame2 *288 , 0,  288, 288, self.x, self.y)

class AttackImage:
    def __init__(self):
        self.image = load_image("attack.png")
        self.frame3=0
    def update(self):
        self.frame3=(self.frame3+1)%5
    def Draw(self):
        self.image.clip_draw(self.frame3 *288 , 0, 288, 288, 600, 200)






def main():
    open_canvas(1600,800)
    dieImage = DieImage()
    walkImage = WalkImage()
    attackImage=AttackImage()

    while gRunning:
        clear_canvas()

        walkImage.update()
        dieImage.update()
        attackImage.update()

        dieImage.Draw()
        walkImage.Draw()
        attackImage.Draw()

        update_canvas()
        handle_events()
        delay(0.10)

    close_canvas()



if __name__ == '__main__':
    main()