import pygame
import os
import sys
import random
from math import sin, cos, radians
pygame.init()
current_path = os.path.dirname(__file__)
os.chdir(current_path)
WIDTH = 1000
HEIGHT = 800
FPS = 60
sc = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
from load import *

def game_lvl():
    sc.fill('grey')
    player_group.draw(sc)
    player_group.update()
    wizard_group.draw(sc)
    wizard_group.update(0,0)
    enemy_group.draw(sc)
    enemy_group.update(0,0)
    mp_group.draw(sc)
    mp_group.update(0,0)
    hp_group.draw(sc)
    hp_group.update(0,0)
    door_group.draw(sc)
    door_group.update(0,0)
    chest_group.draw(sc)
    chest_group.update(0,0)
    wall_group.draw(sc)
    wall_group.update(0,0)
    coin_group.draw(sc)
    coin_group.update(0, 0)
    pygame.display.update()

def drawMaps(nameFile):
    maps = []
    source = 'game_lvl/' + str(nameFile)
    with open(source, 'r') as file:
        for i in range(0, 300):
            maps.append(file.readline().replace('\n', '').split(',')[0:-1])

    pos = [0, 0]
    for i in range(0, len(maps)):
        pos[1] = i * 16
        for j in range(0, len(maps[0])):
            pos[0] = 16 * j
            if maps[i][j] == '1':
                wall2 = Wall(wall2_image, pos)
                wall_group.add(wall2)
                camera_group.add(wall2)
            elif maps[i][j] == '2':
                wall1 = Wall(wall1_image, pos)
                wall_group.add(wall1)
                camera_group.add(wall1)
            elif maps[i][j] == '3':
                wall4 = Wall(wall4_image, pos)
                wall_group.add(wall4)
                camera_group.add(wall4)
            elif maps[i][j] == '4':
                wall3 = Wall(wall3_image, pos)
                wall_group.add(wall3)
                camera_group.add(wall3)
            elif maps[i][j] == '5':
                wizard = Wizard(wizard_image, pos)
                wizard_group.add(wizard)
                camera_group.add(wizard)
            elif maps[i][j] == '9':
                # enemy = Enemy({'idle': enemy_image_idle, 'kill': enemy_image_kill, 'right': enemy_image_right})
                enemy = Enemy(enemy_image_idle, pos)
                enemy_group.add(enemy)
                camera_group.add(enemy)

            elif maps[i][j] == '10':
                bottle_hp = Bottle_HP(bottle1_image, pos)
                hp_group.add(bottle_hp)
                camera_group.add(bottle_hp)
            elif maps[i][j] == '11':
                bottle_mp = Bottle_MP(bottle2_image, pos)
                mp_group.add(bottle_mp)
                camera_group.add(bottle_mp)
            elif maps[i][j] == '12':
                chest = Chest(chest_image, pos)
                chest_group.add(chest)
                camera_group.add(chest)
            elif maps[i][j] == '13':
                coin = Coin(coin_image, pos)
                coin_group.add(coin)
                camera_group.add(coin)
            elif maps[i][j] == '14':
                door = Door(door1_image, pos)
                door_group.add(door)
                camera_group.add(door)
            elif maps[i][j] == '15':
                door_2 = Door(door2_image, pos)
                door_group.add(door_2)
                camera_group.add(door_2)
            elif maps[i][j] == '16':
                door_3 = Door(door3_image, pos)
                door_group.add(door_3)
                camera_group.add(door_3)
            elif maps[i][j] == '17':
                door_4 = Door(door4_image, pos)
                door_group.add(door_4)
                camera_group.add(door_4)


            # elif maps[i][j] == '15':
            #     player = Player({'idle': player_image_idle, 'kill': player_image_kill, 'right': player_image_right,
            #                          'forward': player_image_forward})
            #     player_group.add(player)
            #     camera_group.add(player)



class Wall (pygame.sprite.Sprite):
    def __init__(self,image, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def update(self, stepx, stepy):
        self.collide()
        self.rect.x += stepx
        self.rect.y += stepy

    def collide(self):
        if pygame.sprite.spritecollide(self, player_group, False):
            if player.dir == 'left':
                player.rect.left = self.rect.right
            elif player.dir == 'right':
                player.rect.right = self.rect.left
            elif player.dir == 'top':
                player.rect.top = self.rect.bottom
            elif player.dir == 'bottom':
                player.rect.bottom = self.rect.top

class Chest(pygame.sprite.Sprite):
    def __init__(self, image, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = image[0]
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.frame = 0
        self.timer_anime = 0
        self.anime = True

    def update(self, stepx, stepy):
        self.rect.x += stepx
        self.rect.y += stepy
class Coin(pygame.sprite.Sprite):
    def __init__(self, image, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image_list = image
        self.image = self.image_list[0]
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.frame = 0
        self.timer_anime = 0
        self.anime = True

    def update(self, stepx, stepy):
        self.image = self.image_list[self.frame]
        self.animation()
        self.rect.x += stepx
        self.rect.y += stepy

    def animation(self):
        if self.anime:
            self.timer_anime += 1
            if self.timer_anime / FPS > 0.2:
                if self.frame == len(self.image_list) - 1:
                    self.frame = 0
                else:
                    self.frame += 1
                self.timer_anime = 0
class Door(pygame.sprite.Sprite):
    def __init__(self, image, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.frame = 0
        self.timer_anime = 0
        self.anime = True

    def update(self, stepx, stepy):
        self.rect.x += stepx
        self.rect.y += stepy
class Enemy(pygame.sprite.Sprite):
    def __init__(self, image, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = image[0]
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.frame = 0
        self.timer_anime = 0
        self.anime = True

    def update(self, stepx, stepy):
        self.rect.x += stepx
        self.rect.y += stepy

class Bottle_MP(pygame.sprite.Sprite):
    def __init__(self, image, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.frame = 0
        self.timer_anime = 0
        self.anime = True
    def update(self, stepx, stepy):
        self.rect.x += stepx
        self.rect.y += stepy

class Bottle_HP(pygame.sprite.Sprite):
    def __init__(self, image, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.frame = 0
        self.timer_anime = 0
        self.anime = True
    def update(self, stepx, stepy):
        self.rect.x += stepx
        self.rect.y += stepy
class Wizard(pygame.sprite.Sprite):
    def __init__(self, image, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image_list = image
        self.image = self.image_list[0]
        # self.image = self.image_list[self.frame]
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.frame = 0
        self.timer_anime = 0
        self.anime = True

    def update(self, stepx, stepy):
        self.image = self.image_list[self.frame]
        self.animation()
        self.rect.x += stepx
        self.rect.y += stepy

    def animation(self):
        if self.anime:
            self.timer_anime += 1
            if self.timer_anime / FPS > 0.5:
                if self.frame == len(self.image_list) - 1:
                    self.frame = 0
                else:
                    self.frame += 1
                self.timer_anime = 0


class Player (pygame.sprite.Sprite):
    def __init__(self, image_lists, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image_lists = image_lists
        self.image = self.image_lists['idle'][0]
        self.current_list_image = self.image_lists['idle']
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.anime_idle = True
        self.anime_run = False
        self.anime_atk = False
        self.anime_forward = False
        self.anime_up = False
        self.frame = 0
        self.timer_anime = 0
        self.dir = 'right'
        self.hp = 100
        self.mp = 100
        self.mask = pygame.mask.from_surface(self.image)
        self.mask_outline = self.mask.outline()
        self.mask_list = []
        self.hp_bar = 'blue'
        self.key = pygame.key.get_pressed()

    def move(self):
        if self.key[pygame.K_d]:
            self.rect.x += 2
            self.anime_idle = False
            self.anime_run = True
            self.dir = 'right'
            if self.rect.right > 1000:
                self.rect.right = 1000
                camera_group.update(-self.speed)
        elif self.key[pygame.K_a]:
            self.rect.x -= 2
            self.anime_idle = False
            self.anime_run = True
            self.dir = 'left'
            if self.rect.left < 200:
                self.rect.left = 200
                camera_group.update(self.speed)
        elif self.key[pygame.K_w]:
            self.rect.y -= 2
            self.dir = 'up'
            self.anime_idle = False
            self.anime_up = True
            if self.rect.top < 200:
                self.rect.top = 200
                camera_group.update(0, self.speed)
        elif self.key[pygame.K_s]:
            self.rect.y += 2
            self.dir = 'bottom'
            self.anime_idle = False
            self.anime_forward = True
            if self.rect.top > 1000:
                self.rect.top = 1000
                camera_group.update(0, -self.speed)

    def animation(self):
        self.timer_anime += 2
        if self.timer_anime / FPS > 0.1:
            if self.frame == len(self.current_list_image) - 1:
                self.frame = 0
                if self.anime_atk:
                    self.current_list_image = player_image_idle
                    self.anime_atk = False
                    self.anime_idle = True
            else:
                self.frame += 1
            self.timer_anime = 0
        if self.anime_idle:
            self.current_list_image = self.image_lists['idle']
            self.mask = pygame.mask.from_surface(self.image)
            self.mask_outline = self.mask.outline()
            self.mask_list = []
        elif self.anime_run:
            self.current_list_image = self.image_lists['run']
            self.mask = pygame.mask.from_surface(self.image)
            self.mask_outline = self.mask.outline()
            self.mask_list = []
        elif self.anime_atk:
            self.current_list_image = self.image_lists['atk']
            self.mask = pygame.mask.from_surface(self.image)
            self.mask_outline = self.mask.outline()
            self.mask_list = []
        elif self.anime_up:
            self.current_list_image = self.image_lists['up']
            self.mask = pygame.mask.from_surface(self.image)
            self.mask_outline = self.mask.outline()
            self.mask_list = []
        elif self.anime_forward:
            self.current_list_image = self.image_lists['forward']
            self.mask = pygame.mask.from_surface(self.image)
            self.mask_outline = self.mask.outline()
            self.mask_list = []
        try:
            if self.dir == 'right':
                self.image = self.current_list_image[self.frame]
            elif self.dir == 'up':
                self.image = self.current_list_image[self.frame]
            elif self.dir == 'bottom':
                self.image = self.current_list_image[self.frame]
            else:
                self.image = pygame.transform.flip(self.current_list_image[self.frame], True, False)
        except:
            self.frame = 0

    def maska_k(self):
        self.mask_list = []
        for i in self.mask_outline:
            self.mask_list.append((i[0] + self.rect.x, i[1] + self.rect.y))
        for point in self.mask_list:
            x = point[0]
            y = point[1]
            pygame.draw.circle(sc, 'blue', (x, y), 5)
    def upddate(self):
        self.move()
        self.animation()
        self.maska_k()

def restart():
    global player_group,  wizard_group, enemy_group, mp_group, hp_group, door_group, chest_group, wall_group, camera_group, player, coin_group
    player_group = pygame.sprite.Group()
    wizard_group = pygame.sprite.Group()
    enemy_group = pygame.sprite.Group()
    mp_group = pygame.sprite.Group()
    hp_group = pygame.sprite.Group()
    door_group = pygame.sprite.Group()
    chest_group = pygame.sprite.Group()
    wall_group = pygame.sprite.Group()
    camera_group = pygame.sprite.Group()
    player = Player({'idle': player_image_idle, 'kill': player_image_kill, 'right': player_image_right,
                                              'forward': player_image_forward, 'up': player_image_up}, (100, 100))
    player_group.add(player)
    coin_group = pygame.sprite.Group()
    camera_group.add(player)



restart()
drawMaps('level1_1.txt')
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    game_lvl()
    clock.tick(FPS)
