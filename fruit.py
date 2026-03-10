import pygame
import random

class Fruit:
    def __init__(self, gb_game, image):
        self.screen = gb_game.screen
        self.fruit_image = pygame.transform.scale(image, (60, 60))
        self.fruit_rect = self.fruit_image.get_rect()
        self.fruit_rect.x = random.randint(0, 1100)
        self.fruit_rect.y = -10

    def blit_fruit(self):
        self.screen.blit(self.fruit_image, self.fruit_rect)

    def move_fruit(self):
        self.fruit_rect.y += 1


