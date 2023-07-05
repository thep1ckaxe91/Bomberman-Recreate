import pygame
from pygame._sdl2.video import Image, Renderer, Texture, Window

from Entity import *
from settings import *
from sprite_classes import SpriteHandler


class App:

    def __init__(self,WIN_SIZE = [WIDTH,HEIGHT],Title = "pygame", refresh_rate = 60) -> None:
        self.window = Window(title=Title,size = WIN_SIZE)
        # self.window.resizable = True
        self.camera_center = pygame.math.Vector2(WIN_SIZE[0]/2,WIN_SIZE[1]/2)
        self.renderer = Renderer(self.window)
        self.renderer.draw_color = (0,0,0,255)
        self.refresh_rate = refresh_rate
        self.refresh_time_cnt = 0
        self.clock = pygame.time.Clock()
        self.dt = 0.0

    def check_events(self):
        pass

    def update(self):
        '''
        Update delta time and refresh time
        '''
        self.dt = self.clock.tick(FPS_CAP) * 0.001
        self.refresh_time_cnt += self.dt

    def draw(self):
        pass

    def run(self):
        while True:
            self.check_events()
            self.update()
            if self.refresh_time_cnt >= 1/self.refresh_rate:
                self.draw()
                self.refresh_time_cnt -= 1/self.refresh_rate

class MainMenu(App):

    def __init__(self, WIN_SIZE=[1366, 768], Title="pygame") -> None:
        super().__init__(WIN_SIZE, Title)

    def update(self):
        super().update()
    
    def draw(self):
        self.renderer.clear()

        self.renderer.present()
    
    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

    def run(self):
        while True:
            self.check_events()
            self.update()
            if self.refresh_time_cnt >= 1/self.refresh_rate:
                self.draw()
                self.refresh_time_cnt -= 1/self.refresh_rate

class GamePlay(App):
    def __init__(self, WIN_SIZE=[1366, 768], Title="pygame") -> None:
        super().__init__(WIN_SIZE, Title)
        self.dynamic_group = SpriteHandler(self)
        self.static_group = SpriteHandler(self)
        self.dynamic_group.add(Player(self.dynamic_group,(50,500)))

    def update(self):
        self.dynamic_group.update()
        self.static_group.update()
        super().update()
    
    def draw(self):
        self.renderer.clear()
        self.window.title = str(1/max(0.001,self.dt))
        self.dynamic_group.draw()
        self.static_group.draw()
        self.renderer.present()
        
    
    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
                quit()

    def run(self):
        while True:
            self.check_events()
            self.update()
            if self.refresh_time_cnt >= 1/self.refresh_rate:
                self.draw()
                self.refresh_time_cnt -= 1/self.refresh_rate
        
    
class SceneManager:

    def __init__(self) -> None:
        self.scenes = []
    
    def push(self,scene : App):
        self.scenes.append(scene)
    
    def run(self):
        if len(self.scenes)> 0:
            self.scenes[-1].run()
        