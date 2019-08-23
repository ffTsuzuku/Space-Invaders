import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """A class to  manage bullets fired from the ship. """

    def __init__(self, screen, ship):
        #Settings
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60

        super(Bullet, self).__init__()
        self.screen = screen

        #initialize bullet rect at (0,0)
        self.rect = pygame.Rect(0,0,self.bullet_width, self.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        self.y = float(self.rect.y)




