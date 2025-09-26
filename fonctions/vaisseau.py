import pygame as pg, sys                # sys = module qui permet d'interagir avec Python (sys.exit())
import time

def missile(player, screen, WCOLOR):
    missile = pg.Rect(player.x + 6.5, player.y, 25, 25)
    pg.draw.rect(screen, WCOLOR, missile)

def clamp(WIDTH, HEIGHT, r):
    r.left = max(0, r.left); r.top = max(0, r.top)
    r.right = min(WIDTH, r.right); r.bottom = min(HEIGHT, r.bottom)

# class MyClass:
#     def __init__(self):
#         self.spawned_time = time.time()

#     def can_destroy(self):
#         return time.time() > self.spawned_time + 6  # replace '6' with the seconds the class will exist for

# my_instance = MyClass()
# while True:
#     if my_instance.can_destroy():