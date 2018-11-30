import numpy as np
import pygame
import util_pygame_rect as UPR
import const_color as CC
import util_color as UC
import util_pygame as UP
import util_pygame_input as UPI
import util_pygame_text as UPT
from enum_input import EInput as EI

def touched_rect(inp, rect):
  return inp[EI.TOUCHED] == True and rect.collidepoint(inp[EI.TOUCH_POS])

def do_frame(grid, inp, selected, surface):
  for r in grid:
    if touched_rect(inp, r):
      selected.append(r) # selected
    surface.fill(r.color, r)
  for r in selected:
    sel_color = UC.clearer(r.color, 100)
    surface.fill(sel_color, r)
    label = UPT.make_text(pygame, str(r))

def run_game():
  pygame.init()
  surface = pygame.display.set_mode((640, 480)) # Android ignores resolution.
  clock = pygame.time.Clock()
  surfrect = surface.get_rect()

  grid = UPR.make_grid(8,15,128)

  label = UPT.make_text(pygame, "plains")
  
  selected = []
  while True:
    inp = UPI.process_evs(pygame)
    surface.fill(CC.DARK_GREEN, surfrect)
    do_frame(grid, inp, selected, surface)
    clock.tick(60)
    # pygame.draw.circle(surface, CC.RED, (100, 100), 128)
    pygame.time.wait(100)
    surface.blit(label, (0,0))
    pygame.display.flip()
  
run_game()