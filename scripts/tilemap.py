import pygame

class Tilemap:
  def __init__(self, game, tile_size=8):
    self.game = game
    self.tile_size = tile_size
    self.tilemap = {}
    self.offgrid_tiles = []
    
    for i in range(25):
      self.tilemap[f'{i};10'] = {'type':'grass', 'variant': 7, 'pos': (i, 10)}
  
  def render(self, surf):
    for tile in self.offgrid_tiles:
      surf.blit(self.game.assets[tile['type']][tile['variant']], (tile['pos'][0], tile['pos'][1]))
    
    for loc in self.tilemap:
      tile = self.tilemap[loc]
      surf.blit(self.game.assets[tile['type']][tile['variant']], (tile['pos'][0] * self.tile_size, tile['pos'][1] * self.tile_size))
      
