"""
Name    : dame_gfx.py
Auteur  : Lucas Santos & alexian Jaccard
Date    : 14.11.24
Version : 3.7
Purpose : Jeu de dames avec la librairie pygame
"""
import pygame  # Importation de la bibliothèque pygame pour la gestion des jeux 2D

# Initialisation de Pygame
pygame.init()  # Initialisation de tous les modules de pygame

# Définition des couleurs
case_size = 80  # Taille d'une case du damier en pixels

cases_blanches = (255, 255, 255)  # Couleur des cases blanches du damier (blanc)
cases_noires = (1, 215, 88)  # Couleur des cases noires du damier (vert)

# Marges autour du damier
marge_gauche = 10  # Marge sur la gauche du damier pour l'interface
marge_haut = 10  # Marge en haut du damier
marge_droite = 10  # Marge sur la droite du damier
marge_bas = 10  # Marge en bas du damier

# Taille du damier
nb_lignes = 10  # Nombre de lignes sur le plateau du jeu
nb_colonnes = 10  # Nombre de colonnes sur le plateau du jeu

# Taille de la fenêtre
window_size = (case_size * nb_colonnes + marge_gauche + marge_droite,  # Taille de la fenêtre (largeur, hauteur)
               case_size * nb_lignes + marge_haut + marge_bas)  # Calculée avec la taille des cases et marges
window_color = (255, 255, 255)  # Couleur de fond de la fenêtre

# Création de la fenêtre
screen = pygame.display.set_mode(window_size)  # Création de la fenêtre pygame avec la taille définie
pygame.display.set_caption("Jeu de dames")  # Définir le titre de la fenêtre
screen.fill(window_color)  # Remplissage de l'arrière-plan de la fenêtre avec la couleur blanche

# Icone de la fenêtre
path_to_images = "pictures\\pictures\\"  # Chemin vers le dossier contenant les images utilisées
icon = pygame.image.load(path_to_images + "International_draughts.png")  # Chargement de l'icône de la fenêtre
pygame.display.set_icon(icon)  # Définir l'icône de la fenêtre

# Définir le plateau initial (0 pour vide, 1 pour pion blanc, 2 pour pion noir)
plateau = [[0] * nb_colonnes for _ in range(nb_lignes)]  # Initialisation du damier avec des cases vides

# Placer les pions blancs sur les 4 premières lignes (lignes 0 à 3)
for i in range(4):  # Lignes 0, 1, 2, 3
    for j in range(nb_colonnes):
        if (i + j) % 2 == 1:  # Placer un pion uniquement sur les cases noires
            plateau[i][j] = 1  # Initialisation des pions blancs

# Placer les pions noirs sur les 4 dernières lignes (lignes 6 à 9)
for i in range(6, 10):  # Lignes 6, 7, 8, 9
    for j in range(nb_colonnes):
        if (i + j) % 2 == 1:  # Placer un pion uniquement sur les cases noires
            plateau[i][j] = 2  # Initialisation des pions noirs

# Charger les images des pions
pion_blanc = pygame.image.load(path_to_images + "MA-24_pion.png")  # Charger l'image du pion blanc
pion_blanc = pygame.transform.scale(pion_blanc, (case_size, case_size))  # Mise à l'échelle à la taille de la case

pion_noir = pygame.image.load(path_to_images + "MA-24_pion_noir.png")  # Charger l'image du pion noir
pion_noir = pygame.transform.scale(pion_noir, (case_size, case_size))  # Mise à l'échelle à la taille de la case

dame_blanche = pygame.image.load(path_to_images + "MA-24_dame_blanche.png")  # Charger l'image de la dame blanche
dame_blanche = pygame.transform.scale(dame_blanche, (case_size, case_size))  # Mise à l'échelle pour la case

dame_noir = pygame.image.load(path_to_images + "MA-24_dame_noire.png")  # Charger l'image de la dame noire
dame_noir = pygame.transform.scale(dame_noir, (case_size, case_size))  # Mise à l'échelle pour la case





# Fonction pour dessiner une case
def dessine_case(col, row, couleur):  # Dessine une seule case sur le damier avec la couleur donnée
    pygame.draw.rect(screen, couleur,
                     (marge_gauche + col * case_size,  # Calcul des coordonnées en pixels de la case
                      marge_haut + row * case_size,
                      case_size,
                      case_size), 0)


# Fonction pour dessiner toutes les cases du damier
def dessine_toutes_les_cases():
    for row in range(nb_lignes):
        for col in range(nb_colonnes):
            couleur = cases_blanches if (col + row) % 2 == 0 else cases_noires
            dessine_case(col, row, couleur)


# Fonction pour entourer une case
def entourer_case(col, row):
    pygame.draw.rect(screen, (255, 0, 154),  # Rouge pour entourer la case
                     (marge_gauche + col * case_size,
                      marge_haut + row * case_size,
                      case_size,
                      case_size), 5)  # Bordure de 5 pixels
    pygame.display.flip()


# Dessiner le damier
dessine_toutes_les_cases()

# Affichage des pions (blancs et noirs)
for ligne in range(nb_lignes):
    for col in range(nb_colonnes):
        if plateau[ligne][col] == 1:  # Pion blanc
            screen.blit(pion_blanc, (marge_gauche + case_size * col, marge_haut + case_size * ligne))
        elif plateau[ligne][col] == 2:  # Pion noir
            screen.blit(pion_noir, (marge_gauche + case_size * col, marge_haut + case_size * ligne))

pygame.display.flip()

# Variables pour gérer la sélection et le mouvement
pion_selectionne = None
cases_accessibles = []

# Variable pour gérer le tour du joueur
tour_joueur = 1  # 1 pour le joueur blanc, 2 pour le joueur noir


# Calculer les cases accessibles pour un pion donné
def calculer_cases_accessibles(row, col):
    cases_accessibles = []
    if plateau[row][col] == 1:  # Pion blanc
        directions = [(1, -1), (1, 1)]  # Bas gauche, Bas droite
    elif plateau[row][col] == 2:  # Pion noir
        directions = [(-1, -1), (-1, 1)]  # Haut gauche, Haut droite

    # Vérification des captures possibles
    for d in directions:
        dr, dc = d
        nr, nc = row + dr, col + dc
        # Vérification d'un pion adverse à capturer
        if 0 <= nr < nb_lignes and 0 <= nc < nb_colonnes:
            if plateau[nr][nc] != plateau[row][col] and plateau[nr][nc] != 0:
                # Vérifier la case après l'adversaire
                nr2, nc2 = nr + dr, nc + dc
                if 0 <= nr2 < nb_lignes and 0 <= nc2 < nb_colonnes and plateau[nr2][nc2] == 0:
                    cases_accessibles.append((nr2, nc2))  # Ajouter la case après la capture

    # Si aucune capture n'est possible, vérifier les déplacements normaux
    if not cases_accessibles:
        for d in directions:
            dr, dc = d
            nr, nc = row + dr, col + dc
            if 0 <= nr < nb_lignes and 0 <= nc < nb_colonnes and plateau[nr][nc] == 0:
                cases_accessibles.append((nr, nc))

    return cases_accessibles


# Fonction pour déplacer le pion
def deplacer_pion(row, col):
    global plateau, pion_selectionne, cases_accessibles, tour_joueur

    # Vérifier si le mouvement est valide
    if (row, col) in cases_accessibles:
        # Déplacer le pion sur le plateau
        plateau[row][col] = plateau[pion_selectionne[0]][pion_selectionne[1]]
        plateau[pion_selectionne[0]][pion_selectionne[1]] = 0
        # Vérifier si un pion a été mangé et le retirer
        if abs(row - pion_selectionne[0]) > 1 or abs(col - pion_selectionne[1]) > 1:
            # Calculer la position du pion mangé
            mid_row = (row + pion_selectionne[0]) // 2
            mid_col = (col + pion_selectionne[1]) // 2
            plateau[mid_row][mid_col] = 0  # Enlever le pion mangé

        pion_selectionne = None  # Désélectionner le pion
        cases_accessibles = []  # Effacer les cases accessibles

        # Redessiner le damier et les pions
        dessine_toutes_les_cases()
        for ligne in range(nb_lignes):
            for col in range(nb_colonnes):
                if plateau[ligne][col] == 1:
                    screen.blit(pion_blanc, (marge_gauche + case_size * col, marge_haut + case_size * ligne))
                elif plateau[ligne][col] == 2:
                    screen.blit(pion_noir, (marge_gauche + case_size * col, marge_haut + case_size * ligne))
        pygame.display.flip()

        # Passer au tour suivant
        if tour_joueur == 1:
            tour_joueur = 2  # C'est maintenant au tour du joueur noir
        else:
            tour_joueur = 1  # C'est maintenant au tour du joueur blanc


# Boucle principale
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            souris_x, souris_y = pygame.mouse.get_pos()
            col = (souris_x - marge_gauche) // case_size
            row = (souris_y - marge_haut) // case_size

            # Si on a sélectionné un pion et c'est le tour du joueur
            if plateau[row][col] == tour_joueur:  # Vérifier si le joueur peut déplacer son pion
                pion_selectionne = (row, col)
                cases_accessibles = calculer_cases_accessibles(row, col)
                # Effacer les anciennes cases accessibles
                dessine_toutes_les_cases()
                # Redessiner les pions
                for ligne in range(nb_lignes):
                    for col in range(nb_colonnes):
                        if plateau[ligne][col] == 1:
                            screen.blit(pion_blanc, (marge_gauche + case_size * col, marge_haut + case_size * ligne))
                        elif plateau[ligne][col] == 2:
                            screen.blit(pion_noir, (marge_gauche + case_size * col, marge_haut + case_size * ligne))
                pygame.display.flip()

                # Entourer les cases accessibles devant le pion
                for case in cases_accessibles:
                    entourer_case(case[1], case[0])

            # Si on clique sur une case accessible
            if pion_selectionne:
                # Vérifier s'il y a une capture obligatoire
                capture_possible = any(abs(row - pion_selectionne[0]) > 1 or abs(col - pion_selectionne[1]) > 1 for (row, col) in cases_accessibles)

                if capture_possible:
                    # Si une capture est obligatoire, ne permettre que les cases de capture
                    if (row, col) in cases_accessibles and abs(row - pion_selectionne[0]) > 1:
                        deplacer_pion(row, col)
                elif (row, col) in cases_accessibles:
                    # Si aucune capture n'est obligatoire, on peut déplacer normalement
                    deplacer_pion(row, col)

pygame.quit()