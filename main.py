import pygame
import pygame.freetype as ft
import sys,math,os
from pygame._sdl2.video import Window,Texture,Image,Renderer
from sprite_classes import SpriteUnit,SpriteHandler
from App import *

if __name__ == "__main__":
    scene_manager = SceneManager()
    scene_manager.push(GamePlay())
    scene_manager.run()