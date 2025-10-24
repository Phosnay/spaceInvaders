import pygame as pg, sys                # sys = module qui permet d'interagir avec Python (sys.exit())

""" Enemy hérite de pygame.sprite.Sprite.  
    Cela permettra d'utiliser toutes les fonctionnalités de pygame.sprite.Group 
    (affichage, collisions, suppression, etc.).
"""

class Enemy(pg.sprite.Sprite):
    def __init__(self, x, y, image, powerEnemy, speed=2):
        """
        Création d'un ennemi. 
        (x,y: position de départ), 
        (image: visuel), 
        (powerEnemy: points de vie), 
        (speed: vitesse=2 par défaut)
        """
    # __init__ est le constructeur, appelé à la création d’un objet Enemy.
        super().__init__()                                  # Appeller le constructeur de la classe mère (pg.sprite.Sprite).
        self.image = image.copy()                           # faire une copie de l’image donnée, pour éviter de modifier l’original
        self.rect = self.image.get_rect(topleft=(x, y))     # associer l'image à un rectangle dont le coin supérieur gauche est en x, y
        self.powerEnemy = powerEnemy
        self.speed = speed

    def update(self):
        """ 
        Applique un déplacement horizontal.
        """
        self.rect.x += self.speed                           # selon la vitesse (speed) définie automatiquement dans def __init__

    def takeDamage(self, life):
            """Réduit les points de vie et tue l'ennemi s'ils tombent à 0."""
            self.powerEnemy -= life
            if self.powerEnemy <= 0:
                self.kill()