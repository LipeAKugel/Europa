import sys
import pygame

from scripts.utils import load_image
from scripts.entities import PhysicsEntity

class Game:
  def __init__(self):    
    pygame.init()
    pygame.display.set_caption('Europa')
    self.screen = pygame.display.set_mode((640, 480))

    self.clock = pygame.time.Clock()
    
    self.assets = {
      'player': load_image('astronaut/idle/0.png')
    }
    
    self.player = PhysicsEntity(self, 'player', (50, 50), (8, 8))
    self.movement = [False, False]
 
  def run(self):    
    while True:
      self.screen.fill((0, 0, 0))
      
      self.player.update((self.movement[1] - self.movement[0], 0))
      self.player.render(self.screen)
      
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()
          sys.exit()
        
        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_LEFT:
            self.movement[0] = True
          if event.key == pygame.K_RIGHT:
            self.movement[1] = True

        if event.type == pygame.KEYUP:
          if event.key == pygame.K_LEFT:
            self.movement[0] = False
          if event.key == pygame.K_RIGHT:
            self.movement[1] = False

      
      pygame.display.update()
      self.clock.tick(60)
      
Game().run()