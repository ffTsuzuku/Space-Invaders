class Settings():
    """A Class to store all settings for Space Invaders. """

    def __init__(self):
        #Screen Settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        #Bullet Settings
        self.bullet_speed = 1
        self.max_bullet_limit = 9

        #Alien Settings
        self.fleet_drop_speed = 10

        #Ship Settings
        self.ship_limit = 3

        #Speed Settings
        self.level_up_scale = 1.1

        self.initialize_dynamic_settings()


    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor  =  1

        #fleet direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1

        #Points for shooting alien
        self.alien_points = 50

    def level_up(self, stats):
        """Increase speed settings. And Alien Points"""
        self.ship_speed_factor *= self.level_up_scale
        self.bullet_speed_factor *= self.level_up_scale
        self.alien_speed_factor *= self.level_up_scale
        self.alien_points *= int(self.level_up_scale)

        #Increase the level. 
        stats.level += 1 

        self.printSettings()

    def printSettings(self):
        print("Screen Width: " + str(self.screen_width))
        print("Screen Height: "+  str(self.screen_height))
        print("BG Color: ", self.bg_color)
        print("Bullet Speed: " +  str(self.bullet_speed))
        print("Points Per Alien: " + str(self.alien_points))
        print("Alien Speed: " + str(self.alien_speed_factor))
        print("Ship Speed: " + str(self.ship_speed_factor))

    