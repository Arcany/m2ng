import pygame
from Enemy import Enemy
from Points import Points
from Player import Player
from Rooms import Room, Room0, Room1, Room2, Room3
from random import *
#Defineerime värvid
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
PURPLE = (255, 0, 255)

 

def main():
    """ Peaprogramm """
 
    # Pygamei kutsumine
    pygame.init()
 
    # 800x600 ekraan
    screen = pygame.display.set_mode([800, 600])
 
    # Programmi akna tiitel
    pygame.display.set_caption('Mäng')
 
    # Mängija objekt
    existingsprites = pygame.sprite.Group()
    player = Player(50, 200)
    enemy = Enemy(25, 100)
    point = Points(randint(100,650),randint(100,650))


    existingsprites.add(player)
    existingsprites.add(enemy)
    existingsprites.add(point)

    #Ruumide tegemine
    rooms = []
    room = Room0()
    rooms.append(room)
    room = Room1()
    rooms.append(room)
    room = Room2()
    rooms.append(room)
    room = Room3()
    rooms.append(room)

    current_room_n = 0
    current_room = rooms[current_room_n]
 
    clock = pygame.time.Clock()
 
    tehtud = True
    algus = True
    #Algus ekraan
    while algus:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                algus = False
                labi = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    tehtud = False
                    algus = False
        screen.fill(BLACK)
        font = pygame.font.SysFont("Arial", 72)
        font2 = pygame.font.SysFont("Arial", 36)
        text = font.render("Liigu kasutades noole nuppe", True, GREEN)
        text2 = font2.render("Vajuta tühikut, et alustada", True, BLUE)
        screen.blit(text,(400 - text.get_width() // 2, 300 - text.get_height() // 2))
        screen.blit(text2,(600 - text.get_width() // 2, 500 - text.get_height() // 2))
        pygame.display.flip()
        clock.tick(60)

    #Mäng ise
    while not tehtud:
 
        # --- Sündmuste käsitlemine ---
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                tehtud = True
                labi = False
 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.changespeed(-3, 0)
                if event.key == pygame.K_RIGHT:
                    player.changespeed(3, 0)
                if event.key == pygame.K_UP:
                    player.changespeed(0, -3)
                if event.key == pygame.K_DOWN:
                    player.changespeed(0, 3)
 
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    player.changespeed(3, 0)
                if event.key == pygame.K_RIGHT:
                    player.changespeed(-3, 0)
                if event.key == pygame.K_UP:
                    player.changespeed(0, 3)
                if event.key == pygame.K_DOWN:
                    player.changespeed(0, -3)
 
        # --- Mängu loogika ---
        # Paneb mängija ja vastase liikuma ning kontrollib ruumide vahetust
        player.move(current_room.wall_list)
        enemy.move(current_room.wall_list)
        if player.rect.x < -15:
            if current_room_n == 0:
                current_room_n = 3
                current_room = rooms[current_room_n]
                player.rect.x = 790
                existingsprites.remove(enemy)
                enemy = Enemy(randint(200,500),randint(200,500))
                existingsprites.add(enemy)
                existingsprites.remove(point)
                point = Points(randint(200, 500), randint(200, 500))
                while point.check(current_room.wall_list) == 1:
                    existingsprites.remove(point)
                    point = Points(randint(200, 500), randint(200, 500))
                existingsprites.add(point)
            elif current_room_n == 2:
                current_room_n = 1
                current_room = rooms[current_room_n]
                player.rect.x = 790
                existingsprites.remove(enemy)
                enemy = Enemy(randint(200,500), randint(200,500))
                existingsprites.add(enemy)
                existingsprites.remove(point)
                point = Points(randint(200, 500), randint(200, 500))
                while point.check(current_room.wall_list) == 1:
                    existingsprites.remove(point)
                    point = Points(randint(200, 500), randint(200, 500))
                existingsprites.add(point)
            elif current_room_n == 3:
                current_room_n = 2
                current_room = rooms[current_room_n]
                player.rect.x = 790
                existingsprites.remove(enemy)
                enemy = Enemy(randint(200, 500), randint(200, 500))
                existingsprites.add(enemy)
                existingsprites.remove(point)
                point = Points(randint(200,500), randint(200,500))
                while point.check(current_room.wall_list) == 1:
                    existingsprites.remove(point)
                    point = Points(randint(200, 500), randint(200, 500))
                existingsprites.add(point)
            else:
                current_room_n = 0
                current_room = rooms[current_room_n]
                player.rect.x = 790
                existingsprites.remove(enemy)
                enemy = Enemy(randint(200, 500), randint(200, 500))
                existingsprites.add(enemy)
                existingsprites.remove(point)
                point = Points(randint(200, 500), randint(200, 500))
                while point.check(current_room.wall_list) == 1:
                    existingsprites.remove(point)
                    point = Points(randint(200, 500), randint(200, 500))
                existingsprites.add(point)

        if player.rect.x > 801:
            if current_room_n == 0:
                current_room_n = 1
                current_room = rooms[current_room_n]
                player.rect.x = 0
                existingsprites.remove(enemy)
                enemy = Enemy(randint(350, 650), randint(350, 650))
                existingsprites.add(enemy)
                existingsprites.remove(point)
                point = Points(randint(200, 500), randint(200, 500))
                while point.check(current_room.wall_list) == 1:
                    existingsprites.remove(point)
                    point = Points(randint(200, 500), randint(200, 500))
                existingsprites.add(point)
            elif current_room_n == 1:
                current_room_n = 2
                current_room = rooms[current_room_n]
                player.rect.x = 0
                existingsprites.remove(enemy)
                enemy = Enemy(randint(350, 650), randint(350, 650))
                existingsprites.add(enemy)
                existingsprites.remove(point)
                point = Points(randint(200, 500), randint(200, 500))
                while point.check(current_room.wall_list) == 1:
                    existingsprites.remove(point)
                    point = Points(randint(200, 500), randint(200, 500))
                existingsprites.add(point)
            elif current_room_n == 2:
                current_room_n = 3
                current_room = rooms[current_room_n]
                player.rect.x = 0
                existingsprites.remove(enemy)
                enemy = Enemy(randint(350, 650), randint(350, 650))
                existingsprites.add(enemy)
                existingsprites.remove(point)
                point = Points(randint(200, 500), randint(200, 500))
                while point.check(current_room.wall_list) == 1:
                    existingsprites.remove(point)
                    point = Points(randint(200, 500), randint(200, 500))
                existingsprites.add(point)
            else:
                current_room_n = 0
                current_room = rooms[current_room_n]
                player.rect.x = 0
                existingsprites.remove(enemy)
                enemy = Enemy(randint(350, 650), randint(350, 650))
                existingsprites.add(enemy)
                existingsprites.remove(point)
                point = Points(randint(200, 500), randint(200, 500))
                while point.check(current_room.wall_list) == 1:
                    existingsprites.remove(point)
                    point = Points(randint(200, 500), randint(200, 500))
                existingsprites.add(point)
 
        # --- Kõige joonistamine ---
        screen.fill(WHITE)
 
        existingsprites.draw(screen)
        current_room.wall_list.draw(screen)
        font = pygame.font.SysFont("Arial", 14)
        text = font.render("Skoor: " + str(player.points), True, BLACK)
        screen.blit(text, (50 - text.get_width() // 2, 50 - text.get_height() // 2))
        pygame.display.flip()
 
        clock.tick(60)
        #Vaatab, kas mängija põrkas kokku seinaga
        if player.col == 1:
            tehtud = True
            labi = True

        #Vaatab, kas mängija põrkas kokku vastasega
        if pygame.sprite.collide_rect(player, enemy) == 1:
            tehtud = True
            labi = True
        else:
            pass
        #Vaatab, kas mängija sai punkti kätte
        if pygame.sprite.collide_rect(player, point) == 1 and current_room_n == 0:
            existingsprites.remove(point)
            point = Points(randint(100, 300), randint(100, 300))
            Player.points += 10
            enemy.extra += 1

        elif pygame.sprite.collide_rect(player, point) == 1 and current_room_n == 1:
            existingsprites.remove(point)
            point = Points(randint(100, 300), randint(100, 300))
            Player.points += 20
            existingsprites.add(point)
            enemy.extra += 0.5
        elif pygame.sprite.collide_rect(player, point) == 1 and current_room_n == 2:
            existingsprites.remove(point)
            point = Points(randint(100, 300), randint(100, 300))
            Player.points += 30
            existingsprites.add(point)
            enemy.extra += 0.25
        elif pygame.sprite.collide_rect(player, point) == 1 and current_room_n == 3:
            existingsprites.remove(point)
            point = Points(randint(100, 300), randint(100, 300))
            Player.points += 40
            existingsprites.add(point)
            enemy.extra += 0.1
        while point.check(current_room.wall_list) == 1:
            existingsprites.remove(point)
            point = Points(randint(200, 500), randint(200, 500))
            existingsprites.add(point)


        enemy.nurk(player.rect.x,player.rect.y)
    #Lõpp ekraan
    while labi:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                labi = False
            elif event.type == pygame.KEYDOWN:
                labi = False
        screen.fill(BLACK)
        font = pygame.font.SysFont("Arial",64)
        text = font.render("Mäng läbi", True, GREEN)
        screen.blit(text,(400 - text.get_width() // 2, 300 - text.get_height() // 2))
        font = pygame.font.SysFont("Arial", 32)
        text = font.render("Skoor: " + str(player.points), True, GREEN)
        screen.blit(text, (400 - text.get_width() // 2, 400 - text.get_height() // 2))
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()
 
if __name__ == "__main__":
    main()

