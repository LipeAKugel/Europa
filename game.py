import sys
import pygame

from scripts.utils import load_dir_images
from scripts.utils import load_image
from scripts.entities import PhysicsEntity
from scripts.tilemap import Tilemap
from scripts.background import Background

class Game:
  def __init__(self):    
    pygame.init()
    pygame.display.set_caption('Europa')
    self.screen = pygame.display.set_mode((640, 480))
    self.display = pygame.Surface((320, 240))

    self.clock = pygame.time.Clock()
    
    self.assets = {
      'empty_background': load_image('backgrounds/star_background/empty_background.png'),
      'grass': load_dir_images('tilesets/grass'),
      'bricks': load_dir_images('tilesets/bricks'),
      'player': load_image('astronaut/idle/0.png')
    }
    
    self.player = PhysicsEntity(self, 'player', (50, 50), (9, 10))
    self.movement = [False, False]
    self.tilemap = Tilemap(self)
    self.background = Background(self, self.assets['empty_background'], 0.5)

    self.scroll = [0, 0]
 
  def run(self):    
    while True:
      self.display.fill((0, 0, 0))
      
      # camera scroll
      self.scroll[0] += (self.player.rect().centerx - self.display.get_width() / 2 - self.scroll[0]) / 30
      self.scroll[1] += (self.player.rect().centery - self.display.get_height() / 2 - self.scroll[1]) / 30
      render_scroll = (int(self.scroll[0]), int(self.scroll[1]))
      
      # render game objects
      self.background.render(self.display, offset=render_scroll)
      self.player.update(self.tilemap, (self.movement[1] - self.movement[0], 0))
      self.player.render(self.display, offset=render_scroll)
      self.tilemap.render(self.display, offset=render_scroll)
            
      # player movement
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()
          sys.exit()
        
        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_LEFT:
            self.movement[0] = True
          if event.key == pygame.K_RIGHT:
            self.movement[1] = True
          if event.key == pygame.K_UP:
            self.player.velocity[1] = -3

        if event.type == pygame.KEYUP:
          if event.key == pygame.K_LEFT:
            self.movement[0] = False
          if event.key == pygame.K_RIGHT:
            self.movement[1] = False

      # blit onto screen.
      self.screen.blit(pygame.transform.scale(self.display, self.screen.get_size()), (0, 0))
      pygame.display.update()
      self.clock.tick(60)
      
Game().run()