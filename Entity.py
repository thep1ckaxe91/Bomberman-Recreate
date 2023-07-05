import pygame
from sprite_classes import SpriteHandler, SpriteUnit
from graphics_load import PlayerGraphics
class Entity(SpriteUnit):
    
    def __init__(self, handler: SpriteHandler, pos, world_pos) -> None:
        super().__init__(handler, pos)
        self.display_pos = pygame.math.Vector2(pos)
        self.world_pos = pygame.math.Vector2(world_pos)
    

class Player(Entity):

    def __init__(self, handler: SpriteHandler, pos, world_pos) -> None:
        super().__init__(handler, pos, world_pos)
        self.graphics = PlayerGraphics(handler)

    def movement_handler()
