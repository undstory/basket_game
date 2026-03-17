import pygame

class Catcher:
    def __init__(self, bg_game):
        self.screen = bg_game.screen
        self.screen_rect = self.screen.get_rect()
        self.catcher_image = pygame.image.load('./images/catcher.png')
        self.catcher_image = pygame.transform.scale(self.catcher_image, (120, 120))
        self.catcher_rect = self.catcher_image.get_rect()
        self.catcher_rect.midbottom = self.screen_rect.midbottom
        self.moving_right = False
        self.moving_left = False
        self.catcher_speed = 2

    def blit_catcher(self):
        self.screen.blit(self.catcher_image, self.catcher_rect)
        pygame.draw.rect(self.screen, (255, 0, 0), self.get_catch_zone(), 2)

    def move_catcher(self):
        if self.moving_left and self.catcher_rect.left > 0:
            self.catcher_rect.x -= self.catcher_speed
        elif self.moving_right and self.catcher_rect.right < 1200:
            self.catcher_rect.x += self.catcher_speed

    def get_catch_zone(self):
        return pygame.Rect(
            self.catcher_rect.left + 50,
            self.catcher_rect.top +40,
            self.catcher_rect.width -100,
            self.catcher_rect.height -80
        )