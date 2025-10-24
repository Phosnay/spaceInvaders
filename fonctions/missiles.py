import pygame as pg, sys                    # pg = bibliothèque utilisée pour créer des jeux vidéo, sys = module qui permet d'interagir avec Python (sys.exit())
from classes.classMissile import Missile 


################ instanciation des missiles ###########################
def creationMissile(x, y, POWER, SIZE, wich):
    """
    Crée un missile.
    (x, y : position de départ), 
    (POWER : puissance du missile), 
    (SIZE : taille de référence pour l'image), 
    (wich : "vaisseau" ou "enemy")
    """
    # chargement de l'image 
    if wich == "vaisseau":
        missile_img = pg.image.load("graph/munition20.png").convert_alpha()      # chargement d'une image, en gardant la transparence
        direction = -1
    elif wich == "enemy":
        missile_img = pg.image.load("graph/munition04.png").convert_alpha()      # chargement d'une image, en gardant la transparence
        direction = 1
    else:
        raise ValueError("Type de missile inconnu : doit être 'vaisseau' ou 'enemy'")
    # redimensionnement de l'image en entier
    missile_img = pg.transform.scale(missile_img, (int(SIZE/4), int(SIZE/4)))         # taille de l'image imposée
    # instancier le missile
    missile = Missile(x, y, missile_img, direction, POWER)
    
    return missile

################ destruction des missiles ##########################
def missileKill(missilesGroup, HEIGHT, size):
    """
    destruction des missiles en dehors de l'écran
    (ennemyGroup: collection des missiles), 
    (HEIGHT: hauteur de l'écran), 
    (SIZE: taille de l'image)"""
    for missile in missilesGroup:
        if missile.rect.y + size >= HEIGHT or missile.rect.y < 0:       # si le missile touche le bord
            missile.kill()                                              # suppression du missile de la collection

