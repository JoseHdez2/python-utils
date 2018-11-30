import random

def clamp(num, smallest, biggest):
    return sorted((num,smallest,biggest))[1]

# random

def mutate(n,m):
    return n + random.randint(-m,m)
