class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Bullet setting
        self.bullet_speed = 2.0
        self.bullet_width = 3
        self.bullet_height = 16
        self.bullet_color = (60, 60, 60)
        self.bullet_allowed = 3
