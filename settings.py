import pygame.freetype as ft

ft.init()
FPS_FONT = ft.SysFont('consolas',40)
SCALE = 5
TILESIZE = 16 * SCALE
FPS_CAP = 200
WIDTH,HEIGHT = 1366,768