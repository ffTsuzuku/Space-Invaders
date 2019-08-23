import sys

import pygame


def check_events(ship):
    """Respond to keypresses and mouse events."""

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            handle_key_down_events(event, ship)

        elif event.type == pygame.KEYUP:
            handle_key_up_events(event, ship)
    
def handle_key_down_events(event, ship):
    if event.key == pygame.K_RIGHT:
        #move the ship to the right
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True

def handle_key_up_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False

    if event.key == pygame.K_LEFT:
        ship.moving_left = False

def update_screen(settings, screen, ship):
    """Update images on the screen, and redraw it. """
    screen.fill(settings.bg_color)
    ship.blitme()

    #draw the updated screen
    pygame.display.flip()