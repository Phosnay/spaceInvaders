# Jeu de shooter : space invaders

jeu pour un joueur.

## page d'accueil : 
nom du jeu et menu pour :  
	- choisir le niveau de difficulté  
	- changer les paramètres de son, musique, couleurs  
	- voir le tableau des scores  
	- connaitre les crédits  
	- lancer le jeu,  
	- pour quitter le jeu  

## Niveau 1 du jeu (difficulté moyenne)  
affichage d'une barre d'informations en haut de l'écran   
		- du score,   
		- du niveau,   
		- des points de vie,   
		- des armes choisies (selon l'avancé du jeu),   
		- … (selon l'avancé du jeu)  

affichage des ennemis (E) sous la barre d'informations   
		- 1 ligne de : 10 E de puissance 3 points de vie (E fort) soit 10 E  
		  2 lignes de : 10 E de puissance 2 points de vie (E moyen) sur chaque ligne 	soit 20 E  
		  3 lignes de : 10 E de puissance 1 point de vie (E faible) sur chaque ligne 	soit 30 E  
		- les E sont rangés en lignes et en colonne, à égale distance les uns des autres  
		- aléatoirement, des E donnent des cadeaux (1 point de vie, remonter d'une ligne, ...) quand ils meurent.  

point de vie :  
sont concernés  
1 à 2 E forts  
2 à 4 E moyens  
3 à 6 E faible

remonter :  
est concerné   
1 E quelconque, à partir d'une descente d'un cran,  
... (pourront donner des pièges ou des munitions aux niveaux suivants)  
		- rien n'indique qu'un E peut donner un cadeau.  

affichage du vaisseau au milieu sur la ligne du bas  
affichage de 3 boucliers centrés entre le bas des E et le vaisseau, répartis équitablement sur la ligne  
déplacement des E  
		- tous en même temps, dans la même direction, comme un seul bloc  
		- vers la droite d'un cran, puis un arrêt d'une seconde, ceci en boucle jusqu'à ce qu'un E touche le bord de l'écran  
		- descend d'un cran quand le bord de l'écran est touché et changement de direction (droite ou gauche)  
		- vers la gauche d'un cran, puis un arrêt d'une seconde, ceci en boucle jusqu'à ce qu'un E touche le bord de l'écran  
		- le temps d'arrêt d'une seconde sera plus ou moins court et/ou pourra diminuer au cours du temps selon le niveau de difficulté (selon l'avancé du jeu) quand une ligne d'E est détruite ou quand un certain nombre d'E (une dizaine) est détruit  
		- game over si un E touche le vaisseau ou le bas de l'écran  
		- l'E détruit le pixel du bouclier qu'il touche   


déplacement du vaisseau  
		- se déplace vers la droite ou vers la gauche selon les flèches cliquées par le joueur  
		- (selon l'avancé du jeu) pourra se déplacer vers le haut   

tir des E  
		- dans une colonne d'E, seul celui du bas tir vers le bas  
		- le tir provoque un point de vie en moins au vaissau  
		- le tir provoque la destruction d'un pixel du bouclier  

tir du vaisseau  
		- le vaisseau tir vers le haut, 1 tir tous les x secondes  
		- le tir provoque un point de vie en moins à l'E touché  
		- le tir provoque la destruction d'un pixel du bouclier	  

affichage d'un message  
		- quand tous les E sont morts  
		- quand le vaisseau est détruit  
		- quand le vaisseau perd un point de vie (il clignote par exemple)  

transformation   
		- des E quand il perdent des points de vie : le fort devient un moyen, le moyen devient un faible  
		- des E en étoile (ou autre) pendant un très court instant quand ils meurent  
		- du vaisseau en boule de feu quand il meurt  