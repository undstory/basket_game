import pygame

class Explosion:
    def __init__(self, bg_game, x, y):
        self.screen = bg_game.screen
        self.screen_rect = self.screen.get_rect()
        self.explosion_image = pygame.image.load('./images/boom.png')
        self.explosion_image = pygame.transform.scale(self.explosion_image, (60, 60))
        self.explosion_rect = self.explosion_image.get_rect(center=(x, y))
        self.spawn_time = pygame.time.get_ticks()
        self.duration = 500

    def blit_boom(self):
        self.screen.blit(self.explosion_image, self.explosion_rect)

    def is_alive(self):
        return pygame.time.get_ticks() - self.spawn_time < self.duration