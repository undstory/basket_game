import sys
import pygame
import random
from basket import Basket
from fruit import Fruit

# <a href='https://pngtree.com/freepng/pretty-basket_48522.html'>png image from pngtree.com/</a>

class BasketGame:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((1200, 800))
        self.basket = Basket(self)
        self.fruits = []
        self.spawn_fruit = pygame.USEREVENT + 1 # rozne identyfikatory eventow
        pygame.time.set_timer(self.spawn_fruit, 1000)
        self.apple_img = pygame.image.load('./images/banana.png')
        self.banana_img = pygame.image.load('./images/apple.png')
        self.fruit_type = [self.apple_img, self.banana_img]

    def _spawn_fruits(self):
        image = random.choice(self.fruit_type)
        self.fruits.append(Fruit(self, image))


    def _update_screen(self):
        self.screen.fill((20, 20, 20))
        self.basket.blit_basket()
        for fruit in self.fruits:
            fruit.blit_fruit()
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
            elif event.type == self.spawn_fruit:
                self._spawn_fruits()

    def run_game(self):
        while True:
            self._manage_events()
            self.basket.move_basket()
            for fruit in self.fruits:
                fruit.move_fruit()
            self._update_screen()
            self.clock.tick(60)

if __name__ == '__main__':
    bg = BasketGame()
    bg.run_game()