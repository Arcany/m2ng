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
    change_x = 2
    change_y = 1


    def __init__(self, x, y,length):
        super().__init__()
        self.img_file = "./sprites/enemies/blockerMad.png"

        self.image = pygame.image.load(self.img_file)
        self.image = pygame.transform.scale(self.image, (15,15))

        self.rect = self.image.get_rect()
        self.rect.y = y-15
        self.rect.x = x
        self.length = length
        self.algus_x = x
        self.direction = choice(["right", "left"])

    def randcolor(self):
        return choice([YELLOW, BLUE, GREEN, RED, PURPLE])

    def move(self):

        """ Liigutab vastast"""
        # Liigub paremale/vasakule
        if self.algus_x+self.length > self.rect.x+15 and self.direction == "right":
            self.rect.x += self.change_x
        elif self.algus_x+self.length <= self.rect.x+15 and self.direction == "right":
            self.direction = "left"
        elif self.algus_x - self.length < self.rect.x-5 and self.direction == "left":
            self.rect.x -= self.change_x
        else:
            self.direction = "right"
