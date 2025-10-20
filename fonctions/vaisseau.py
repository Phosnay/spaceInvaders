import pygame as pg, sys                # sys = module qui permet d'interagir avec Python (sys.exit())
import time

def clamp(WIDTH, HEIGHT, r):
    r.left = max(0, r.left); r.top = max(0, r.top)
    r.right = min(WIDTH, r.right); r.bottom = min(HEIGHT, r.bottom)

# r = player = pg.Rect(WIDTH//2 - SIZE//2, HEIGHT//1.1 - SIZE//2, SIZE, SIZE) 
# dx = vaut +1 vers la droite, -1 vers la gauche, 0 sinon
# dy = vaut +1 vers le bas, -1 vers le haut, 0 sinon

def move_and_collide(r, dx, dy, speed, dt, walls):
    # X
    r.x += int(dx * speed * dt)
    for w in walls:
        if r.colliderect(w):
            if dx > 0:  r.right = w.left
            elif dx < 0: r.left  = w.right
    # Y
    r.y += int(dy * speed * dt)
    for w in walls:
        if r.colliderect(w):
            if dy > 0:  r.bottom = w.top
            elif dy < 0: r.top   = w.bottom

def missilesPlayer(screen, missiles):
    # Mise à jour des missiles
    for m in missiles:
        m.y -= 7
        if m.bottom < 0:
            missiles.remove(m)
    
    for m in missiles:
        pg.draw.rect(screen, (0, 255, 0), m)
    pg.display.flip()

def creerMissilesVaisseau():
    Missile = pg.USEREVENT + 1 #crée un événement personnalisé avec un identifiant unique
    pg.time.set_timer(Missile, 1000) #Création d'un missile par seconde
    return Missile