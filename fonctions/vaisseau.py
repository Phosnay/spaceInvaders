import pygame as pg, sys                # sys = module qui permet d'interagir avec Python (sys.exit())
from classes.classHeart import Heart

def displayHeart(heartGroup, pv_player, emptyHeart):
    newImage = emptyHeart.copy()
    i = 0
    for heart in heartGroup:
        if i >= pv_player:  
            heart.image = newImage
        i += 1



def fillHeartGroup(number):
    """
    Instanciation des coeurs.  
    number: nombre de coeurs   
    """
    Start_X = 10                   # positionnement du premier ennemi pour que la ligne soit centrée
    heartGroup = pg.sprite.Group()                                              # conteneur gérant plusieurs sprites.
    fullHeart = pg.image.load("graph/fullheart.png").convert_alpha()
    fullHeart = pg.transform.scale(fullHeart, (50, 50))
    for position in range(number):
        x = Start_X + position * 40
        heart = Heart(x, 10, fullHeart)
        heartGroup.add(heart)
    return heartGroup
