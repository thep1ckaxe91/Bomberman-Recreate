import math
import os
import sys

import pygame

from App import *
from settings import *

pygame.display.set_mode((1,1),pygame.NOFRAME)

if __name__ == "__main__":
    scene_manager = SceneManager()
    scene_manager.push(GamePlay())
    scene_manager.run()