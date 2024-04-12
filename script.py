import os
import pygame


def load_image(directory, zoom=False, size=1):
    image_list = []
    files = os.listdir(directory)
    for i in files:
        image = pygame.image.load(f'{directory}/{i}').convert_alpha()
        if zoom:
            image = pygame.transform.rotozoom(image,0,size)
        image_list.append(image)
    return image_list