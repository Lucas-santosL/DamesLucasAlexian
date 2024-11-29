"""
Name    : MA-24_Python_jeudames.py
Auteur  : Lucas Santos & alexian Jaccard
Date    : 14.11.24
Version : 3.7
Purpose : Jeu de dames avec la librairie pygame
"""

import pygame


def dessine_case(case_pos):
    """Dessine la xème case du damier
    """
    global screen, case_size, cases_blanches, cases_noires, marge_gauche, marge_haut
    if case_pos % 2:
        pygame.draw.rect(screen, cases_blanches,
                         (marge_gauche + case_pos * case_size,
                          marge_haut,
                          case_size,
                          case_size),
                         0)
    else:
        pygame.draw.rect(screen, cases_noires,
                         (marge_gauche + case_pos * case_size,
                          marge_haut,
                          case_size,
                          case_size),
                         0)


# ------------
# --- MAIN ---
# ------------

plateau = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1]

# Version pygame
case_size = 80
cases_blanches = (255, 255, 255)
cases_noires = (1, 1, 1)
pions_blancs = (255, 255, 255)
pions_noirs = (255, 255, 255 )

# Marges autour du damier
marge_gauche = 10
marge_droite = 10
marge_haut = 10
marge_bas = 10

pion_pos = 0

path_to_images = "pictures\\pictures\\"
pygame.init()

# Window size x, y
nb_colonnes = len(plateau)
window_size = (case_size * nb_colonnes
               + marge_gauche
               + marge_droite,
               case_size*nb_colonnes
               + marge_haut
               + marge_bas
               )
window_color = (250, 202, 255)
screen = pygame.display.set_mode(window_size)
icon = pygame.image.load(path_to_images + "International_draughts.png")
pygame.display.set_icon(icon)
pygame.display.set_caption("MA-24_pion.png")
screen.fill(window_color)

# Affiche le damier
for case in range(nb_colonnes):
    dessine_case(case)


# Charge l'image du pion
pion = pygame.image.load(path_to_images + "MA-24_pion.png")
pion = pygame.transform.scale(pion, (case_size, case_size))
screen.blit(pion, (marge_gauche, marge_haut))
pygame.display.flip()


def afficher_plateau(plateau):
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
    global screen, case_size, marge_gauche, marge_haut, pion_pos, pion, nb_colonnes
    if pion_pos < (nb_colonnes-1):
       dessine_case(pion_pos)
       pion_pos += 1
    screen.blit(pion, (marge_gauche +case_size*pion_pos, marge_haut))

def bouge_gauche():
    global screen, case_size, marge_gauche, marge_haut, pion_pos, pion, nb_colonnes
    if pion_pos > 0:
       dessine_case(pion_pos)
       pion_pos -= 1
    screen.blit(pion, (marge_gauche +case_size*pion_pos, marge_haut))

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
        elif btn_presse[pygame.K_q]:
            running = False
        pygame.display.update()

pygame.quit()
