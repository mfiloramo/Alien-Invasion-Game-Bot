import pygame
from pygame.sprite import Sprite
from random import random


class Bot(Sprite):
    """A class to manage the ship."""

    def __init__(self, ai_game):
        """Initialize the ship and set its starting position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship image and get its rect.
        self.image = pygame.image.load('images/bot.bmp')
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

        # Store a decimal value for the ship's horizontal position.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # Movement flags
        self.moving_right = False
        self.moving_left = False

        # Set a toggle switch to coordinate sweeping movement.
        self.move_switch = 0

        # Indicate whether or not the targeting system is active.
        self.target_active = False

        self.locked_on = False

    def update(self):
        """Update the ship's position based on the movement flags."""
        # Update the ship's x value, not the rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # Update rect object from self.x.
        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Center the ship on the screen."""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)

    def auto_fire(self):
        """Automates firing bullets. Randomness implemented."""
        num = random()
        if num > 0.5:
            return True
        else:
            return False

    def sweep_movement(self):
        """Automates sweeping movements across either end of the screen."""
        # Regulates detection mode speed.
        # self.settings.ship_speed = 2.0

        # Toggles sweeping movement based on the bot's move_switch.
        if self.move_switch == 0:
            self.moving_right = True
            self.moving_left = False
        if self.move_switch == 1:
            self.moving_right = False
            self.moving_left = True

        # Regulates ship edge proximity for sweeping movement based on screen width.
        if self.rect.right >= self.settings.screen_width:
            self.move_switch = 1
        if self.rect.left <= 0:
            self.move_switch = 0

