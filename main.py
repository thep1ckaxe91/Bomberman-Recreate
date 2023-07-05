import math
import os
import sys

import pygame
import pygame.freetype as ft
from pygame._sdl2.video import Image, Renderer, Texture, Window

from App import *
from settings import *

screen_surf = pygame.display.set_mode((1,1),pygame.NOFRAME)

if __name__ == "__main__":
    scene_manager = SceneManager()
    scene_manager.push(GamePlay())
    scene_manager.run()