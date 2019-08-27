import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
from bullet import Bullet
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button

import game_functions as gf


def run_game():
    #Initialize game and create a screen object
    pygame.init()
    settings = Settings()
    settings.printSettings()

    screen = pygame.display.set_mode(
            (settings.screen_width, settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Make the Play button.
    play_button = Button(settings, screen, "Play")

    ship = Ship(settings, screen)
    bullets = Group()
    aliens = Group()

    stats = GameStats(settings)
    sb = Scoreboard(settings, screen, stats)

    gf.create_fleet(settings, screen, ship, aliens)

    #Start the main loop
    while True:
        gf.check_events(settings, screen, stats, sb, play_button, ship, aliens, 
                bullets)

        if stats.game_active:
                ship.update()
                bullets.update()
                gf.update_bullets(settings, screen, stats, sb, ship, bullets, 
                        aliens)
                gf.update_aliens(settings, stats, sb, screen, ship, aliens, 
                        bullets)
                        
        gf.update_screen(settings, screen, sb,  ship, bullets, aliens, stats, 
                play_button)
        

run_game()
