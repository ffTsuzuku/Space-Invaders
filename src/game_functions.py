import sys

from bullet import Bullet
import pygame


def check_events(ship, bullets, screen):
    """Respond to keypresses and mouse events."""

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            handle_key_down_events(event, screen, ship, bullets)

        elif event.type == pygame.KEYUP:
            handle_key_up_events(event, screen, ship)
    
def handle_key_down_events(event, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        #move the ship to the right
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        new_bullet = Bullet(screen, ship)
        bullets.add(new_bullet)

def handle_key_up_events(event, screen, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False

    if event.key == pygame.K_LEFT:
        ship.moving_left = False

def update_screen(settings, screen, ship, bullets):
    """Update images on the screen, and redraw it. """
    screen.fill(settings.bg_color)
    ship.blitme()

    for bullet in bullets.sprites():
        bullet.draw_bullet()

    #draw the updated screen
    pygame.display.flip()