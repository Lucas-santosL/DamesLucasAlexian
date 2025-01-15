import pygame

# Initialisation de Pygame
pygame.init()

# Définition des couleurs
case_size = 80
cases_blanches = (255, 255, 255)
cases_noires = (1, 215, 88)

# Marges autour du damier
marge_gauche = 10
marge_haut = 10
marge_droite = 10
marge_bas = 10

# Taille du damier
nb_lignes = 10
nb_colonnes = 10

# Taille de la fenêtre
window_size = (case_size * nb_colonnes + marge_gauche + marge_droite,
               case_size * nb_lignes + marge_haut + marge_bas)
window_color = (255, 255, 255)

# Création de la fenêtre
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Jeu de dames")
screen.fill(window_color)

# Icone de la fenêtre
path_to_images = "pictures\\pictures\\"  # Assure-toi que le chemin est correct
icon = pygame.image.load(path_to_images + "International_draughts.png")
pygame.display.set_icon(icon)

# Définir le plateau initial (0 pour vide, 1 pour pion blanc, 2 pour pion noir)
plateau = [[0] * nb_colonnes for _ in range(nb_lignes)]

# Placer les pions blancs sur les 4 premières lignes (lignes 0 à 3)
for i in range(4):  # Lignes 0, 1, 2, 3
    for j in range(nb_colonnes):
        if (i + j) % 2 == 1:  # Placer sur les cases vertes
            plateau[i][j] = 1  # Pion blanc

# Placer les pions noirs sur les 4 dernières lignes (lignes 6 à 9)
for i in range(6, 10):  # Lignes 6, 7, 8, 9
    for j in range(nb_colonnes):
        if (i + j) % 2 == 1:  # Placer sur les cases vertes
            plateau[i][j] = 2  # Pion noir

# Charger les images des pions
pion_blanc = pygame.image.load(path_to_images + "MA-24_pion.png")
pion_blanc = pygame.transform.scale(pion_blanc, (case_size, case_size))

pion_noir = pygame.image.load(path_to_images + "MA-24_pion_noir.png")
pion_noir = pygame.transform.scale(pion_noir, (case_size, case_size))


# Fonction pour dessiner une case
def dessine_case(col, row, couleur):
    pygame.draw.rect(screen, couleur,
                     (marge_gauche + col * case_size,
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

    # Vérification des cases accessibles devant le pion
    for d in directions:
        dr, dc = d
        nr, nc = row + dr, col + dc
        if 0 <= nr < nb_lignes and 0 <= nc < nb_colonnes and plateau[nr][nc] == 0:
            cases_accessibles.append((nr, nc))

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
                deplacer_pion(row, col)

pygame.quit()
