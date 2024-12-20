
"""
Name    : dame_regle.py
Auteur  : Lucas Santos & alexian Jaccard
Date    : 14.11.24
Version : 3.7
Purpose : Jeu de dames avec la librairie pygame
"""
import dame_gfx as gfx
import pygame


def bouger_pion(pion, pion_ligne, pion_pos, nouvelle_ligne, nouvelle_pos):
    """Déplace le pion du damier, met à jour l'affichage"""
    # Efface l'ancienne position
    couleur_case = gfx.cases_blanches if (pion_pos + pion_ligne) % 2 else gfx.cases_noires
    gfx.dessine_case(pion_pos, pion_ligne, couleur_case)

    # Met à jour la nouvelle position
    pion_ligne = nouvelle_ligne
    pion_pos = nouvelle_pos
    pion_pos_noir = nouvelle_pos
    pion_pos_noir2 = nouvelle_pos
    # Affiche le pion à sa nouvelle position
    screen.blit(pion, (marge_gauche + case_size * pion_pos, marge_haut + case_size * pion_ligne))

    return pion_ligne, pion_pos

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
        gfx.dessine_case(pion_pos, 0)
        pion_pos += 1
    screen.blit(pion, (marge_gauche + case_size * pion_pos, marge_haut))


def bouge_gauche():
    """Déplace le pion vers la gauche"""
    global screen, case_size, marge_gauche, marge_haut, pion_pos, pion, nb_colonnes
    if pion_pos > 0:
        gfx.dessine_case(pion_pos, 0)
        pion_pos -= 1
    screen.blit(pion, (marge_gauche + case_size * pion_pos, marge_haut))

def bouge_haut():
    """Déplace le pion noir vers le haut"""
    global screen, case_size, marge_gauche, marge_haut, pion_pos_noir, pion_noir, nb_colonnes
    if pion_pos_noir > 0:
        gfx.dessine_case(0, pion_pos_noir)
        pion_pos_noir -= 1
    screen.blit(pion_noir, (marge_gauche, marge_haut + case_size * pion_pos_noir))


def bouge_bas():
    """Déplace le pion noir vers le bas"""
    global screen, case_size, marge_gauche, marge_haut, pion_pos_noir, pion_noir, nb_colonnes
    if pion_pos_noir < (nb_colonnes - 1):
        gfx.dessine_case(0, pion_pos_noir)
        pion_pos_noir += 1
    screen.blit(pion_noir, (marge_gauche, marge_haut + case_size * pion_pos_noir))


for i in range(5, 8):
    for j in range(8):
        if (i + j) % 2 == 1:  # Placer les pions sur les cases noires (i + j impair)
            gfx.plateau[i][j] = 'p'  # Pion du joueur 2



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

        #elif btn_presse[pygame.K_q]:
            #running = False

        pygame.display.update()

