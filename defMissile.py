def missile(player):
    missile = pg.Rect(player.x, player.y, 25, 25)
    pg.draw.rect(screen, WCOLOR, missile)
    print("Missile créé")