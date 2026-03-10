import pygame

class Basket:
    def __init__(self, bg_game):
        self.screen = bg_game.screen
        self.screen_rect = self.screen.get_rect()
        self.basket_image = pygame.image.load('./images/basket.png')
        self.basket_image = pygame.transform.scale(self.basket_image, (120, 120))
        self.basket_rect = self.basket_image.get_rect()
        self.basket_rect.midbottom = self.screen_rect.midbottom
        self.moving_right = False
        self.moving_left = False
        self.basket_speed = 2

    def blit_basket(self):
        self.screen.blit(self.basket_image, self.basket_rect)

    def move_basket(self):
        if self.moving_left and self.basket_rect.left > 0:
            self.basket_rect.x -= self.basket_speed
        elif self.moving_right and self.basket_rect.right < 1200:
            self.basket_rect.x += self.basket_speed