from pygame._sdl2.video import Window,Texture,Image,Renderer
import pygame
from settings import *
class App:

    def __init__(self,WIN_SIZE = [1366,768],Title = "pygame", refresh_rate = 60) -> None:
        self.window = Window(title=Title,size = WIN_SIZE)
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
        self.dt = self.clock.tick() * 0.001
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
        super().run()

class GamePlay(App):
    def __init__(self, WIN_SIZE=[1366, 768], Title="pygame") -> None:
        super().__init__(WIN_SIZE, Title)

    def update(self):
        super().update()
    
    def draw(self):
        self.renderer.clear()
        self.window.title = str(1/max(0.001,self.dt))
        self.renderer.present()
        
    
    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

    def run(self):
        super().run()
        
    
class SceneManager:

    def __init__(self) -> None:
        self.scenes = []
    
    def push(self,scene : App):
        self.scenes.append(scene)
    
    def run(self):
        if len(self.scenes)> 0:
            self.scenes[-1].run()
        