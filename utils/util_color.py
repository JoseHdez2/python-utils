import util_num as UN
import random

def random_color():
    return (random.randint(0,255),
            random.randint(0,255),
            random.randint(0,255))

def clamp_color(color):
  return (UN.clamp(color[0],0,255), UN.clamp(color[1],0,255), UN.clamp(color[2],0,255))

def mutate_color(r,g,b,diff):
    c = ((UN.mutate(r,diff), UN.mutate(g,diff), UN.mutate(b,diff)))
    return clamp_color(c)

def clearer(color, n):
  c = ((color[0] + n, color[1] + n, color[2] + n))
  return clamp_color(c)