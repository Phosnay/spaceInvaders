import pygame as pg, sys                # sys = module qui permet d'interagir avec Python (sys.exit())

#button class
class Button(pg.sprite.Sprite):
	def __init__(self, x, y, image, scale):
		width = image.get_width()
		height = image.get_height()
		self.image = pg.transform.scale(image, (int(width * scale), int(height * scale)))
		self.rect = self.image.get_rect()
		self.rect.topleft = (x, y)
		self.clicked = False

	def draw(self, surface):
		action = False
		position = pg.mouse.get_pos() #Recuperer la position de la souris

		if self.rect.collidepoint(position): #On verifie si la souris est sur le bouton
			if pg.mouse.get_pressed()[0] == 1 and self.clicked == False: #Verification clic gauche souris
				self.clicked = True
				action = True

		if pg.mouse.get_pressed()[0] == 0: 
			self.clicked = False

		surface.blit(self.image, (self.rect.x, self.rect.y))

		return action