import pygame
from Walls import Wall

class Room(object):
    """ Ruumi klass"""

    # Igal toal on seina list
    wall_list = None

    # enemy_sprites = None

    def __init__(self):
        """ Constructor"""
        self.wall_list = pygame.sprite.Group()
        # self.enemy_sprites = pygame.sprite.Group()


class Room0(Room):
    """Seinad ruumis 0"""

    def __init__(self):
        super().__init__()
        # Teeb seinad
        self.C = ".\sprites\tiles\castleCenter.png"

        # See on seinade list. Igal kuju [x, y, laius, kõrgus, värv]
        walls = [[0, 0, 20, 250, self.C],
                 [0, 350, 20, 250, self.C],
                 [780, 0, 20, 250, self.C],
                 [780, 350, 20, 250, self.C],
                 [20, 0, 760, 20, self.C],
                 [20, 580, 760, 20, self.C]
                 ]

        # Käib järjendi läbi, teeb seinad
        for item in walls:
            wall = Wall(item[0], item[1], item[2], item[3], item[4])
            self.wall_list.add(wall)


class Room1(Room):
    """Seinad ruumis 1"""

    def __init__(self):
        super().__init__()
        # Teeb seinad
        self.C = ".\sprites\tiles\castleCenter.png"

        # See on seinade list. Igal kuju [x, y, laius, kõrgus, värv]
        walls = [[0, 0, 20, 250, self.C],
                 [0, 350, 20, 250, self.C],
                 [780, 0, 20, 250, self.C],
                 [780, 350, 20, 250, self.C],
                 [20, 0, 760, 20, self.C],
                 [20, 580, 760, 20, self.C],
                 [390, 50, 20, 500, self.C]
                 ]

        # Käib järjendi läbi, teeb seinad
        for item in walls:
            wall = Wall(item[0], item[1], item[2], item[3], item[4])
            self.wall_list.add(wall)


class Room2(Room):
    """Seinad ruumis 2"""

    def __init__(self):
        super().__init__()
        self.C = ".\sprites\tiles\castleCenter.png"
        walls = [[0, 0, 20, 250, self.C],
                 [0, 350, 20, 250, self.C],
                 [780, 0, 20, 250, self.C],
                 [780, 350, 20, 250, self.C],
                 [20, 0, 760, 20, self.C],
                 [20, 580, 760, 20, self.C],
                 [190, 50, 20, 500, self.C],
                 [590, 50, 20, 500, self.C]
                 ]

        for item in walls:
            wall = Wall(item[0], item[1], item[2], item[3], item[4])
            self.wall_list.add(wall)


class Room3(Room):
    """Seinad ruumis 3"""

    def __init__(self):
        super().__init__()
        self.C = ".\sprites\tiles\castleCenter.png"

        walls = [[0, 0, 20, 250, self.C],
                 [0, 350, 20, 250, self.C],
                 [780, 0, 20, 250, self.C],
                 [780, 350, 20, 250, self.C],
                 [20, 0, 760, 20, self.C],
                 [20, 580, 760, 20, self.C]
                 ]

        for item in walls:
            wall = Wall(item[0], item[1], item[2], item[3], item[4])
            self.wall_list.add(wall)

        for x in range(100, 800, 100):
            for y in range(30, 451, 300):
                wall = Wall(x, y, 20, 235, self.C)
                self.wall_list.add(wall)

        for x in range(150, 700, 100):
            wall = Wall(x, 200, 20, 200, self.C)
            self.wall_list.add(wall)

