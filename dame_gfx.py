"""
Name    : dame_gfx.py
Auteur  : Lucas Santos & alexian Jaccard
Date    : 14.11.24
Version : 3.7
Purpose : Jeu de dames avec la librairie pygame
"""

import pygame

def dessine_case(col, row, couleur):
    """Dessine une case du damier à la position (col, row) avec la couleur spécifiée"""
    pygame.draw.rect(screen, couleur,
                     (marge_gauche + col * case_size,
                      marge_haut + row * case_size,
                      case_size,
                      case_size), 0)

def dessine_toutes_les_case():
    """Redessine toutes les cases du plateau"""
    for row in range(nb_lignes):
        for col in range(nb_colonnes):
            couleur = cases_blanches if (col + row) % 2 else cases_noires
            dessine_case(col, row, couleur)

def afficher_plateau(plateau):
    """Affiche le plateau dans la console"""
    for ligne in plateau:
        print(" ".join(str(case) for case in ligne))

plateau = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1]


case_size = 80
cases_blanches = (240, 230, 140)
cases_noires = (160, 82, 45)

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
window_color = (255, 255, 255)

# Création de la fenêtre
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Jeu de dames")
screen.fill(window_color)

# Icone de la fenêtre
path_to_images = "pictures\\pictures\\"
icon = pygame.image.load(path_to_images + "International_draughts.png")
pygame.display.set_icon(icon)

# Dessin du damier
dessine_toutes_les_case()

# Affichage du pion initial
pion_pos = 0  # Position initiale du pion blanc
pion_ligne = 0
pion = pygame.image.load(path_to_images + "MA-24_pion.png")
pion = pygame.transform.scale(pion, (case_size, case_size))
screen.blit(pion, (marge_gauche, marge_haut))

for compteur in range(5):
    pion_pos_noir= 1+(compteur+1 * compteur)
    pion_pos_noir2= (compteur+1 * compteur)
    pion_ligne_noir = 6  # Commence en bas (ligne 9)
    pion_ligne_noir2 = 7  # Commence en bas (ligne 9)
    pion_ligne_noir3 = 8  # Commence en bas (ligne 9)
    pion_ligne_noir4 = 9 # Commence en bas (ligne 9)
    pion_noir = pygame.image.load(path_to_images + "MA-24_pion_noir.png")
    pion_noir = pygame.transform.scale(pion_noir, (case_size, case_size))
    screen.blit(pion_noir, (marge_gauche + case_size * pion_pos_noir2, marge_haut + case_size * pion_ligne_noir))
    screen.blit(pion_noir, (marge_gauche + case_size * pion_pos_noir, marge_haut + case_size * pion_ligne_noir2))
    screen.blit(pion_noir, (marge_gauche + case_size * pion_pos_noir2, marge_haut + case_size * pion_ligne_noir3))
    screen.blit(pion_noir, (marge_gauche + case_size * pion_pos_noir, marge_haut + case_size * pion_ligne_noir4))

for compteur in range(5):
    pion_pos_blanc= 1+(compteur+1 * compteur)
    pion_pos_blanc2= (compteur+1 * compteur)
    pion_ligne_blanc = 0 # Commence en bas (ligne 9)
    pion_ligne_blanc2 = 1  # Commence en bas (ligne 9)
    pion_ligne_blanc3 = 2  # Commence en bas (ligne 9)
    pion_ligne_blanc4 = 3 # Commence en bas (ligne 9)
    pion_noir = pygame.image.load(path_to_images + "MA-24_pion.png")
    pion_noir = pygame.transform.scale(pion_noir, (case_size, case_size))
    screen.blit(pion_noir, (marge_gauche + case_size * pion_pos_blanc2, marge_haut + case_size * pion_ligne_blanc))
    screen.blit(pion_noir, (marge_gauche + case_size * pion_pos_blanc, marge_haut + case_size * pion_ligne_blanc2))
    screen.blit(pion_noir, (marge_gauche + case_size * pion_pos_blanc2, marge_haut + case_size * pion_ligne_blanc3))
    screen.blit(pion_noir, (marge_gauche + case_size * pion_pos_blanc, marge_haut + case_size * pion_ligne_blanc4))


# Affichage du pion noir
#pion_pos_noir = 1 # Position initiale du pion noir
#pion_pos_noir2 = 3
#pion_ligne_noir = 9  # Commence en bas (ligne 9)
#pion_noir = pygame.image.load(path_to_images + "MA-24_pion_noir.png")
#pion_noir = pygame.transform.scale(pion_noir, (case_size, case_size))
#screen.blit(pion_noir, (marge_gauche + case_size * pion_pos_noir, marge_haut + case_size * pion_ligne_noir))


pygame.display.flip()

# Boucle principale
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        btn_presse = pygame.key.get_pressed()

pygame.quit()
