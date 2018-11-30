from enum_input import EInput
from pygame.locals import QUIT

def process_evs(pygame):
  inp = {
    EInput.TOUCHED: False,
    EInput.TOUCH_POS: None
  }
  for ev in pygame.event.get():
    if ev.type == QUIT:
      pygame.quit()
    elif ev.type == pygame.MOUSEBUTTONDOWN:
      inp[EInput.TOUCHED] = True
      inp[EInput.TOUCH_POS] = ev.pos
      pygame.mouse.get_rel()
    elif ev.type == pygame.MOUSEBUTTONUP:
      inp[EInput.TOUCHED] = False
  return inp