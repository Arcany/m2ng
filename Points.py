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
class Points(pygame.sprite.Sprite):

    def __init__(self,x,y):
        """ Constructor funktsioon """

        # Kõrgema konstruktori kutsumine
        super().__init__()

        # Laius,kõrgus
        self.img_file = "./sprites/points/coinGold.png"
        self.image = pygame.image.load(self.img_file)
        self.image = pygame.transform.scale(self.image, (30,30))

        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x

    def randcolor(self):
        return choice([YELLOW, BLUE, GREEN, RED, PURPLE])

    def check(self,walls):
        for block in walls:
            if pygame.sprite.collide_rect(self, block) == 1:
                return 1
            else:
                pass


