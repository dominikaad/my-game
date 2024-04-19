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
lvl_game = 1
lvl = 'menu'
all_score = 0
font = pygame.font.SysFont('Aria', 30)
s = pygame.font.SysFont('Aria', 120)
q = pygame.font.SysFont('Aria', 70)
sc = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
from load import *

def game_lvl():
    sc.fill('grey')
    floor_group.draw(sc)
    floor_group.update(0,0)
    topor_group.update()
    topor_group.draw(sc)


    enemy_group.draw(sc)
    enemy_group.update()
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
    player_group.draw(sc)
    player_group.update()
    enemy_boss_group.draw(sc)
    enemy_boss_group.update(0,0)
    wizard_group.draw(sc)
    wizard_group.update(0,0)
    key_group.draw(sc)
    key_group.update(0,0)
    text_render = font.render('SCORE:' + str(player.score), True, 'black')
    sc.blit(text_render, (10, 10))
    text_render = q.render('LEVEL:' + str(lvl_game), True, 'black')
    sc.blit(text_render, (400, 10))
    if lvl_game == 3:
        sc.blit(fog_image,(player.rect.center[0] - 2060, player.rect.center[1] - 2060))
    pygame.display.update()
def drawMaps(nameFile):
    maps = []
    source = 'game_lvl/' + str(nameFile)
    with open(source, 'r') as file:
        for i in range(0, 80):
            maps.append(file.readline().replace('\n', '').split(',')[0:-1])

    pos = [0, 0]
    for i in range(0, len(maps)):
        pos[1] = i * 32
        for j in range(0, len(maps[0])):
            pos[0] = 32 * j
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
            elif maps[i][j] == '6':
                enemy = Enemy({'idle': enemy_image_idle, 'kill': enemy_image_kill, 'right': enemy_image_right, 'left': enemy_image_left}, pos)
                enemy_group.add(enemy)
                camera_group.add(enemy)
            elif maps[i][j] == '7':
                bottle_hp = Bottle_HP(bottle1_image, pos)
                hp_group.add(bottle_hp)
                camera_group.add(bottle_hp)
            elif maps[i][j] == '8':
                floor = Floor(floor_image, pos)
                floor_group.add(floor)
                camera_group.add(floor)
            elif maps[i][j] == '9':
                chest = Chest(chest_image, pos)
                chest_group.add(chest)
                camera_group.add(chest)
            elif maps[i][j] == '10':
                coin = Coin(coin_image, pos)
                coin_group.add(coin)
                camera_group.add(coin)
            elif maps[i][j] == '15':
                door = Door(door1_image, pos)
                door_group.add(door)
                camera_group.add(door)
            elif maps[i][j] == '17':
                door_2 = Door(door2_image, pos)
                door_group.add(door_2)
                camera_group.add(door_2)
            elif maps[i][j] == '18':
                enemy_boss = Enemy_boss(slime_big1_image, pos)
                enemy_boss_group.add(enemy_boss)
                camera_group.add(enemy_boss)




class Wall (pygame.sprite.Sprite):
    def __init__(self,image, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.speedx = 0
        self.speedy = 0
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
            elif player.dir == 'up':
                player.rect.top = self.rect.bottom
            elif player.dir == 'bottom':
                player.rect.bottom = self.rect.top
    def camera_move(self, stepx, stepy):
        self.rect.x += stepx + self.speedx
        self.rect.y += stepy + self.speedy
class Floor (pygame.sprite.Sprite):
    def __init__(self,image, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.speedx = 0
        self.speedy = 0
    def update(self, stepx, stepy):
        self.rect.x += stepx
        self.rect.y += stepy
    def camera_move(self, stepx, stepy):
        self.rect.x += stepx + self.speedx
        self.rect.y += stepy + self.speedy
class Chest(pygame.sprite.Sprite):
    def __init__(self, image, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image_list = image
        self.image = self.image_list[0]
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.frame = 0
        self.timer_anime = 0
        self.anime = False
        self.speedx = 0
        self.speedy = 0
        self.score_key = 0
    def update(self, stepx, stepy):
        self.image = self.image_list[self.frame]
        self.rect.x += stepx
        self.rect.y += stepy
        self.animation()
        if pygame.sprite.spritecollide(self, player_group, False):
            self.anime = True

    def camera_move(self, stepx, stepy):
        self.rect.x += stepx + self.speedx
        self.rect.y += stepy + self.speedy
    def animation(self):
        if self.anime:
            self.timer_anime += 1
            if self.timer_anime / FPS > 0.2:
                if self.frame == len(self.image_list) - 1:
                    self.frame = 0
                    player.keys += 1
                    key = Key(key_image, (player.keys*40,40))
                    key_group.add(key)
                    self.kill()
                else:
                    self.frame += 1
                self.timer_anime = 0

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
        self.speedx = 0
        self.speedy = 0

    def update(self, stepx, stepy):
        self.image = self.image_list[self.frame]
        self.animation()
        self.rect.x += stepx
        self.rect.y += stepy
        if pygame.sprite.spritecollide(self, player_group, False):
            player.score += 10
            # all_score += player.score
            self.kill()


    def camera_move(self, stepx, stepy):
        self.rect.x += stepx + self.speedx
        self.rect.y += stepy + self.speedy
    def animation(self):
        if self.anime:
            self.timer_anime += 1
            if self.timer_anime / FPS > 0.15:
                if self.frame == len(self.image_list) - 1:
                    self.frame = 0
                else:
                    self.frame += 1
                self.timer_anime = 0

class Key(pygame.sprite.Sprite):
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
        self.speedx = 0
        self.speedy = 0

    def update(self, stepx, stepy):
        self.animation()
        self.rect.x += stepx
        self.rect.y += stepy
    def camera_move(self, stepx, stepy):
        self.rect.x += stepx + self.speedx
        self.rect.y += stepy + self.speedy

    def animation(self):
        if self.anime:
            self.image = self.image_list[self.frame]
            self.timer_anime += 1
            if self.timer_anime / FPS > 0.2:
                if self.frame == len(self.image_list) - 1:
                    self.frame = 0
                else:
                    self.frame += 1
                self.timer_anime = 0
class Enemy_boss(pygame.sprite.Sprite):
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
        self.speedx = 0
        self.speedy = 0
        self.timer = 0
        self.hp = 100

    def update(self, stepx, stepy):
        self.image = self.image_list[self.frame]
        self.animation()
        self.draw_stats()
        self.life()
        self.rect.x += stepx
        self.rect.y += stepy
        if 0< self.rect.centerx < 1200 and 0 < self.rect.centery <800:
            self.timer += 1
        if self.timer / FPS > 2:
            enemy = Enemy({'idle': enemy_image_idle, 'kill': enemy_image_kill, 'right': enemy_image_right,
                           'left': enemy_image_left}, self.rect.center)
            enemy_group.add(enemy)
            camera_group.add(enemy)
            self.timer = 0

    def animation(self):
        if self.anime:
            self.timer_anime += 1
            if self.timer_anime / FPS > 0.7:
                if self.frame == len(self.image_list) - 1:
                    self.frame = 0
                else:
                    self.frame += 1
                self.timer_anime = 0
    def draw_stats(self):
        width_hp = 96 * (self.hp/100)
        # width_mp = 96 * (self.mp / 100)
        pygame.draw.rect(sc,'black', (self.rect.x - 30, self.rect.y - 52, 100,20), 2)
        pygame.draw.rect(sc,'red', (self.rect.x - 27, self.rect.y - 50, width_hp, 15))

        # pygame.draw.rect(sc, 'black', (self.rect.x - 30, self.rect.y - 30, 100, 10), 2)
        # pygame.draw.rect(sc, 'blue', (self.rect.x - 27, self.rect.y - 27, width_mp, 6))
        if self.hp<1:
            self.kill()
    def life(self):
        if pygame.sprite.spritecollide(self, topor_group, False):
            self.hp -= 1

    def camera_move(self, stepx, stepy):
        self.rect.x += stepx + self.speedx
        self.rect.y += stepy + self.speedy
class Door(pygame.sprite.Sprite):
    def __init__(self, image, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        # self.frame = 0
        # self.timer_anime = 0
        # self.anime = True
        self.speedx = 0
        self.speedy = 0
        self.open = False
    def update(self, stepx, stepy):
        self.rect.x += stepx
        self.rect.y += stepy
        self.collide()
    def collide(self):

        if pygame.sprite.spritecollide(self, player_group, False) and self.open == False and player.keys>0:
            self.open = True
            player.keys -= 1
            for i in key_group:
                pass
            else:
                i.kill()
        if self.open == False:
            if pygame.sprite.spritecollide(self, player_group, False):
                if player.dir == 'left':
                    player.rect.left = self.rect.right
                elif player.dir == 'right':
                    player.rect.right = self.rect.left
                elif player.dir == 'up':
                    player.rect.top = self.rect.bottom
                elif player.dir == 'bottom':
                    player.rect.bottom = self.rect.top
        # else:
        #     player.keys -= 1
        #
    def camera_move(self, stepx, stepy):
        self.rect.x += stepx + self.speedx
        self.rect.y += stepy + self.speedy
class Enemy(pygame.sprite.Sprite):
    def __init__(self,image_lists, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image_lists = image_lists
        self.image = self.image_lists['idle'][0]
        self.current_list_image = self.image_lists['idle']
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.frame = 0
        self.timer_anime = 0
        self.anime = True
        self.speedx = 0
        self.speedy = 0
        self.speed = 1
        self.anime_idle = True
        self.anime_right = False
        self.anime_kill = False
        self.anime_left = False
        self.trigger = False
        self.atack_dir = ''
        self.frame = 0
        self.move = True
        self.timer_anime = 0
        self.dir = 'top'
        self.timer_move = 0
        self.mask = pygame.mask.from_surface(self.image)
        self.mask_outline = self.mask.outline()
        self.mask_list = []
        self.timer_trigger = 0
    def update(self):
        if 0<self.rect.centerx<WIDTH and 0 <self.rect.centery<HEIGHT:
            d = ((self.rect.center[0] - player.rect.center[0]) ** 2
                 + (self.rect.center[1] - player.rect.center[1])** 2) ** (1/2)
            self.animation()
            self.maska_k()
            self.collide()
        else:
            d = 0
        self.timer_move += 1
        if self.move and self.timer_move / FPS > 1.2:
            if random.randint(1, 4) == 1:
                self.dir = 'top'
            if random.randint(1, 4) == 2:
                self.dir = 'bottom'
            if random.randint(1, 4) == 3:
                self.dir = 'right'
            if random.randint(1, 4) == 4:
                self.dir = 'left'
            self.timer_move = 0
        if self.move :
            if self.dir == 'top':
                self.anime_idle = True
                self.anime_right = False
                self.anime_left = False
                self.anime_kill = False
                self.rect.y -= self.speed
            if self.dir == 'bottom':
                self.anime_idle = True
                self.anime_right = False
                self.anime_left = False
                self.anime_kill = False
                self.rect.y += self.speed
            if self.dir == 'right':
                self.anime_right = True
                self.anime_idle = False
                self.anime_left = False
                self.anime_kill = False
                self.rect.x += self.speed
            if self.dir == 'left':
                self.anime_right = False
                self.anime_idle = False
                self.anime_left = True
                self.anime_kill = False
                self.rect.x -= self.speed

        if pygame.sprite.spritecollide(self, wall_group, False) or pygame.sprite.spritecollide(self, door_group,
                                                                                                False) or pygame.sprite.spritecollide(
                self, chest_group, False):
            self.trigger = False
            self.timer_move = 0
            if self.dir == 'top':
                self.dir = 'bottom'
            elif self.dir == 'bottom':
                self.dir = 'top'
            elif self.dir == 'right':
                self.dir = 'left'
            elif self.dir == 'left':
                self.dir = 'right'
        if not self.trigger:
            self.timer_trigger += 1
        if d < 230 and self.timer_trigger/FPS>1:
            self.timer_trigger = 0
            self.trigger = True
        else:
            self.trigger= False
        if self.trigger:
            pos_player = player.rect.center
            pos = self.rect.center
            if pos[0]-pos_player[0] > 0:
                if pos[1] - pos_player[1]> 0:
                    self.atack_dir = ('left', 'top')
                else:
                    self.atack_dir = ('left', 'bottom')
            else:
                if pos[1] - pos_player[1]> 0:
                    self.atack_dir = ('right', 'top')
                else:
                    self.atack_dir = ('right', 'bottom')
            if self.atack_dir == ('left', 'top'):
                self.dir = 'left'
                if abs(pos[0] - pos_player[0]) < 20:
                    self.dir = 'top'
            elif self.atack_dir == ('left', 'bottom'):
                self.dir = 'left'
                if abs(pos[0] - pos_player[0]) < 20:
                    self.dir = 'bottom'
            elif self.atack_dir == ('right', 'top'):
                self.dir = 'right'
                if abs(pos[0] - pos_player[0]) < 20:
                    self.dir = 'top'
            elif self.atack_dir == ('right', 'bottom'):
                self.dir = 'right'
                if abs(pos[0] - pos_player[0]) < 20:
                    self.dir = 'bottom'
    def camera_move(self, stepx, stepy):
        self.rect.x += stepx + self.speedx
        self.rect.y += stepy + self.speedy

    def animation(self):
        self.timer_anime += 2
        if self.timer_anime / FPS > 0.1:
            if self.frame == len(self.current_list_image) - 1:
                self.frame = 0
                if self.anime_kill:
                    self.current_list_image = player_image_idle
                    self.anime_kill = False
                    self.anime_idle = True
                    self.kill()
            else:
                self.frame += 1
            self.timer_anime = 0
        if self.anime_idle:
            self.current_list_image = self.image_lists['idle']
            self.mask = pygame.mask.from_surface(self.image)
            self.mask_outline = self.mask.outline()
            self.mask_list = []
        elif self.anime_right:
            self.current_list_image = self.image_lists['right']
            self.mask = pygame.mask.from_surface(self.image)
            self.mask_outline = self.mask.outline()
            self.mask_list = []
        elif self.anime_left:
            self.current_list_image = self.image_lists['left']
            self.mask = pygame.mask.from_surface(self.image)
            self.mask_outline = self.mask.outline()
            self.mask_list = []
        elif self.anime_kill:
            self.current_list_image = self.image_lists['kill']
            self.mask = pygame.mask.from_surface(self.image)
            self.mask_outline = self.mask.outline()
            self.mask_list = []
        try:

            self.image = self.current_list_image[self.frame]

        except:
            self.frame = 0

    def maska_k(self):
        self.mask_list = []
        for i in self.mask_outline:
            self.mask_list.append((i[0] + self.rect.x, i[1] + self.rect.y))
        #for point in self.mask_list:
        #    x = point[0]
        #    y = point[1]
        #    # pygame.draw.circle(sc, 'red', (x, y), 1)
#
    def collide(self):

        if pygame.sprite.spritecollide(self, topor_group, False):
            self.anime_kill = True
            self.anime_idle = False
            self.anime_right = False
            self.anime_left= False
            self.move = False
            # self.kill()
# class Bottle_MP(pygame.sprite.Sprite):
#     def __init__(self, image, pos):
#         pygame.sprite.Sprite.__init__(self)
#         self.image = image
#         self.rect = self.image.get_rect()
#         self.rect.x = pos[0]
#         self.rect.y = pos[1]
#         self.frame = 0
#         self.timer_anime = 0
#         self.anime = True
#         self.speedx = 0
#         self.speedy = 0
#     def update(self, stepx, stepy):
#         self.rect.x += stepx
#         self.rect.y += stepy
#         if pygame.sprite.spritecollide(self, player_group, False):
#             self.kill()
#             if player.mp < 70:
#                 player.mp += 30
#             else:
#                 player.mp = 100
#     def camera_move(self, stepx, stepy):
#         self.rect.x += stepx + self.speedx
#         self.rect.y += stepy + self.speedy

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
        self.speedx = 0
        self.speedy = 0
    def update(self, stepx, stepy):
        self.rect.x += stepx
        self.rect.y += stepy
        if pygame.sprite.spritecollide(self, player_group, False):
            self.kill()
            if player.hp < 70:
                player.hp += 30
            else:
                player.hp = 100
    def camera_move(self, stepx, stepy):
        self.rect.x += stepx + self.speedx
        self.rect.y += stepy + self.speedy
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
        self.speedx = 0
        self.speedy = 0

    def update(self, stepx, stepy):
        self.image = self.image_list[self.frame]
        self.animation()
        self.collide()
        self.rect.x += stepx
        self.rect.y += stepy

    def collide(self):
        if pygame.sprite.spritecollide(self, player_group, False):
            if lvl_game == 1:
                sc.blit(goal_1_image, (340, 340))
            elif lvl_game == 2:
                sc.blit(goal_2_image, (340, 340))

    def animation(self):
        if self.anime:
            self.timer_anime += 1
            if self.timer_anime / FPS > 0.5:
                if self.frame == len(self.image_list) - 1:
                    self.frame = 0
                else:
                    self.frame += 1
                self.timer_anime = 0

    def camera_move(self, stepx, stepy):
        self.rect.x += stepx + self.speedx
        self.rect.y += stepy + self.speedy

class SUPER_GROUP(pygame.sprite.Group):
    def camera_move(self, *args, **kwargs):
        for sprite in self.sprites():
            sprite.camera_move(*args, **kwargs)

class Topor(pygame.sprite.Sprite):
    def __init__(self, image, pos, start_deg):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.centerx = pos[0]
        self.rect.centery = pos[1]
        self.deg_rotate = 0
        self.deg = start_deg
        self.timer_attack = 0
    def update(self):
        self.rotate()
        self.move()
    def rotate(self):
        self.deg_rotate -= 20
        self.image = pygame.transform.rotate(topor_image, self.deg_rotate)

    def move(self):
        self.deg += 3
        self.rect.centerx = 100 * cos(radians(self.deg)) + player.rect.centerx
        self.rect.centery = 100 * sin(radians(self.deg)) + player.rect.centery
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
        self.anime_right = False
        self.anime_left = False
        # self.anime_atk = False
        self.anime_forward = False
        self.anime_up = False
        self.frame = 0
        self.timer_anime = 0
        self.dir = 'right'
        self.hp = 100
        # self.mp = 100
        self.score = 0
        self.speed = 7
        self.topor = 1
        self.mask = pygame.mask.from_surface(self.image)
        self.mask_outline = self.mask.outline()
        self.mask_list = []
        self.hp_bar = 'blue'
        self.key = pygame.key.get_pressed()
        self.add_topor()
        self.keys = 0

    def move(self):
        if self.key[pygame.K_d]:
            self.rect.x += 7
            self.anime_idle = False
            self.anime_right = True
            self.anime_left =False
            self.dir = 'right'
            if self.rect.right > 800:
                self.rect.right = 800
                camera_group.camera_move(-self.speed, 0)
        elif self.key[pygame.K_a]:
            self.rect.x -= 7
            self.anime_idle = False
            self.anime_left = True
            self.anime_right= False
            self.dir = 'left'
            if self.rect.left < 200:
                self.rect.left = 200
                camera_group.camera_move(self.speed, 0)
        elif self.key[pygame.K_w]:
            self.rect.y -= 7
            self.anime_idle = False
            self.anime_up = True
            self.anime_forward = False
            self.dir = 'up'
            if self.rect.top < 200:
                self.rect.top = 200
                camera_group.camera_move(0, self.speed)
        elif self.key[pygame.K_s]:
            self.rect.y += 7
            self.anime_idle = False
            self.anime_forward = True
            self.anime_up = False
            self.dir = 'bottom'
            if self.rect.top > 600:
                self.rect.top = 600
                camera_group.camera_move(0, -self.speed)
        else:
            self.anime_right = False
            self.anime_idle = True

    def animation(self):
        self.timer_anime += 2
        if self.timer_anime / FPS > 0.1:
            if self.frame == len(self.current_list_image) - 1:
                self.frame = 0
                # if self.anime_atk:
                #     self.current_list_image = player_image_idle
                #     # self.anime_atk = False
                #     self.anime_idle = True
            else:
                self.frame += 1
            self.timer_anime = 0
        if self.anime_idle:
            self.current_list_image = self.image_lists['idle']
            self.mask = pygame.mask.from_surface(self.image)
            self.mask_outline = self.mask.outline()
            self.mask_list = []
        elif self.anime_right:
            self.current_list_image = self.image_lists['right']
            self.mask = pygame.mask.from_surface(self.image)
            self.mask_outline = self.mask.outline()
            self.mask_list = []
        elif self.anime_left:
            self.current_list_image = self.image_lists['left']
            self.mask = pygame.mask.from_surface(self.image)
            self.mask_outline = self.mask.outline()
            self.mask_list = []
        # elif self.anime_atk:
        #     self.current_list_image = self.image_lists['atk']
        #     self.mask = pygame.mask.from_surface(self.image)
        #     self.mask_outline = self.mask.outline()
        #     self.mask_list = []
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
            elif self.dir == 'left':
                self.image = self.current_list_image[self.frame]
        except:
            self.frame = 0

    def maska_k(self):
        self.mask_list = []
        for i in self.mask_outline:
            self.mask_list.append((i[0] + self.rect.x, i[1] + self.rect.y))
        for point in self.mask_list:
            x = point[0]
            y = point[1]
            # pygame.draw.circle(sc, 'blue', (x, y), 1)

    def draw_stats(self):
        width_hp = 96 * (self.hp/100)
        # width_mp = 96 * (self.mp / 100)
        pygame.draw.rect(sc,'black', (self.rect.x - 30, self.rect.y - 52, 100,20), 2)
        pygame.draw.rect(sc,'green', (self.rect.x - 27, self.rect.y - 50, width_hp, 15))

        # pygame.draw.rect(sc, 'black', (self.rect.x - 30, self.rect.y - 30, 100, 10), 2)
        # pygame.draw.rect(sc, 'blue', (self.rect.x - 27, self.rect.y - 27, width_mp, 6))
        if self.hp<1:
            self.kill()
            pygame.quit()
            sys.exit()

    def life(self):
        if pygame.sprite.spritecollide(self, enemy_group, False):
            self.hp -= 0.1
    def next_level(self):
        global lvl_game
        if lvl_game == 1 and self.score > 2739 and pygame.sprite.spritecollide(self, wizard_group, False):
            lvl_game += 1
            restart()
            drawMaps(str(lvl_game) + '_0.txt')
            drawMaps(str(lvl_game)+ '.txt')
        if lvl_game == 2 and len(enemy_boss_group) == 0:
            lvl_game += 1
            restart()
            drawMaps('2_0.txt')
            drawMaps('2.txt')

    def add_topor(self):
        global topor_group
        topor_group = pygame.sprite.Group()
        for i in range(self.topor):
            topor = Topor(topor_image, (self.rect.centerx + 70, self.rect.centery + 70), (360 // self.topor * i))
            topor_group.add(topor)
    def update(self):
        self.maska_k()
        self.key = pygame.key.get_pressed()
        self.move()
        self.animation()
        self.draw_stats()
        self.life()
        self.next_level()


def startMenu():
    sc.fill('grey')
    button_group.draw(sc)
    button_group.update()
    text_rend = s.render('WELCOME!', True, 'black')
    sc.blit(text_rend, (250, 100))
    # text_render = font.render('SCORE:' + str(all_score), True, 'black')
    # sc.blit(text_render, (10, 10))
    pygame.display.update()
class Button (pygame.sprite.Sprite):
    def __init__(self, image, pos, next_lvl, text):
        pygame.sprite.Sprite.__init__(self)
        self.image_list = image
        self.image = self.image_list[0]
        self.rect = self.image.get_rect()
        self.rect.topleft = pos
        self.next_lvl = next_lvl
        self.time = 0
        self.frame = 0
        self.timer_anime = 0
        self.anime = False
    def update(self):
        self.time += 1
        global lvl
        click = pygame.mouse.get_pos()
        self.animation()
        if pygame.mouse.get_pressed()[0]:
            if self.rect.left <click[0] < self.rect.right and self.rect.top < click[1] < self.rect.bottom:
                self.anime = True



    def animation(self):
        global lvl
        if self.anime:
            self.image = self.image_list[self.frame]
            print(self.frame)
            self.timer_anime += 1
            if self.timer_anime / FPS > 0.2:
                if self.frame == len(self.image_list) - 1:
                    self.frame = 0
                    lvl = self.next_lvl
                    if lvl == 'game':
                        restart()
                        drawMaps('1_0.txt')
                        drawMaps('1.txt')
                    elif lvl == 'end':
                        pygame.quit()
                        sys.exit()
                else:
                    self.frame += 1
                self.timer_anime = 0



def restart():
    global player_group,  wizard_group, enemy_group, mp_group, hp_group,enemy_boss_group,door_group,floor_group,button_group, chest_group, wall_group, camera_group, player, coin_group,key_group, topor_group
    player_group = pygame.sprite.Group()
    topor_group = pygame.sprite.Group()
    wizard_group = pygame.sprite.Group()
    enemy_group = pygame.sprite.Group()
    mp_group = pygame.sprite.Group()
    hp_group = pygame.sprite.Group()
    door_group = pygame.sprite.Group()
    chest_group = pygame.sprite.Group()
    wall_group = pygame.sprite.Group()
    camera_group = SUPER_GROUP()
    enemy_boss_group = pygame.sprite.Group()
    player = Player({'idle': player_image_idle, 'right': player_image_right,'left': player_image_left,
                                              'forward': player_image_forward, 'up': player_image_up}, (200, 200))
    player_group.add(player)
    coin_group = pygame.sprite.Group()
    key_group = pygame.sprite.Group()
    floor_group = pygame.sprite.Group()

button_group = pygame.sprite.Group()
button_start = Button(button_play_image, (600,500), 'game', 'start')
button_group.add(button_start)
button_exit = Button(button_exit_image, (200,500), 'end', 'exit')
button_group.add(button_exit)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    if lvl == 'game':
        game_lvl()
    elif lvl == 'menu':
        startMenu()
    elif lvl == 'exit':
        pygame.quit()
        sys.exit()
    clock.tick(FPS)



# restart()
# drawMaps('level_1_0_last1.txt')
# drawMaps('level_1_last1.txt')
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             sys.exit()
#     game_lvl()
#     clock.tick(FPS)
