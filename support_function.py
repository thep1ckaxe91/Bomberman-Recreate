import pygame
def world_to_display_pos(world_pos : pygame.math.Vector2, camera_center : pygame.math.Vector2, width : int, height : int, screen_width : int, screen_height : int) -> tuple[int,int]:
    '''
    translate from world pos to display pos
    width, height is width and height of the sprite
    '''
    dp = world_pos - camera_center + (screen_width/2,screen_height/2) - (width/2,height/2)
    return [int(dp.x),int(dp.y)]