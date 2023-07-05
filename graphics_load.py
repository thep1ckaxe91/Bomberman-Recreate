import pygame
from pygame._sdl2.video import Texture

from settings import *

'''
Everything must be loaded as sdl2 Texture
'''
class PlayerGraphics:
    def __init__(self,handler) -> None:
        path = "assets/graphics/player/"
        self.up = Texture.from_surface(
            handler.app.renderer,
            pygame.transform.scale(pygame.image.load(path + "up.png").convert_alpha(),(TILESIZE*SCALE,TILESIZE*SCALE))
        )
        self.down = Texture.from_surface(
            handler.app.renderer,
            pygame.transform.scale(pygame.image.load(path + "down.png").convert_alpha(),(TILESIZE*SCALE,TILESIZE*SCALE))
        )
        self.left = Texture.from_surface(
            handler.app.renderer,
            pygame.transform.scale(pygame.image.load(path + "left.png").convert_alpha(),(TILESIZE*SCALE,TILESIZE*SCALE))
        )
        self.right = Texture.from_surface(
            handler.app.renderer,
            pygame.transform.scale(pygame.image.load(path + "right.png").convert_alpha(),(TILESIZE*SCALE,TILESIZE*SCALE))
        )
        self.die = Texture.from_surface(
            handler.app.renderer,
            pygame.transform.scale(pygame.image.load(path + "die.png").convert_alpha(),(TILESIZE*SCALE,TILESIZE*SCALE))
        )

class EnemiesGraphics:
    def __init__(self) -> None:
        pass
