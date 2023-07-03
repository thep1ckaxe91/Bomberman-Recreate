import pygame
from pygame._sdl2.video import Image,Texture,Window,Renderer
from App import App
class Scene:

    def __init__(self, app : App, background_img : Texture, last_time = -1) -> None:
        self.app = app
        self.bg = background_img
        self.last_time = last_time

    def events_check(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
    
    def main(self):
        self.app.run()