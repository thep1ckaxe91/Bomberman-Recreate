import pygame
from sprite_classes import SpriteHandler, SpriteUnit
class Entity(SpriteUnit):
    
    def __init__(self, handler: SpriteHandler, pos, world_pos) -> None:
        super().__init__(handler, pos)
        self.display_offset = pos
        self.x,self.y = world_pos[0],world_pos[1]
    
    def update():
        return super().update()