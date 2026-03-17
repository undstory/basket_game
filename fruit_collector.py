import sys
import pygame
import random
from catcher import Catcher
from fruit import Fruit
from explosion import Explosion

# <a href='https://pngtree.com/freepng/pretty-catcher_48522.html'>png image from pngtree.com/</a>

class FruitCollectorGame:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((1200, 800))
        self.catcher = Catcher(self)
        self.explosions = []
        self.fruits = []
        self.spawn_fruit = pygame.USEREVENT + 1 # rozne identyfikatory eventow
        pygame.time.set_timer(self.spawn_fruit, 1000)
        self.apple_img = pygame.image.load('./images/apple.png')
        self.banana_img = pygame.image.load('./images/banana.png')
        self.bomb_img = pygame.image.load('./images/bomb.png')
        self.fruit_type = [self.apple_img, self.banana_img, self.bomb_img]

    def _spawn_fruits(self):
        fruit_data = random.choice([
            {
                "image": self.apple_img,
                "points": 10,
                "type": "apple"
            },
            {
                "image": self.banana_img,
                "points": 20,
                "type": "banana"
            },
                    {
                "image": self.bomb_img,
                "points": -50,
                "type": "bomb"
            },
            ])
        self.fruits.append(Fruit(self, fruit_data))

    def _check_collisions(self):
        catch_zone = self.catcher.get_catch_zone()

        for fruit in self.fruits[:]:
            if catch_zone.colliderect(fruit.fruit_rect):
                self.catcher.set_full()
                if fruit.type == 'bomb':
                    self.explosions.append(Explosion(self, fruit.fruit_rect.centerx, fruit.fruit_rect.centery))
                self.fruits.remove(fruit)


    def _update_screen(self):
        self.screen.fill((20, 20, 20))
        self.catcher.blit_catcher()
        for fruit in self.fruits:
            fruit.blit_fruit()
        for explosion in self.explosions:
            if explosion.is_alive():
                explosion.blit_boom()
            else:
                self.explosions.remove(explosion)
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
                    self.catcher.moving_left = True
                elif event.key == pygame.K_RIGHT:
                    self.catcher.moving_right = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    self.catcher.moving_left = False
                if event.key == pygame.K_RIGHT:
                    self.catcher.moving_right = False
            elif event.type == self.spawn_fruit:
                self._spawn_fruits()

    def run_game(self):
        while True:
            self._manage_events()
            self.catcher.move_catcher()
            for fruit in self.fruits:
                fruit.move_fruit()
                self._check_collisions()
            self._update_screen()
            self.clock.tick(60)

if __name__ == '__main__':
    bg = FruitCollectorGame()
    bg.run_game()