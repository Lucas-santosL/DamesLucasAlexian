import dame_gfx
import dame_main
import pygame


def bouger_pion(pion, pion_ligne, pion_pos, nouvelle_ligne, nouvelle_pos):
    """Déplace le pion du damier, met à jour l'affichage"""
    # Efface l'ancienne position
    couleur_case = cases_blanches if (pion_pos + pion_ligne) % 2 else cases_noires
    dessine_case(pion_pos, pion_ligne, couleur_case)

    # Met à jour la nouvelle position
    pion_ligne = nouvelle_ligne
    pion_pos = nouvelle_pos
    # Affiche le pion à sa nouvelle position
    screen.blit(pion, (marge_gauche + case_size * pion_pos, marge_haut + case_size * pion_ligne))

    return pion_ligne, pion_pos


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

        #pygame.display.update()