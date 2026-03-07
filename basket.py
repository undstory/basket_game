import pygame

class Basket:
    def __init__(self, bg_game):
        self.screen = bg_game.screen
        self.screen_rect = bg_game.screen.get_rect()
        self.basket_image = pygame.image.load('./images/basket.png')
        self.basket_image = pygame.transform.scale(self.basket_image, (64, 64))
        self.basket_rect = self.basket_image.get_rect()
        self.basket_rect.midbottom = self.screen_rect.midbottom

    def blitBasket(self):
        self.screen.blit(self.basket_image, self.basket_rect)