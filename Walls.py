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

class Wall(pygame.sprite.Sprite):
    """Seinade klass """

    def __init__(self, x, y, width, height,img_file):
        """ Constructor funktsioon"""

        # Kõrgema konstruktori kutsumine
        super().__init__()

        # Teeb seina

        self.image = pygame.image.load(img_file)
        self.image = pygame.transform.scale(self.image, (width, height))

        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
        self.rect.h = height
        self.rect.w = width

    def randcolor(self):
        return choice([YELLOW, BLUE, GREEN, RED, PURPLE])

