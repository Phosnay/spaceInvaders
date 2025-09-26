import pygame as pg, sys                # sys = module qui permet d'interagir avec Python (sys.exit())
import time

def clamp(WIDTH, HEIGHT, r):
    r.left = max(0, r.left); r.top = max(0, r.top)
    r.right = min(WIDTH, r.right); r.bottom = min(HEIGHT, r.bottom)