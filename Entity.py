import pygame
from pygame.locals import *
from graphics_load import PlayerGraphics
from settings import *
from sprite_classes import SpriteHandler, SpriteUnit
from support_function import *


class Entity(SpriteUnit):
    
    def __init__(self, handler: SpriteHandler, world_pos) -> None:
        super().__init__(handler)
        self.display_pos = pygame.math.Vector2()
        self.world_pos = pygame.math.Vector2(world_pos)
    

class Player(Entity):

    run_speed = 32 #pixel per sec
    def __init__(self, handler: SpriteHandler, world_pos) -> None:
        super().__init__(handler, world_pos)
        self.graphics = PlayerGraphics(handler)
        self.image = self.graphics.down
        self.rect = pygame.Rect(0,0,TILESIZE,TILESIZE)
        

    def movement_handler(self):
        keys = pygame.key.get_pressed()
        if keys[K_w]:
            self.world_pos[1] -= self.run_speed*self.handler.app.dt*SCALE
        if keys[K_s]:
            self.world_pos[1] += self.run_speed*self.handler.app.dt*SCALE
        if keys[K_d]:
            self.world_pos[0] += self.run_speed*self.handler.app.dt*SCALE
        if keys[K_a]:
            self.world_pos[0] -= self.run_speed*self.handler.app.dt*SCALE

    def translate(self):
        self.rect.topleft = world_to_display_pos(self.world_pos,self.handler.app.camera_center,TILESIZE,TILESIZE,WIDTH,HEIGHT)
    
    def draw(self):
        self.handler.app.renderer.blit(self.image,pygame.Rect(*world_to_display_pos(self.world_pos,self.handler.app.camera_center,TILESIZE,TILESIZE,WIDTH,HEIGHT),width=TILESIZE,height=TILESIZE))
    
    def update(self):
        self.movement_handler()
        self.translate()
        super().update()