"""
Name    : MA-24_Python_jeudames.py
Auteur  : Lucas Santos & alexian Jaccard
Date    : 14.11.24
Version : 3.7
Purpose : Jeu de dames avec la librairie pygame
"""
from idlelib.colorizer import color_config

import pygame
from pygame.examples.cursors import color_cursor


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


def deplacer_pion(plateau, x1, y1, x2, y2):
    """
    Déplace un pion du plateau de (x1, y1) à (x2, y2).
    Vérifie si la destination est vide (0).
    """
    if plateau[x2][y2] == 0:  # Si la case de destination est vide
        plateau[x2][y2] = plateau[x1][y1]  # Déplace le pion
        plateau[x1][y1] = 0  # Vide la case de départ
        return True
    else:
        print("La case de destination est occupée!")
        return False


def bouge_droite():
    """Déplace le pion vers la droite"""
    global screen, case_size, marge_gauche, marge_haut, pion_pos, pion, nb_colonnes
    if pion_pos < (nb_colonnes - 1):
        dessine_case(pion_pos, 0)
        pion_pos += 1
    screen.blit(pion, (marge_gauche + case_size * pion_pos, marge_haut))


def bouge_gauche():
    """Déplace le pion vers la gauche"""
    global screen, case_size, marge_gauche, marge_haut, pion_pos, pion, nb_colonnes
    if pion_pos > 0:
        dessine_case(pion_pos, 0)
        pion_pos -= 1
    screen.blit(pion, (marge_gauche + case_size * pion_pos, marge_haut))

def bouge_haut():
    """Déplace le pion noir vers le haut"""
    global screen, case_size, marge_gauche, marge_haut, pion_pos_noir, pion_noir, nb_colonnes
    if pion_pos_noir > 0:
        dessine_case(0, pion_pos_noir)
        pion_pos_noir -= 1
    screen.blit(pion_noir, (marge_gauche, marge_haut + case_size * pion_pos_noir))


def bouge_bas():
    """Déplace le pion noir vers le bas"""
    global screen, case_size, marge_gauche, marge_haut, pion_pos_noir, pion_noir, nb_colonnes
    if pion_pos_noir < (nb_colonnes - 1):
        dessine_case(0, pion_pos_noir)
        pion_pos_noir += 1
    screen.blit(pion_noir, (marge_gauche, marge_haut + case_size * pion_pos_noir))



# ------------ MAIN -------------

# Paramètres du plateau
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

        # Déplacer le pion blanc vers le bas à droite (1 case)
        #if btn_presse[pygame.K_d]:
            #if pion_pos < (nb_colonnes - 1) and pion_ligne < (nb_lignes - 1):
                #pion_ligne, pion_pos = bouger_pion(pion, pion_ligne, pion_pos, pion_ligne + 1, pion_pos + 1)

        # Déplacer le pion blanc vers le bas à gauche (1 case)
        #elif btn_presse[pygame.K_a]:
            #if pion_pos > 0 and pion_ligne < (nb_lignes - 1):
                #pion_ligne, pion_pos = bouger_pion(pion, pion_ligne, pion_pos, pion_ligne + 1, pion_pos - 1)

        # Déplacer le pion noir vers le haut à gauche (1 case)
        #elif btn_presse[pygame.K_w]:
            #if pion_pos_noir > 0 and pion_ligne_noir > 0:
                #pion_ligne_noir, pion_pos_noir = bouger_pion(pion_noir, pion_ligne_noir, pion_pos_noir, pion_ligne_noir - 1, pion_pos_noir - 1)

        # Déplacer le pion noir vers le haut à droite (1 case)
        #elif btn_presse[pygame.K_s]:
           #if pion_pos_noir < (nb_colonnes - 1) and pion_ligne_noir > 0:
                #pion_ligne_noir, pion_pos_noir = bouger_pion(pion_noir, pion_ligne_noir, pion_pos_noir, pion_ligne_noir - 1, pion_pos_noir + 1)

        pygame.display.update()
pygame.quit()