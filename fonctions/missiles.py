import pygame as pg, sys                    # pg = bibliothèque utilisée pour créer des jeux vidéo, sys = module qui permet d'interagir avec Python (sys.exit())
from classes.classMissile import Missile 


################ instanciation des missiles ###########################
def missileGroup(x, y, POWER, SIZE, wich):
    """
    Crée un groupe contenant un missile.
    x, y : position de départ
    POWER : puissance du missile
    SIZE : taille de référence pour l'image
    wich : "vaisseau" ou "enemy"
    """
    group = pg.sprite.Group()
    
    # chargement de l'image 
    if wich == "vaisseau":
        missile_img = pg.image.load("graph/munition50.png").convert_alpha()      # chargement d'une image, en gardant la transparence
    elif wich == "enemy":
        missile_img = pg.image.load("graph/munition04.png").convert_alpha()      # chargement d'une image, en gardant la transparence
    else:
        raise ValueError("Type de missile inconnu : doit être 'vaisseau' ou 'enemy'")
    # redimensionnement de l'image en entier
    missile_img = pg.transform.scale(missile_img, (int(SIZE / 10), int(SIZE / 10)))         # taille de l'image imposée

    # instancier le missile
    missile = Missile(x, y, missile_img, POWER)
    group.add(missile)

    # Optionnel : créer un événement pour tirer automatiquement
    MISSILE_EVENT = pg.USEREVENT + 1
    pg.time.set_timer(MISSILE_EVENT, 1000)
    
    return group
