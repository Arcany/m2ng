import pygame
from random import *

#Defineerime värvid
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
PURPLE = (255, 0, 255)


class Enemy(pygame.sprite.Sprite):
    # Kiirus
    change_x = 0
    change_y = 0

    #Trahvi kiirus(Ehk, mida kauem on mängija ruumis seda kiiremaks läheb vastane)
    extra = 0

    def __init__(self, x, y):
        super().__init__()

        self.image = pygame.Surface([15, 15])
        self.image.fill(self.randcolor())

        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x

    def randcolor(self):
        return choice([YELLOW, BLUE, GREEN, RED, PURPLE])

    def move(self, enemy):
        """ Liigutab vastast"""

        # Liigub paremale/vasakule
        self.rect.x += self.change_x
        self.rect.y += self.change_y

    def nurk(self, x, y):
        x1 = self.rect.x - x
        y1 = self.rect.y - y

        if x1 <= 0 and y1 >= 0:
            self.change_x = 1.5 + self.extra
            self.change_y = -1.5 - self.extra
        elif x1 <= 0 and y1 <= 0:
            self.change_x = 1.5 + self.extra
            self.change_y = 1.5 + self.extra
        elif x1 >= 0 and y1 >= 0:
            self.change_x = -1.5 - self.extra
            self.change_y = -1.5 - self.extra
        elif x1 >= 0 and y1 <= 0:
            self.change_x = -1.5 - self.extra
            self.change_y = 1.5 + self.extra