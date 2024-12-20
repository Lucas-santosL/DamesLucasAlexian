"""
Name    : dame_regle.py
Auteur  : Lucas Santos & Alexian Jaccard
Date    : 14.11.24
Version : 3.7
Purpose : Gestion des règles du jeu de dames
"""
import dame_gfx as gfx

def bouger_pion(pion, pion_ligne, pion_pos, nouvelle_ligne, nouvelle_pos):
    """Déplace le pion du damier, met à jour l'affichage"""
    couleur_case = gfx.cases_blanches if (pion_pos + pion_ligne) % 2 else gfx.cases_noires
    gfx.dessine_case(pion_pos, pion_ligne, couleur_case)

    pion_ligne = nouvelle_ligne
    pion_pos = nouvelle_pos
    gfx.screen.blit(pion, (gfx.marge_gauche + gfx.case_size * pion_pos, gfx.marge_haut + gfx.case_size * pion_ligne))
    return pion_ligne, pion_pos

def deplacer_pion(plateau, x1, y1, x2, y2):
    """
    Déplace un pion du plateau de (x1, y1) à (x2, y2).
    Vérifie si la destination est vide (0) et met à jour les coordonnées du pion sélectionné.
    """
    if plateau[x2][y2] == 0:
        plateau[x2][y2] = plateau[x1][y1]
        plateau[x1][y1] = 0
        gfx.selected_pion_x, gfx.selected_pion_y = x2, y2
        return True
    else:
        print("La case de destination est occupée ou hors limites!")
        return False