import pygame as pg, sys                # sys = module qui permet d'interagir avec Python (sys.exit())
import time

def missilesPlayer(screen, missiles):
    # Mise à jour des missiles
    for m in missiles[:]:
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

def pv_vaisseau(pv_joueur, screen, fheart, eheart, gameover_img):
    if pv_joueur == 3:
        screen.blit(fheart, (10,10))
        screen.blit(fheart, (60,10))
        screen.blit(fheart, (110,10))
    elif pv_joueur == 2:
        screen.blit(fheart, (10,10))
        screen.blit(fheart, (60,10))
        screen.blit(eheart, (110,10))
    elif pv_joueur == 1:
        screen.blit(fheart, (10,10))
        screen.blit(eheart, (40,10))
        screen.blit(eheart, (70,10))
    elif pv_joueur <= 0:
        screen.blit(eheart, (10,10))
        screen.blit(eheart, (40,10))
        screen.blit(eheart, (70,10))
        screen.blit(gameover_img, (0,0))
        pg.display.flip()