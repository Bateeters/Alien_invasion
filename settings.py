class Settings:
    """A class to store all settings for Alien Invasion"""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (25,25,25)

        # Ship settings
        self.ship_speed = 2

        # Bullet Settings
        self.bullet_speed = 2.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (230,230,230)
        self.bullets_allowed = 7

        # Alien settings
        self.alien_speed = 1.0