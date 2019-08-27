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
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 30
        #fleet direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1

        #Ship Settings
        self.ship_limit = 3


    def printSettings(self):
        print("Screen Width: " + str(self.screen_width))
        print("Screen Height: "+  str(self.screen_height))
        print("BG Color: ", self.bg_color)
        print("Bullet Speed: " +  str(self.bullet_speed))

    