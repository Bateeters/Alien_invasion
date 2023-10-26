class Settings:
    """A class to store all settings for Alien Invasion"""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (25,25,25)
        self.font_color = (255, 255, 255)

        # Ship settings
        self.ship_speed = 3
        self.ship_limit = 3

        # Bullet Settings
        self.bullet_speed = 2.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (230,230,230)
        self.bullets_allowed = 7

        # Alien settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10 # Adjusted for testing purposes. Base speed is 10
        
        # How quickly the game speeds up
        self.speedup_scale = 1.25

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.ship_speed = 1.5
        self.bullet_speed = 2.5
        self.alien_speed = 1.0

        # Fleet direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1

        # Scoring settings
        self.alien_points = 50
    
    def increase_speed(self):
        """Increse speed settings."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale