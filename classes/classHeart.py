import pygame as pg, sys                # sys = module qui permet d'interagir avec Python (sys.exit())

""" Heart hérite de pygame.sprite.Sprite.  
    Cela permettra d'utiliser toutes les fonctionnalités de pygame.sprite.Group.  
    (affichage, collisions, suppression, etc.). 
"""

class Heart(pg.sprite.Sprite):
    def __init__(self, x, y, image):
        """
        Création d'un coeur.  
        x,y: position de départ   
        image: visuel  
        """
    # __init__ est le constructeur, appelé à la création d’un objet Enemy.
        super().__init__()                                  # Appeller le constructeur de la classe mère (pg.sprite.Sprite).
        self.image = image.copy()                           # faire une copie de l’image donnée, pour éviter de modifier l’original
        self.rect = self.image.get_rect(topleft=(x, y))     # associer l'image à un rectangle dont le coin supérieur gauche est en x, y


