import pygame

BASE_IMG_PATH = 'data/assets/sprites/'

def load_image(path):
  img = pygame.image.load(BASE_IMG_PATH + path)
  img.set_colorkey((0, 0, 0))
  return img
    