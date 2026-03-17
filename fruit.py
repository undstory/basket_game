import pygame
import random

class Fruit:
    def __init__(self, bg_game, data):
        self.screen = bg_game.screen
        self.image = data["image"]
        self.fruit_image = pygame.transform.scale(self.image, (60, 60))
        self.points = data["points"]
        self.type = data["type"]
        self.fruit_rect = self.fruit_image.get_rect()
        self.fruit_rect.x = random.randint(0, 1100)
        self.fruit_rect.y = -10

    def blit_fruit(self):
        self.screen.blit(self.fruit_image, self.fruit_rect)
        pygame.draw.rect(self.screen, (255, 0, 0), self.fruit_rect, 2)

    def move_fruit(self):
        self.fruit_rect.y += 1


