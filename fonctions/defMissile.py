import pygame as pg, sys                # sys = module qui permet d'interagir avec Python (sys.exit())

def missile(player, screen, WCOLOR):
    missile = pg.Rect(player.x, player.y, 25, 25)
    pg.draw.rect(screen, WCOLOR, missile)
    print("Missile créé")