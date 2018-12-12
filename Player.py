import pygame

#Defineerime värvid
BLACK = (0, 0, 0)
class Player(pygame.sprite.Sprite):
    """ Mängija klass"""

    # Kiirus
    change_x = 0
    change_y = 5

    # Punktid
    points = 0

    def __init__(self, x, y):
        """ Constructor funktsioon """

        # Kõrgema konstruktori kutsumine
        super().__init__()

        # Laius,kõrgus
        self.img_file = "./sprites/player/p3_front.png"
        self.image = pygame.image.load(self.img_file)
        self.image = pygame.transform.scale(self.image, (50,70))

        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
        self.jumping_allowed = 0
        self.col = 0
        self.is_jumping = 0

    def collision(self):
        if self.col == 0:
            self.col = 1

    def changespeed(self, x, y):
        """ Muudab mängija kiirust, nupuvahetusega"""
        self.change_x += x
        self.change_y += y

    def move(self, walls):
        """ Liigutab mängijat"""

        # Liigub paremale/vasakule
        self.rect.x += self.change_x

        # Kas me tabasime seina?
        wall_collision_list = pygame.sprite.spritecollide(self, walls, False)
        for block in wall_collision_list:
            # Ei muuda asukohta
            if self.change_x > 0:
                self.rect.right = block.rect.left

            else:
                # Ei muuda asukohta
                self.rect.left = block.rect.right

        # Liigub üles/alla
        self.rect.y += self.change_y

        # Kas me tabasime seina?
        wall_collision_list = pygame.sprite.spritecollide(self, walls, False)
        if wall_collision_list == []:
            self.col = 0
        for block in wall_collision_list:

            # Ei muuda asukohta
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
                self.collision()


            else:
                self.rect.top = block.rect.bottom
                self.collision()
        if self.is_jumping == 1 and self.change_y <= 5:
            pass
        else:
            self.is_jumping = 0
        if self.is_jumping == 1:
            self.change_y += 1






