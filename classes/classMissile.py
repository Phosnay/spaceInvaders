import pygame as pg, sys                # sys = module qui permet d'interagir avec Python (sys.exit())

""" Missile hérite de pygame.sprite.Sprite.  
    Cela permettra d'utiliser toutes les fonctionnalités de pygame.sprite.Group 
    (affichage, collisions, suppression, etc.).
"""

class Missile(pg.sprite.Sprite):
    def __init__(self, x, y, image, powerMissile=1):
    # __init__ est le constructeur, appelé à la création d’un objet Missile.
        super().__init__()                                  # Appeller le constructeur de la classe mère (pg.sprite.Sprite).
        self.image = image.copy()                           # faire une copie de l’image donnée, pour éviter de modifier l’original
        self.rect = self.image.get_rect(topleft=(x, y))     # associer l'image à un rectangle dont le coin supérieur gauche est en x, y
        self.powerMissile = powerMissile
        self.speed = 2
        
    def update(self, dx=0):
        """ Cette méthode est appelée par Group.update(dx, dy, largeur de screen).
            Ici elle applique un déplacement (dx, dy) en pixels.
        """
        self.rect.x += self.speed    