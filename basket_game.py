import sys
import pygame
from basket import Basket

# <a href='https://pngtree.com/freepng/pretty-basket_48522.html'>png image from pngtree.com/</a>

class BasketGame:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((1200, 800))
        self.basket = Basket(self)

    def _update_screen(self):
        self.screen.fill((20, 20, 20))
        self.basket.blitBasket()
        pygame.display.flip()

    def _manage_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit
                    sys.exit()
                elif event.key == pygame.K_LEFT:
                    self.basket.moving_left = True
                elif event.key == pygame.K_RIGHT:
                    self.basket.moving_right = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    self.basket.moving_left = False
                if event.key == pygame.K_RIGHT:
                    self.basket.moving_right = False

    def run_game(self):
        while True:
            self._manage_events()
            self.basket.moveBasket()
            self._update_screen()
            self.clock.tick(60)





if __name__ == '__main__':
    bg = BasketGame()
    bg.run_game()