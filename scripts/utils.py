import os
import pygame

BASE_IMG_PATH = 'data/assets/sprites/'

def load_image(path):
  img = pygame.image.load(BASE_IMG_PATH + path)
  img.set_colorkey((0, 0, 0))
  return img

def load_dir_images(path):
  images = []
  for img_name in sorted(os.listdir(BASE_IMG_PATH + path)):
    images.append(load_image(path + '/' + img_name))
  return images
    