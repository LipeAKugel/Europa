import pygame

class Background:
  def __init__(self, game, img, parallax):
    self.game = game
    self.img = img
    self.pos = [-self.img.get_width()/6, -self.img.get_height()/2 + self.game.display.get_height()/2]
    self.parallax = parallax
    
  def render(self, surf, offset=(0, 0)):
    
    render_offset = (offset[0] * self.parallax, offset[1] * self.parallax)
    render_pos = list(map(lambda axis, offset: axis - offset, self.pos, render_offset))
    
    print(render_offset)
        
    if render_offset[0] <= self.pos[0]:
      render_pos[0] = 0
    if render_offset[1] <= self.pos[1]:
      render_pos[1] = 0
    if render_offset[0] >= self.img.get_width() + self.pos[0]:
      render_pos[0] = self.img.get_width()
    if render_offset[1] >= self.img.get_height() + self.pos[1]:
      render_pos[1] = self.img.get_height()
    
    
    surf.blit(self.img, tuple(render_pos))