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
        self.frame1=(self.frame1+1)%6
    def Draw(self):
        self.image.clip_draw(self.frame1 *300 , 0,300, 331, 200, 240)

class WalkImage:
    def __init__(self):
        self.x, self.y = 1000,600
        self.frame2=0
        self.image = load_image("walk.png")
    def update(self):
        self.frame2 = (self.frame2+1)%6
        self.x -=10
    def Draw(self):
        self.image.clip_draw(self.frame2 *320 , 0, 320, 245, self.x, self.y)

class AttackImage:
    def __init__(self):
        self.image = load_image("attack.png")
        self.frame3=0
    def update(self):
        self.frame3=(self.frame3+1)%6
    def Draw(self):
        self.image.clip_draw(self.frame3 *350 , 0, 350, 247, 600, 200)

class AppearImage:
    def __init__(self):
        self.image = load_image("appear.png")
        self.frame4=0
    def update(self):
        self.frame4=(self.frame4+1)%8
    def Draw(self):
        self.image.clip_draw(self.frame4 *322 , 0, 332, 246, 1200, 200)







def main():
    open_canvas(1600,800)
    dieImage = DieImage()
    walkImage = WalkImage()
    attackImage=AttackImage()
    appearImage=AppearImage()

    while gRunning:
        clear_canvas()

        walkImage.update()
        dieImage.update()
        attackImage.update()
        appearImage.update()

        dieImage.Draw()
        walkImage.Draw()
        attackImage.Draw()
        appearImage.Draw()

        update_canvas()
        handle_events()
        delay(0.12)

    close_canvas()



if __name__ == '__main__':
    main()
