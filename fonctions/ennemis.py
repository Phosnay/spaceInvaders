import pygame as pg, sys                # pg = bibliothèque utilisée pour créer des jeux vidéo, sys = module qui permet d'interagir avec Python (sys.exit())
from classes.classEnemy import Enemy            # ou import classBlock 

SPACE_X, SPACE_Y = 10, 3        # espacement entre les rangés, les lignes
START_Y = 100                   # distance entre le haut de l'écran et la position des ennemis au début du jeu 
DOWN = 10                       # distance de chaque déplacement des ennemis vers le bas

################ instanciation des ennemis ###########################
def fillEnemyGroup(ROWS, COLS, WIDTH, SIZE):
    Start_X = (WIDTH - ((10 * SIZE) + (9 * SPACE_X))) // 2                      # positionnement du premier ennemi pour que la ligne soit centrée
    enemyGroup = pg.sprite.Group()                                              # conteneur gérant plusieurs sprites.
    enemyStrong_img = pg.image.load("graph/space10.1.png").convert_alpha()      # chargement d'une image, en gardant la transparence
    enemyStrong_img = pg.transform.scale(enemyStrong_img, (SIZE, SIZE))         # taille de l'image imposée
    enemyMedium_img = pg.image.load("graph/space12.1.png").convert_alpha()
    enemyMedium_img = pg.transform.scale(enemyMedium_img, (SIZE, SIZE))
    enemyWeak_img = pg.image.load("graph/space13.1.png").convert_alpha()
    enemyWeak_img = pg.transform.scale(enemyWeak_img, (SIZE, SIZE))
    for row in range(ROWS):
        for col in range(COLS):
            x = Start_X + col * (SIZE + SPACE_X)
            y = START_Y + row * (SIZE + SPACE_Y)
            # selon la rangée, changer l'image des ennemis
            if row < 1:
                image = enemyStrong_img
                powerEnemy = 3
            elif row < 3:
                image = enemyMedium_img
                powerEnemy = 2
            else:
                image = enemyWeak_img
                powerEnemy = 1
            e = Enemy(x, y, image, powerEnemy)
            enemyGroup.add(e)
    return enemyGroup

################ changement de direction des ennemis ##########################
def directionOfEnemies(enemyGroup, WIDTH, SIZE):
    """
    Dès qu'un ennemi touche les bords, tous les ennemis partent en sens inverse.
    (ennemyGroup: collection des ennemis), 
    (WIDTH: largeur de l'écran), 
    (SIZE: taille de l'image)"""
    inScreen = True
    for enemy in enemyGroup:
        if enemy.rect.x + SIZE >= WIDTH or enemy.rect.x < 0:        # si un seul vaisseau touche le bord
            inScreen = False
    if inScreen == False:
        for enemy in enemyGroup:
            enemy.speed *= -1           # changement de direction
            enemy.rect.y += DOWN

################ Collision entre un missile et un ennemi ###########################
def detectCollision(missiles, sprites):
    """
    Détecte les collisions entre les missiles et les ennemis.
    Supprime le missile et l'ennemi touchés.
    """
    pg.sprite.groupcollide(missiles, sprites, True, True)
    

# pygame.sprite.groupcollide(group1, group2, dokill1, dokill2)
# compare tous les sprites des deux groupes.
# group1 : missilesVaisseau
# group2 : enemyGroup
# dokill1 : si True, supprime le sprite de group1 quand il y a collision (le missile)
# dokill2 : si True, supprime le sprite de group2 (l’ennemi)
# retourne un dictionnaire : Chaque clé est un missile ayant touché un ou plusieurs ennemis,
#                            chaque valeur est une liste des ennemis touchés.