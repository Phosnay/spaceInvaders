import pygame as pg, sys                # sys = module qui permet d'interagir avec Python (sys.exit())

""" Missile hérite de pygame.sprite.Sprite.  
    Cela permettra d'utiliser toutes les fonctionnalités de pygame.sprite.Group 
    (affichage, collisions, suppression, etc.).
"""

class Missile(pg.sprite.Sprite):
    def __init__(self, x, y, image, direction, powerMissile=1, speed=2):
        """
        Création d'un missile. 
        (x,y: position de départ), 
        (image: visuel), 
        (direction: 1=vers le bas, -1=vers le haut)
        (powerMissile: puissance=1 par défaut),
        (speed: vitesse=2 par défaut) 
        """
    # __init__ est le constructeur, appelé à la création d’un objet Missile.
        super().__init__()                                  # Appeller le constructeur de la classe mère (pg.sprite.Sprite).
        self.image = image.copy()                           # faire une copie de l’image donnée, pour éviter de modifier l’original
        self.rect = self.image.get_rect(topleft=(x, y))     # associer l'image à un rectangle dont le coin supérieur gauche est en x, y
        self.powerMissile = powerMissile
        self.speed = speed * direction
        
    def update(self):
        """ 
        Applique un déplacement vertical.
        """
        self.rect.y += self.speed