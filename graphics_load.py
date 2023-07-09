import pygame
from pygame._sdl2.video import Renderer, Texture

from settings import *

'''
Everything must be loaded as sdl2 Texture
'''
class PlayerGraphics:
    def __init__(self,handler) -> None:
        path = "assets/graphics/player/"
        self.up = Texture.from_surface(
            handler.app.renderer,
            pygame.transform.scale_by(pygame.image.load(path + "up.png").convert_alpha(),(SCALE,SCALE))
        )
        self.down = Texture.from_surface(
            handler.app.renderer,
            pygame.transform.scale_by(pygame.image.load(path + "down.png").convert_alpha(),(SCALE,SCALE))
        )
        self.left = Texture.from_surface(
            handler.app.renderer,
            pygame.transform.scale_by(pygame.image.load(path + "left.png").convert_alpha(),(SCALE,SCALE))
        )
        self.right = Texture.from_surface(
            handler.app.renderer,
            pygame.transform.scale_by(pygame.image.load(path + "right.png").convert_alpha(),(SCALE,SCALE))
        )
        self.die = Texture.from_surface(
            handler.app.renderer,
            pygame.transform.scale_by(pygame.image.load(path + "die.png").convert_alpha(),(SCALE,SCALE))
        )

class GamePlayGraphics:

    def __init__(self,renderer : Renderer) -> None:
        path = "assets/graphics/general/"
        self.playfield = Texture.from_surface(
            renderer,
            pygame.transform.scale_by(pygame.image.load(path+"playfield.png"),(SCALE,SCALE))
        )
        self.door = Texture.from_surface(
            renderer,
            pygame.transform.scale_by(pygame.image.load(path+"door.png"),(SCALE,SCALE))
        )

class EnemiesGraphics:
    def __init__(self) -> None:
        pass
