import pygame as pg, sys                # pg = bibliothèque utilisée pour créer des jeux vidéo, sys = module qui permet d'interagir avec Python (sys.exit())
from classes.classEnemy import Enemy            # ou import classBlock 

SPACE_X, SPACE_Y = 10, 3        # espacement entre les rangés, les lignes
START_Y = 100                   # distance entre le haut de l'écran et la position des ennemis au début du jeu 
DOWN = 10                       # distance de chaque déplacement des ennemis vers le bas

################ instanciation des ennemis ###########################
def fillEnemyGroup(rows, cols, WIDTH, SIZE):
    """
    Instanciation des ennemis.  
    rows: nombre de pixels entre deux rangées  
    cols: nombre de pixels entre deux colonnes  
    WIDTH: largeur de l'écran  
    SIZE: taille de l'image  
    """
    Start_X = (WIDTH - ((10 * SIZE) + (9 * SPACE_X))) // 2                      # positionnement du premier ennemi pour que la ligne soit centrée
    enemyGroup = pg.sprite.Group()                                              # conteneur gérant plusieurs sprites.
    enemyStrong_img = pg.image.load("graph/space10.1.png").convert_alpha()      # chargement d'une image, en gardant la transparence
    enemyMedium_img = pg.image.load("graph/space12.1.png").convert_alpha()
    enemyWeak_img = pg.image.load("graph/space13.1.png").convert_alpha()
    for row in range(rows):
        for col in range(cols):
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
    if not inScreen:
        for enemy in enemyGroup:
            enemy.speed *= -1           # changement de direction
            enemy.rect.y += DOWN

################ Collision entre deux sprites ###########################
def detectCollision(group1, group2, points, damage):
    """
    Détecte les collisions entre deux groupes de sprites.    
    Supprime l'objet du premier groupe (group1).  
    Retire des point de vie à l'objet du deuxième groupe (group2).  
    
    group1: ennemi ou missile  
    group2: vaisseau ou ennemi  
    point: points de vie  
    damage: points perdus  
    screen: écran
    """
    collisions = pg.sprite.groupcollide(group1, group2, True, False)
    for sprite1, sprite2_hit in collisions.items():
        for sprite in sprite2_hit:
            if sprite.takeDamage(damage):  
                return 1
    return 0 
                

# pygame.sprite.groupcollide(group1, group2, dokill1, dokill2)
# compare tous les sprites des deux groupes.
# group1 : missilesVaisseau
# group2 : enemyGroup
# dokill1 : si True, supprime le sprite de group1 quand il y a collision (le missile)
# dokill2 : si True, supprime le sprite de group2 (l’ennemi)
# retourne un dictionnaire : Chaque clé est un missile ayant touché un ou plusieurs ennemis,
#                            chaque valeur est une liste des ennemis touchés.