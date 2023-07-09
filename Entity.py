from typing import Any

import pygame
from pygame._sdl2.video import Image, Texture
from pygame.locals import *

from graphics_load import *
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
        self.image = Image(self.graphics.down,pygame.Rect(0,0,TILESIZE,TILESIZE))
        self.rect = pygame.Rect(0,0,TILESIZE,TILESIZE)
        self.hitbox = self.rect.inflate(-2*SCALE,-2*SCALE)
        

    def movement_handler(self):
        if self.keys[K_w]:
            self.world_pos[1] -= self.run_speed*self.handler.app.dt*SCALE
        if self.keys[K_s]:
            self.world_pos[1] += self.run_speed*self.handler.app.dt*SCALE
        if self.keys[K_d]:
            self.world_pos[0] += self.run_speed*self.handler.app.dt*SCALE
        if self.keys[K_a]:
            self.world_pos[0] -= self.run_speed*self.handler.app.dt*SCALE

    def translate(self):
        self.rect.topleft = world_to_display_pos(self.world_pos,self.handler.app.camera_center,TILESIZE,TILESIZE,WIDTH,HEIGHT)
    
    def check_collision(self):
        pass

    
    def animation_handler(self):
        if self.keys[K_w]:
            self.image = 
    
    def update(self):
        self.keys = pygame.key.get_pressed()
        self.movement_handler()
        self.translate()
        self.check_collision()
        super().update()

class PlayField(Entity):

    def __init__(self, handler: SpriteHandler, world_pos) -> None:
        super().__init__(handler, world_pos)
        self.image = GamePlayGraphics(self.handler.app.renderer).playfield
        self.rect = self.image.get_rect()
    
    def update(self) -> None:
        self.rect.topleft = world_to_display_pos(self.world_pos,self.handler.app.camera_center,self.rect.width,self.rect.height,WIDTH,HEIGHT)
        