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
        self.power = powerPlayer
        self.speed = speed

    def update(self, screen):
        """ 
        Applique un déplacement selon les touches enfoncées (flèches ou d,q,z,s)
        Oblige le vaisseau à rester dans l'écran (screen)
        """
        k = pg.key.get_pressed()                                            # retourne l'état actuel de toutes les touches du clavier
        dx = (k[pg.K_RIGHT] or k[pg.K_d]) - (k[pg.K_LEFT] or k[pg.K_q])     # k[pg.K_RIGHT] == 1 si la touche flèche droite est enfoncée sinon vaut 0
        dy = (k[pg.K_DOWN]  or k[pg.K_s]) - (k[pg.K_UP]   or k[pg.K_z])     # dy vaut +1 vers le bas, -1 vers le haut, 0 sinon

        self.rect.x += self.speed * dx   # selon la vitesse (speed) définie automatiquement dans def __init__
        self.rect.y += self.speed * dy   # selon la vitesse (speed) définie automatiquement dans def __init__

        # empêche le vaisseau de sortir de l'écran ancienne version avec WIDTH et HEIGHT en variables
        # self.rect.x = max(0, min(self.rect.x, WIDTH - self.rect.width))
        # self.rect.y = max(0, min(self.rect.y, HEIGHT - self.rect.height))

        # empêche le vaisseau de sortir de l'écran avec clamp
        screen_rect = screen.get_rect()     # récupère le rectangle de la fenêtre (x=0, y=0, width, height).
        self.rect.clamp_ip(screen_rect)     # recadre le vaisseau à l’intérieur de cette zone.

    def takeDamage(self, life, screen):
        """
        Réduit les points de vie et arrêt du jeu si le vaisseau tombe à 0.  
        Affichage des points de vie (coeurs).  
        life: point de vie  
        screen: écran  
        """
        fheart = pg.image.load("graph/fullheart.png").convert_alpha()
        fheart = pg.transform.scale(fheart, (50, 50))
        eheart = pg.image.load("graph/emptyheart.png").convert_alpha()
        eheart = pg.transform.scale(eheart, (50, 50))
        self.power -= life

        if self.power == 3:
            screen.blit(fheart, (10,10))
            screen.blit(fheart, (60,10))
            screen.blit(fheart, (110,10))
        elif self.power == 2:
            screen.blit(fheart, (10,10))
            screen.blit(fheart, (60,10))
            screen.blit(eheart, (110,10))
        elif self.power == 1:
            screen.blit(fheart, (10,10))
            screen.blit(eheart, (40,10))
            screen.blit(eheart, (70,10))
        elif self.power <= 0:
            screen.blit(eheart, (10,10))
            screen.blit(eheart, (40,10))
            screen.blit(eheart, (70,10))
            gameover_img = pg.image.load("graph/gameover_img.png").convert_alpha()
            gameover_img = pg.transform.scale(gameover_img, screen.get_size())
            screen.blit(gameover_img, (0,0))
