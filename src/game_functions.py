import sys

from alien import Alien
from bullet import Bullet
from time import sleep

import pygame



def check_events(game_settings, screen, stats, play_button, ship, aliens, 
    bullets):
    """Respond to keypresses and mouse events."""

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            handle_key_down_events(event, screen, ship, bullets, game_settings)

        elif event.type == pygame.KEYUP:
            handle_key_up_events(event, screen, ship)

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(game_settings, screen, stats, play_button, ship,
                aliens, bullets,  mouse_x, mouse_y)

def check_play_button(game_settings, screen, stats, play_button, ship, aliens, 
    bullets, mouse_x, mouse_y):
    """Start a new game if the player clicked Play."""
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        #Reset the game difficulty
        game_settings.initialize_dynamic_settings()

        #Hide the mouse.
        pygame.mouse.set_visible(False)

        # Reset the game statistics.
        stats.reset_stats()
        stats.game_active = True

        #Empty the aliens and bullets.
        aliens.empty()
        bullets.empty()

        # Create a new fleet and center the ship
        create_fleet(game_settings, screen, ship, aliens)
        ship.center_ship()
    
def handle_key_down_events(event, screen, ship, bullets, settings):
    if event.key == pygame.K_RIGHT:
        #move the ship to the right
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(settings, screen, ship, bullets)

def handle_key_up_events(event, screen, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False

    if event.key == pygame.K_LEFT:
        ship.moving_left = False

def update_screen(settings, screen, ship, bullets, alien, stats, play_button):
    """Update images on the screen, and redraw it. """
    screen.fill(settings.bg_color)
    ship.blitme()
    alien.draw(screen) #draw all spawned aliens in the group

    for bullet in bullets.sprites():
        bullet.draw_bullet()

    # Draw the play button if the game is inactive.
    if not stats.game_active:
        play_button.draw_button()


    #draw the updated screen
    pygame.display.flip()

def fire_bullet(settings, screen, ship, bullets):
    """Fire a bullet if the global limit isn't reached. """
    if len(bullets) < settings.max_bullet_limit:
        new_bullet = Bullet(screen, ship, settings)
        bullets.add(new_bullet)


def update_bullets(settings, screen, ship, bullets, aliens):
    """Despawn any offscreen bullets.And Update current position"""
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    
    # Check for any bullets that have hit aliens.
    # If so, remove the bullet and the alien.
    check_bullet_alien_collisions(settings, screen, ship, aliens, 
        bullets)

def check_bullet_alien_collisions(settings, screen, ship, aliens,
    bullets):
    """Respond to bullet-alien collisions."""
    # Remove any bullets and aliens that have collided.
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, 
        True)

    if len(aliens) == 0:
        # Destroy existing bullets and create new fleet.
        bullets.empty()
        settings.increase_speed() #increase difficulty
        create_fleet(settings, screen, ship, aliens)

def get_number_aliens_x(settings, alien_width):
    """Determine the number of aliens that fit in the row. """
    available_space_x = settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))

    return number_aliens_x

def get_number_rows(settings, ship_height, alien_height):
    """Determine the number of rows of aliens that fit on the screen."""
    available_space_y = (settings.screen_height - (
                            3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))

    return number_rows

def create_alien(settings, screen, aliens, alien_number, row_number):
    """Create an alien and place it in the row. """
    alien = Alien(settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)

def create_fleet(settings, screen, ship, aliens):
    """Generate a wave of aliens. """
    #Create an alien and find the number of aliens in a row.
    alien = Alien(settings, screen)
    number_aliens_x = get_number_aliens_x(settings, alien.rect.width)
    number_rows = get_number_rows(settings, ship.rect.height, alien.rect.height)

    #create the firsr row of aliens
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            #Create an alien and place it in the row
            create_alien(settings, screen, aliens, alien_number, row_number)
            alien.x = alien.rect.width + 2 * alien.rect.width * alien_number
            alien.rect.x = alien.x
            aliens.add(alien)
    
def check_fleet_edges(settings, aliens):
    """Respond appropriately if any aliens have reached an edge."""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(settings, aliens)
            break

def change_fleet_direction(settings, aliens):
    """Drop the entire fleet and change the fleet's direction."""
    for alien in aliens.sprites():
        alien.rect.y += settings.fleet_drop_speed
    settings.fleet_direction *= -1

def update_aliens(settings, stats, screen, ship,  aliens, bullets):
    """Check if the fleet is at an edge, 
        and then update the positions of all aliens in the fleet.
    """
    check_fleet_edges(settings, aliens)
    aliens.update()

    # Look for alien-ship collisions.
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(settings, stats, screen, ship, aliens, bullets)

    # Look for aliens hitting the bottom of the screen.
    check_aliens_bottom(settings, stats, screen, ship, aliens, bullets)

def ship_hit(settings, stats, screen, ship, aliens, bullets):
    """Respond to ship being hit by alien."""
    if stats.ships_left > 0:
        # Decrement ships_left.
        stats.ships_left -= 1

        # Empty the list of aliens and bullets.
        aliens.empty()
        bullets.empty()

        # Create a new fleet and center the ship.
        create_fleet(settings, screen, ship, aliens)
        ship.center_ship()

        # Pause.
        sleep(0.5)

    else:
        stats.game_active = False
        pygame.mouse.set_visible(True) # Renable the mouse

def check_aliens_bottom(settings, stats, screen, ship, aliens, bullets):
    """Check if any aliens have reahed the bottom of the screen."""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            # Treat this the same as if the ship got hit.
            ship_hit(settings, stats, screen, ship, aliens, bullets)
            break