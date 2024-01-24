import pygame

class Background:
  def __init__(self, game, img, parallax):
    self.game = game
    self.img = img
    self.pos = [-self.img.get_width()/2 + self.game.display.get_width()/2,
                -self.img.get_height()/2 + self.game.display.get_height()/2]
    self.parallax = parallax
    
  def update_pos(self, surf, offset):
    # controls the background position
    render_offset = (offset[0] * self.parallax, offset[1] * self.parallax)
    render_pos = list(map(lambda axis, offset: axis - offset, self.pos, render_offset))
    
    # x axis limiting.
    if render_offset[0] <= self.pos[0]:
      render_pos[0] = 0
    if render_offset[0] >= self.img.get_width()/2 - surf.get_width()/2:
      render_pos[0] = -self.img.get_width() + surf.get_width()

    # y axis limiting.
    if render_offset[1] <= self.pos[1]:
      render_pos[1] = 0
    if render_offset[1] >= self.img.get_height()/2 - surf.get_height()/2:
      render_pos[1] = -self.img.get_height() + surf.get_height()
  
    return render_pos
    
  def render(self, surf, offset=(0, 0)):
    render_pos = self.update_pos(surf, offset)
    surf.blit(self.img, tuple(render_pos))