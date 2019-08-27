import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
from bullet import Bullet

import game_functions as gf


def run_game():
    #Initialize game and create a screen object
    pygame.init()
    settings = Settings()
    settings.printSettings()

    screen = pygame.display.set_mode(
            (settings.screen_width, settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    ship = Ship(screen)
    bullets = Group()
    aliens = Group()

    gf.create_fleet(settings, screen, ship, aliens)

    #Start the main loop
    while True:
        gf.check_events(ship, bullets, screen, settings)
        ship.update()
        bullets.update()
        gf.update_bullets(bullets, aliens)
        gf.update_aliens(settings, aliens)
        gf.update_screen(settings, screen, ship, bullets, aliens)
        

run_game()
