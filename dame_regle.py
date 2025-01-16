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
    """
    Déplace un pion donné sur le plateau vers une nouvelle position.

    Arguments:
    pion : Surface pygame représentant le pion à déplacer.
    pion_ligne : Ligne actuelle du pion.
    pion_pos : Position actuelle (colonne) du pion.
    nouvelle_ligne : Ligne cible où le pion sera déplacé.
    nouvelle_pos : Colonne cible où le pion sera déplacé.

    Retourne:
    Tuple (nouvelle_ligne, nouvelle_pos).
    """
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
    Déplace un pion d'une case à une autre sur le plateau.

    Arguments:
    plateau : Liste 2D représentant le damier.
    x1, y1 : Coordonnées de la position de départ du pion sur le plateau.
    x2, y2 : Coordonnées de la position d'arrivée du pion.

    Retourne:
    True si le déplacement a été effectué correctement.
    False si la case de destination est occupée.
    """
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


def transformer_en_dame(pion, ligne, col, plateau):
    """
    Transforme un pion en dame lorsqu'il atteint le bord du damier.

    Arguments:
    pion : Type ou valeur du pion (blanc ou noir).
    ligne : Ligne où le pion est actuellement situé.
    col : Colonne où le pion est actuellement situé.
    plateau : Liste 2D représentant l'état du damier.

    Effets:
    Modifie le plateau pour remplacer le pion par une dame.
    Affiche un message confirmant la transformation.
    """
    """Transforme le pion en dame lorsqu'il atteint le bord."""
    if ligne == 0 or ligne == 7:  # Si le pion atteint le bord du plateau
        plateau[ligne][col] = 'D'  # 'D' représente une dame
        print(f"Le pion en ({ligne}, {col}) est devenu une dame!")


def deplacer_dame(plateau, x1, y1, x2, y2):
    """
    Déplace une dame d'une position à une autre sur le plateau.

    Arguments:
    plateau : Liste 2D représentant le damier.
    x1, y1 : Coordonnées de la position initiale de la dame.
    x2, y2 : Coordonnées de la position cible de la dame.

    Retourne:
    True si le déplacement a été réussi et valide.
    False si le déplacement est invalide ou la destination est occupée.
    """
    """Déplace une dame du plateau de (x1, y1) à (x2, y2)."""
    if abs(x2 - x1) == abs(y2 - y1):  # Vérifie si le mouvement est bien en diagonale
        if plateau[x2][y2] == 0:  # Si la case de destination est vide
            plateau[x2][y2] = plateau[x1][y1]  # Déplace la dame
            plateau[x1][y1] = 0  # Vide la case de départ
            return True
        else:
            print("La case de destination est occupée!")
            return False
    else:
        print("Le mouvement n'est pas en diagonale!")
        return False


def bouge_droite():
    """
    Déplace un pion joueur vers la droite sur le plateau, si possible.

    Effets:
    Efface la position actuelle et met à jour la position du pion.
    Met à jour l'affichage du damier en conséquence.
    """
    """Déplace le pion vers la droite"""
    global screen, case_size, marge_gauche, marge_haut, pion_pos, pion, nb_colonnes
    if pion_pos < (nb_colonnes - 1):
        gfx.dessine_case(pion_pos, 0)
        pion_pos += 1
    screen.blit(pion, (marge_gauche + case_size * pion_pos, marge_haut))


def bouge_gauche():
    """
    Déplace un pion joueur vers la gauche sur le plateau, si possible.

    Effets:
    Efface la position actuelle et met à jour la position du pion.
    Met à jour l'affichage du damier en conséquence.
    """
    """Déplace le pion vers la gauche"""
    global screen, case_size, marge_gauche, marge_haut, pion_pos, pion, nb_colonnes
    if pion_pos > 0:
        gfx.dessine_case(pion_pos, 0)
        pion_pos -= 1
    screen.blit(pion, (marge_gauche + case_size * pion_pos, marge_haut))


def bouge_haut():
    """
    Déplace un pion noir vers le haut sur le plateau, si possible.

    Effets:
    Efface la position actuelle et met à jour la position du pion noir.
    Met à jour l'affichage du damier en conséquence.
    """
    """Déplace le pion noir vers le haut"""
    global screen, case_size, marge_gauche, marge_haut, pion_pos_noir, pion_noir, nb_colonnes
    if pion_pos_noir > 0:
        gfx.dessine_case(0, pion_pos_noir)
        pion_pos_noir -= 1
    screen.blit(pion_noir, (marge_gauche, marge_haut + case_size * pion_pos_noir))


def bouge_bas():
    """
    Déplace un pion noir vers le bas sur le plateau, si possible.

    Effets:
    Efface la position actuelle et met à jour la position du pion noir.
    Met à jour l'affichage du damier en conséquence.
    """
    """Déplace le pion noir vers le bas"""
    global screen, case_size, marge_gauche, marge_haut, pion_pos_noir, pion_noir, nb_colonnes
    if pion_pos_noir < (nb_colonnes - 1):
        gfx.dessine_case(0, pion_pos_noir)
        pion_pos_noir += 1
    screen.blit(pion_noir, (marge_gauche, marge_haut + case_size * pion_pos_noir))


def transformer_en_dame(pion, ligne, col, plateau):
    """Transforme le pion en dame lorsqu'il atteint le bord."""
    if ligne == 0 or ligne == 7:  # Si le pion atteint le bord du plateau
        plateau[ligne][col] = 'D'  # 'D' représente une dame
        print(f"Le pion en ({ligne}, {col}) est devenu une dame!")

        # Utiliser l'image correspondante pour une dame
        if pion == 1:  # Pion blanc
            gfx.screen.blit(gfx.dame_blanche, (
                gfx.marge_gauche + gfx.case_size * col,
                gfx.marge_haut + gfx.case_size * ligne
            ))
        elif pion == 2:  # Pion noir
            gfx.screen.blit(gfx.dame_noir, (
                gfx.marge_gauche + gfx.case_size * col,
                gfx.marge_haut + gfx.case_size * ligne
            ))
        pygame.display.flip()  # Met à jour l'affichage


# Placer les pions sur le plateau
for i in range(5, 8):
    for j in range(8):
        if (i + j) % 2 == 1:  # Placer les pions sur les cases noires (i + j impair)
            gfx.plateau[i][j] = 'p'  # Pion du joueur 2
            # Vérifier si le pion atteint le bord
            transformer_en_dame(gfx.plateau, i, j, gfx.plateau)

