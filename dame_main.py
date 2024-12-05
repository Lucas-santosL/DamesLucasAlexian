"""
Name    : MA-24_Python_jeudames.py
Auteur  : Lucas Santos & alexian Jaccard
Date    : 14.11.24
Version : 3.7
Purpose : Jeu de dames avec la librairie pygame
"""

import pygame


def dessine_case(col, row):
    """Dessine une case du damier à la position (col, row)"""
    global screen, case_size, cases_blanches, cases_noires, marge_gauche, marge_haut

    # Alterne entre case blanche et noire
    couleur = cases_blanches if (col + row) % 2 else cases_noires

    # Dessine la case
    pygame.draw.rect(screen, couleur,
                     (marge_gauche + col * case_size,
                      marge_haut + row * case_size,
                      case_size,
                      case_size), 0)


def afficher_plateau(plateau):
    """Affiche le plateau dans la console"""
    for ligne in plateau:
        print(" ".join(str(case) for case in ligne))




# ------------ MAIN -------------

# Paramètres du plateau
case_size = 80
cases_blanches = (255, 255, 255)
cases_noires = (0, 0, 0)


# Marges autour du damier
marge_gauche = 10
marge_droite = 10
marge_haut = 10
marge_bas = 10

# Initialisation de Pygame
pygame.init()

# Taille du damier
nb_lignes = 10  # Nombre de lignes
nb_colonnes = 10  # Nombre de colonnes

# Taille de la fenêtre
window_size = (case_size * nb_colonnes + marge_gauche + marge_droite,
               case_size * nb_lignes + marge_haut + marge_bas)
window_color = (250, 202, 255)

# Création de la fenêtre
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Jeu de dames")
screen.fill(window_color)

# Icone de la fenêtre
path_to_images = "pictures\\pictures\\"
icon = pygame.image.load(path_to_images + "International_draughts.png")
pygame.display.set_icon(icon)

# Dessin du damier
for row in range(nb_lignes):
    for col in range(nb_colonnes):
        dessine_case(col, row)

# Affichage du pion initial
pion_pos = 0  # Position initiale du pion
pion = pygame.image.load(path_to_images + "MA-24_pion.png")
pion = pygame.transform.scale(pion, (case_size, case_size))
screen.blit(pion, (marge_gauche, marge_haut))

#afiché le deuxième pion
pion_pos_noir = 0  # Position initiale du pion
pion_noir = pygame.image.load(path_to_images + "MA-24_pion_noir.png")
pion_noir = pygame.transform.scale(pion_noir, (case_size, case_size))
screen.blit(pion_noir, (marge_gauche, marge_haut))
pygame.display.flip()

# Boucle principale
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        btn_presse = pygame.key.get_pressed()
        if btn_presse[pygame.K_RIGHT]:
            bouge_droite()
        elif btn_presse[pygame.K_LEFT]:
            bouge_gauche()
        elif btn_presse[pygame.K_UP]:
            bouge_haut()
        elif btn_presse[pygame.K_DOWN]:
            bouge_bas()
        elif btn_presse[pygame.K_q]:
            running = False

        pygame.display.update()
pygame.quit()