import pygame
import os
import sys
import random
pygame.init()
current_path = os.path.dirname(__file__)
os.chdir(current_path)
WIDTH = 1200
HEIGHT = 800
FPS = 60
sc = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
font = pygame.font.SysFont('Aria', 50)
from load import *

def game_lvl():
    sc.fill('grey')
    player_group.draw(sc)
    player_group.update
    wizard_group.draw(sc)
    wizard_group.update
    enemy_group.draw(sc)
    enemy_group.update
    mp_group.draw(sc)
    mp_group.update
    hp_group.draw(sc)
    hp_group.update
    lever_group.draw(sc)
    lever_group.update
    chest_group.draw(sc)
    chest_group.update
    wall_group.draw(sc)
    wall_group.update(0)
    pygame.display.update()

    def drawMaps(nameFile):
        maps = []
        source = 'game_lvl/' + str(nameFile)
        with open(source, 'r') as file:
            for i in range(0, 10):
                maps.append(file.readline().replace('\n', '').split(',')[0:-1])

        pos = [0, 0]
        for i in range(0, len(maps)):
            pos[1] = i * 80
            for j in range(0, len(maps[0])):
                pos[0] = 80 * j
                if maps[i][j] == '5':
                    wall1 = Wall(wall1_image_image, pos)
                    wall_group.add(wall1)
                    camera_group.add(wall1)
                elif maps[i][j] == '6':
                    wall2 = Wall(wall2_image, pos)
                    wall_group.add(wall2)
                    camera_group.add(wall2)
                elif maps[i][j] == '7':
                    wall3 = Wall(wall3_image, pos)
                    wall_group.add(wall3)
                    camera_group.add(wall3)
                elif maps[i][j] == '8':
                    wall4 = Wall(wall4_image, pos)
                    wall_group.add(wall4)
                    camera_group.add(wall4)
                elif maps[i][j] == '9':
                    chest = Chest(chest_image, pos)
                    chest_group.add(chest)
                    camera_group.add(chest)
                elif maps[i][j] == '11':
                    lever = Lever(lever_image, pos)
                    lever_group.add(lever)
                    camera_group.add(lever)
                elif maps[i][j] == '12':
                    bottle_hp = Bottle_HP(bottle1_image, pos)
                    hp_group.add(bottle_hp)
                    camera_group.add(bottle_hp)
                elif maps[i][j] == '13':
                    bottle_mp = Bottle_MP(bottle2_image, pos)
                    mp_group.add(bottle_mp)
                    camera_group.add(bottle_mp)
                elif maps[i][j] == '14':
                    enemy = Enemy({'idle':enemy_image_idle, 'kill': enemy_image_kill, 'right': enemy_image_right})
                    enemy_group.add(enemy)
                    camera_group.add(enemy)
                elif maps[i][j] == '15':
                    player = Player({'idle':player_image_idle, 'kill': player_image_kill, 'right': player_image_right, 'forward': player_image_forward})
                    player_group.add(player)
                    camera_group.add(player)
                elif maps[i][j] == '16':
                    wizard = Wizard(wizard_image, pos)
                    wizard_group.add(wizard)
                    camera_group.add(wizard)

class Wall (pygame.sprite.Sprite):
    def __init__(self,image, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def update(self, step):
        self.rect.x += step
        if pygame.sprite.spritecollide(self, player_group, False):
            if abs(self.rect.top - player.rect.bottom) < 15:
                player.rect.bottom = self.rect.top - 5
                player.on_ground = True
            if abs(self.rect.bottom - player.rect.top) < 15:
                player.rect.top = self.rect.bottom + 5
                player.velocity_y = 0
            if (abs(self.rect.left - player.rect.right) < 15
                    and abs(self.rect.centery - player.rect.centery) < 50):
                player.rect.right = self.rect.left
            if (abs(self.rect.right - player.rect.left) < 15
                    and abs(self.rect.centery - player.rect.centery) < 50):
                player.rect.left = self.rect.right

class Wizard (pygame.sprite.Sprite):
    def __init__(self, image, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = image[0]
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.frame = 0
        self.timer_anime = 0
        self.anime = True

    def update(self):
        self.animation()
    def animation(self):
        if self.anime:
            self.timer_anime += 1
            if self.timer_anime / FPS > 0.1:
                if self.frame == len(player_image) - 1:
                    self.frame = 0
                else:
                    self.frame += 1
                self.timer_anime = 0

class Player (pygame.sprite.Sprite):
    def __init__(self, image_lists):
        pygame.sprite.Sprite.__init__(self)
        self.image_lists = image_lists
        self.image = self.image_lists['idle'][0]
        self.current_list_image = self.image_lists['idle']
        self.rect = self.image.get_rect()
        self.anime_idle = True
        self.anime_run = False
        self.anime_atk = False
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
            if self.rect.right > 1000:
                self.rect.right = 1000
                camera_group.update(-self.speed)
        elif self.key[pygame.K_a]:
            self.rect.x -= 2
            self.anime_idle = False
            self.anime_run = True
            if self.rect.left < 200:
                self.rect.left = 200
                camera_group.update(self.speed)
        elif self.key[pygame.K_w]:
            self.rect.y -= 2
            self.anime_idle = False
            self.anime_run = True
            if self.rect.top < 200:
                self.rect.top = 200
                camera_group.update(0, self.speed)
        elif self.key[pygame.K_s]:
            self.rect.y += 2
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
                    self.current_list_image = player1_image_idle
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
        try:
            if self.dir == 'right':
                self.image = self.current_list_image[self.frame]
            else:
                self.image = pygame.transform.flip(self.current_list_image[self.frame], True, False)
        except:
            self.frame = 0

def restart():
    global player_group,  wizard_group, enemy_group, mp_group, hp_group, lever_group, chest_group, wall_group
    player_group = pygame.sprite.Group()
    wizard_group = pygame.sprite.Group()
    enemy_group = pygame.sprite.Group()
    mp_group = pygame.sprite.Group()
    hp_group = pygame.sprite.Group()
    lever_group = pygame.sprite.Group()
    chest_group = pygame.sprite.Group()
    wall_group = pygame.sprite.Group()



restart()
drawMaps('1.txt')
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    game_lvl()
    clock.tick(FPS)