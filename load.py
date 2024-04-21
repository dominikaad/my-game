import pygame
from script import load_image
wall1_image = pygame.image.load('image/blocks/Wall1.png').convert_alpha()
wall2_image = pygame.image.load('image/blocks/Wall2.png').convert_alpha()
wall3_image = pygame.image.load('image/blocks/Wall3.png').convert_alpha()
wall4_image = pygame.image.load('image/blocks/Wall4.png').convert_alpha()
lever_image = load_image('image/decorate/lever', True,2)
chest_image = load_image('image/decorate/chest', True,2)
coin_image = load_image('image/decorate/coin', True,2)
bottle1_image = pygame.image.load('image/decorate/Bottle_1.png').convert_alpha()
# bottle2_image = pygame.image.load('image/decorate/Bottle_2.png').convert_alpha()
wizard_image = load_image('image/wizard', True,2)
player_image_idle = load_image('image/player_2/idle', True,0.5)
player_image_forward = load_image('image/player_2/bottom', True,0.5)
# player_image_kill = load_image('image/player/kill', True,2)
player_image_right = load_image('image/player_2/right', True,0.5)
player_image_left = load_image('image/player_2/left',True,0.5)
player_image_up = load_image('image/player_2/top', True,0.5)
enemy_image_idle = load_image('image/enemy/iddle',True,2.5)
enemy_image_kill = load_image('image/enemy/kill',True,2.5)
enemy_image_right = load_image('image/enemy/right',True,2.5)
enemy_image_left = load_image('image/enemy/left',True,2.5)
# door1_image = pygame.image.load('image/blocks/Door.png').convert_alpha()
# door2_image = pygame.image.load('image/blocks/Door2.png').convert_alpha()
# door3_image = pygame.image.load('image/blocks/Door3.png').convert_alpha()
# door4_image = pygame.image.load('image/blocks/Door4.png').convert_alpha()
goal_1_image = pygame.image.load('image/goals/goal_1.png').convert_alpha()
goal_2_image = pygame.image.load('image/goals/goal_2.png').convert_alpha()
goal_3_image = pygame.image.load('image/goals/goal_3.png').convert_alpha()
key_image = load_image('image/keys', True, 2)
topor_image = pygame.image.load('image/topor/1.png').convert_alpha()
floor_image = pygame.image.load('image/blocks/Floor_l_d.png').convert_alpha()
door1_image = pygame.image.load('image/blocks/Door1_1.png').convert_alpha()
door2_image = pygame.image.load('image/blocks/Door2_2.png').convert_alpha()
button_play_image = load_image('image/button/play', True, 6)
button_exit_image = load_image('image/button/exit',True, 6)
fog_image = pygame.image.load('image/decorate/fog.png').convert_alpha()
slime_big1_image = load_image('image/enemy/big', True, 5)
slime_fon_image = load_image('image/enemy/left', True, 5)
player_fon_image = load_image('image/player_2/left')