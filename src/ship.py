import pygame

class Ship():

    def __init__(self, screen):
        """Initialize the ship and set its starting position. """
        self.screen = screen

        self.image = pygame.image.load('../images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.center = float(self.rect.centerx)

        #Flags
        self.moving_right = False
        self.moving_left = False

        #Attributes
        self.speed_factor = 1.5

    def blitme(self):
        """Draw the ship at its current location. """
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Center the ship on the screen."""
        self.center = self.screen_rect.centerx

    def update(self):
        """Update the ship's position based on movement flags. """

        if self.moving_right and self.rect.right < self.screen_rect.right: 
            self.center += self.speed_factor
        
        elif self.moving_left and self.rect.left > 0:
            self.center += -self.speed_factor

        self.rect.centerx = self.center