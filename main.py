import pygame
import pygame.freetype as ft
import sys,math,os
from pygame._sdl2.video import Window,Texture,Image,Renderer
from sprite_classes import SpriteUnit,SpriteHandler

class App:

    def __init__(self,WIN_SIZE = [1366,768],Title = "pygame") -> None:
        self.window = Window(title=Title,size = WIN_SIZE)
        self.renderer = Renderer(self.window)
        self.renderer.draw_color = (0,0,0,255)
        self.refresh_rate = 60
        self.refresh_time_cnt = 0
        self.clock = pygame.time.Clock()
        self.dt = 0.0

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

    def update(self):
        self.dt = self.clock.tick() * 0.001
        self.refresh_time_cnt += self.dt

    def draw(self):
        self.renderer.clear()

        self.renderer.present()

    def run(self):
        while True:
            self.check_events()
            self.update()
            if self.refresh_time_cnt >= 1/self.refresh_rate:
                self.draw()
                self.refresh_time_cnt -= 1/self.refresh_rate

if __name__ == "__main__":
    app = App()
    app.run()