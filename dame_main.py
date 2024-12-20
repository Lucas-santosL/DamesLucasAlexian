"""
Name    : dame_main.py
Auteur  : Lucas Santos & alexian Jaccard
Date    : 14.11.24
Version : 3.7
Purpose : Jeu de dames avec la librairie pygame
"""
import dame_regle as regle
import dame_gfx as gfx
import pygame

# Initialisation de Pygame
pygame.init()

# Initialisation du plateau (10x10 avec 0 pour case vide, 1 pour pions blancs, 2 pour pions noirs)
plateau = [[0 if (i + j) % 2 == 0 else (1 if i < 4 else (2 if i > 5 else 0)) for j in range(10)] for i in range(10)]
gfx.afficher_plateau(plateau)
gfx.dessine_plateau(plateau)

# Boucle principale
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()


pygame.quit()