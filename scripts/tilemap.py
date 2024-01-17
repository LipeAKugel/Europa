import pygame

NEIGHBOR_OFFSETS = [(-1, -1), (0, -1), (1, -1), (-1, 0), (0, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]
PHYSICS_TILES = {'grass'}

class Tilemap:
  def __init__(self, game, tile_size=8):
    self.game = game
    self.tile_size = tile_size
    self.tilemap = {}
    self.offgrid_tiles = []
    
    for i in range(25):
      self.tilemap[f'{i};10'] = {'type':'grass', 'variant': 7, 'pos': (i, 10)}

  def tiles_around(self, pos):
    tiles = []
    grid_pos = (int(pos[0] // self.tile_size), int(pos[1] // self.tile_size))
    for offset in NEIGHBOR_OFFSETS:
      neighbor_loc = f'{grid_pos[0] + offset[0]};{grid_pos[1] + offset[1]}'
      if neighbor_loc in self.tilemap:
        tiles.append(self.tilemap[neighbor_loc])
    return tiles

  def physics_rects_around(self, pos):
    rects = []
    for tile in self.tiles_around(pos):
      if(tile['type'] in PHYSICS_TILES):
        rects.append(pygame.Rect(tile['pos'][0] * self.tile_size, tile['pos'][1] * self.tile_size,
                                 self.tile_size, self.tile_size))
    return rects
  
  def render(self, surf):
    for tile in self.offgrid_tiles:
      surf.blit(self.game.assets[tile['type']][tile['variant']], (tile['pos'][0], tile['pos'][1]))
    
    for loc in self.tilemap:
      tile = self.tilemap[loc]
      surf.blit(self.game.assets[tile['type']][tile['variant']], (tile['pos'][0] * self.tile_size, tile['pos'][1] * self.tile_size))
      
