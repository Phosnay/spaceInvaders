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

################ déplacement des ennemis ##########################
def directionOfMouvement(enemyGroup, WIDTH, SIZE):
    inScreen = True
    for enemy in enemyGroup:
        if enemy.rect.x + SIZE >= WIDTH or enemy.rect.x < 0:        # si un seul vaisseau touche le bord
            inScreen = False
    if inScreen == False:
        for enemy in enemyGroup:
            enemy.speed *= -1           # changement de direction
            enemy.rect.y += DOWN

################ Collision entre un missile et un ennemi ###########################
def detectCollision(missiles, enemies):
    """
    Détecte les collisions entre les missiles et les ennemis.
    Supprime le missile et l'ennemi touchés.
    """
    # missiles étant une liste dont un élement va être supprimé, on en fait une copie ([:]) afin d'éviter des erreurs
    # enemies étant un groupe de sprite dont un élément va être supprimé, on n'a pas besoin de faire une copie
    for m in missiles[:]:
        # Vérifie la collision entre le missile et les ennemis
        collided = pg.sprite.spritecollide(m, enemies, dokill=True)     # dokill=True → supprime automatiquement les ennemis touchés de enemies pendant l’itération.
        if collided:                                                    # Si au moins un ennemi est touché
            missiles.remove(m)                                          # On supprime aussi le missile
