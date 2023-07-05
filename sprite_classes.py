from __future__ import annotations

from typing import TYPE_CHECKING

import pygame

if TYPE_CHECKING:
    from App import App
class SpriteHandler:

    def __init__(self, app : App) -> None:
        self.app = app
        self.group = pygame.sprite.Group()
        self.sprites = []
    
    def add(self,sprite : 'SpriteUnit'):
        self.sprites.append(sprite)
        self.group.add(sprite)
    
    def pop(self):
        """
        Delete the last sprite added to the handler
        """
        sprite = self.sprites.pop()
        sprite.kill()

    def empty(self):
        self.group.empty()
        self.sprites.clear()
    
    def draw(self):
        self.group.draw(self.app.renderer)

    def update(self):
        self.group.update()
        
class SpriteUnit(pygame.sprite.Sprite):
    
    def __init__(self,handler : SpriteHandler) -> None:
        super().__init__()
        self.handler = handler
