import pygame as pg, sys                # sys = module qui permet d'interagir avec Python (sys.exit())

""" 
    player hérite de pygame.sprite.Sprite.  
    Cela permettra d'utiliser toutes les fonctionnalités de pygame.sprite.Group 
    (affichage, collisions, suppression, etc.).
"""

class Player(pg.sprite.Sprite):
    def __init__(self, x, y, image, powerPlayer, speed=2):
        """
        Création du vaisseau. 
        (x,y: position de départ), 
        (image: visuel), 
        (powerPlayer: points de vie), 
        (speed: vitesse=2 par défaut)
        """
    # __init__ est le constructeur, appelé à la création d’un objet Enemy.
        super().__init__()                                  # Appeller le constructeur de la classe mère (pg.sprite.Sprite).
        self.image = image.copy()                           # faire une copie de l’image donnée, pour éviter de modifier l’original
        self.rect = self.image.get_rect(topleft=(x, y))     # associer l'image à un rectangle dont le coin supérieur gauche est en x, y
        self.powerPlayer = powerPlayer
        self.speed = speed

    def update(self, screen):
        """ 
        Applique un déplacement selon les touches enfoncées (flèches ou d,q,z,s)
        """
        k = pg.key.get_pressed()                                            # retourne l'état actuel de toutes les touches du clavier
        dx = (k[pg.K_RIGHT] or k[pg.K_d]) - (k[pg.K_LEFT] or k[pg.K_q])     # k[pg.K_RIGHT] == 1 si la touche flèche droite est enfoncée sinon vaut 0
        dy = (k[pg.K_DOWN]  or k[pg.K_s]) - (k[pg.K_UP]   or k[pg.K_z])     # dy vaut +1 vers le bas, -1 vers le haut, 0 sinon

        self.rect.x += self.speed * dx                         # selon la vitesse (speed) définie automatiquement dans def __init__
        self.rect.y += self.speed * dy                         # selon la vitesse (speed) définie automatiquement dans def __init__

        # empêche le vaisseau de sortir de l'écran
        # self.rect.x = max(0, min(self.rect.x, WIDTH - self.rect.width))
        # self.rect.y = max(0, min(self.rect.y, HEIGHT - self.rect.height))
        screen_rect = screen.get_rect()     # récupère le rectangle de la fenêtre (x=0, y=0, width, height).
        self.rect.clamp_ip(screen_rect)     # recadre le vaisseau à l’intérieur de cette zone.