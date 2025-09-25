import pygame as pg, sys                # sys = module qui permet d'interagir avec Python (sys.exit())


################ instanciation des ennemis ###########################""
def displayLigne(who, x, y, screen, SIZE, SPACE):
    for i in range(10):
        ennemy = pg.Rect((x + ((SIZE + SPACE) * i)), y, SIZE, SIZE)                            # rectangle (x, y, largeur, hauteur) 
        screen.blit(who, ennemy.topleft) 

def displayEnnemies(screen, WIDTH, SIZE, SPACE):
    firstSpotX = (WIDTH - ((10 * SIZE) + (9 * SPACE))) // 2                     # // : division entière (sans reste)
    firstSpotY = 100


    ennemyStrong_img = pg.image.load("graph/space10.1.png").convert_alpha()     # chargement d'une image, en gardant la transparence
    ennemyStrong_img = pg.transform.scale(ennemyStrong_img, (SIZE, SIZE))
    ennemyMedium_img = pg.image.load("graph/space12.1.png").convert_alpha()
    ennemyMedium_img = pg.transform.scale(ennemyMedium_img, (SIZE, SIZE))
    ennemyWeak_img = pg.image.load("graph/space13.1.png").convert_alpha()
    ennemyWeak_img = pg.transform.scale(ennemyWeak_img, (SIZE, SIZE))
    displayLigne(ennemyStrong_img, firstSpotX, firstSpotY, screen, SIZE, SPACE)
    displayLigne(ennemyMedium_img, firstSpotX, (firstSpotY + (SIZE + SPACE)) , screen, SIZE, SPACE)
    displayLigne(ennemyMedium_img, firstSpotX, (firstSpotY + (SIZE + SPACE) * 2), screen, SIZE, SPACE)
    displayLigne(ennemyWeak_img, firstSpotX, (firstSpotY + (SIZE + SPACE) * 3), screen, SIZE, SPACE)
    displayLigne(ennemyWeak_img, firstSpotX, (firstSpotY + (SIZE + SPACE) * 4), screen, SIZE, SPACE)
    displayLigne(ennemyWeak_img, firstSpotX, (firstSpotY + (SIZE + SPACE) * 5), screen, SIZE, SPACE)


