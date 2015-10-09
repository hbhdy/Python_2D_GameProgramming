from pico2d import *

class Background:
    def __init__(self):
        self.image = load_image("background.png")
    def draw(self):
        self.image.draw_to_origin(0,0,1600,800)
