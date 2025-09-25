import pygame as pg, sys                # sys = module qui permet d'interagir avec Python (sys.exit())
from classes.classEnemy import Enemy            # ou import classBlock 


################ instanciation des ennemis ###########################""
def fillEnemies(ROWS, COLS, WIDTH, SIZE):
    enemies = pg.sprite.Group()    # conteneur gérant plusieurs sprites.
    SPACE_X, SPACE_Y = 10, 8
    START_X = (WIDTH - ((10 * SIZE) + (9 * SPACE_X))) // 2
    START_Y = 100
    enemyStrong_img = pg.image.load("graph/space10.1.png").convert_alpha()     # chargement d'une image, en gardant la transparence
    enemyStrong_img = pg.transform.scale(enemyStrong_img, (SIZE, SIZE))
    enemyMedium_img = pg.image.load("graph/space12.1.png").convert_alpha()
    enemyMedium_img = pg.transform.scale(enemyMedium_img, (SIZE, SIZE))
    enemyWeak_img = pg.image.load("graph/space13.1.png").convert_alpha()
    enemyWeak_img = pg.transform.scale(enemyWeak_img, (SIZE, SIZE))
    for row in range(ROWS):
        for col in range(COLS):
            x = START_X + col * (SIZE + SPACE_X)
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
            enemies.add(e)
    return enemies

################ déplacement des ennemis ###########################""
# enemy.x = position de enemy sur l'axe des x
# enemy.y = position de enemy sur l'axe des y