import const_color as CC

def mk_font(pygame):
    return pygame.font.SysFont("DejaVuSans", 64)

def mk_text(somefont, something):
    return somefont.render(something, 1, (255, 255, 255))
    
def make_text(pygame, something):
  return mk_font(pygame).render(something, 1, CC.WHITE)