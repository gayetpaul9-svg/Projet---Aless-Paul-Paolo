"""
Point d'entrée principal du projet GPS du lycée.
Gère la boucle Pygame, les interfaces, et les interactions utilisateur.
Ce module contient la boucle principale de jeu et le rendu des écrans.
"""
import pygame
import math
import os
from pygame.draw import rect
from pytmx.util_pygame import load_pygame
import classes
import fonctions
from fonctions import liste_etage
from layers import layers_1, layers_2, layers_3, layers_cdi, layers_1B, noms_etages, dico_etage, layers


#initialisation pygame
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode()
fond_image = pygame.image.load("assets/civ.png").convert()
fond_image = pygame.transform.scale(fond_image, screen.get_size())
pygame.mixer.music.load("assets/sons_fond.mp3")
pygame.mixer.music.set_volume(1)
pygame.mixer.music.play(-1)
son_clic = pygame.mixer.Sound("assets/effet_sonore.mp3")
font = pygame.font.SysFont(None, 36)
clock = pygame.time.Clock()
clock.tick(60)
info = pygame.display.Info()
selection_type = "start"
images = {
    'loupe': pygame.image.load("assets/loupe.png").convert_alpha(),
    'civ': pygame.image.load("assets/civ.png").convert(),
    'marque': pygame.image.load("assets/marque.png").convert(),
    'verifier': pygame.image.load("assets/verifier.png").convert(),
    'P1': pygame.image.load('assets/P1.jpg').convert(),
    'P2': pygame.image.load('assets/P2.jpg').convert(),
    'P3': pygame.image.load('assets/P3.jpg').convert(),
    'P4': pygame.image.load('assets/P4.jpg').convert(),
    'P5': pygame.image.load('assets/P5.jpg').convert(),
    'P6': pygame.image.load('assets/P6.jpg').convert(),
    'P7': pygame.image.load('assets/P7.jpg').convert(),
    'P8': pygame.image.load('assets/P8.jpg').convert(),
    'P9': pygame.image.load('assets/P9.jpg').convert(),
    'P10': pygame.image.load('assets/P10.jpg').convert(),
    'P11': pygame.image.load('assets/P11.jpg').convert(),
    'P12': pygame.image.load('assets/P12.jpg').convert(),
    'P13': pygame.image.load('assets/P13.jpg').convert(),
    'P14': pygame.image.load('assets/P14.jpg').convert(),
    'P15': pygame.image.load('assets/P15.jpg').convert(),
    'P16': pygame.image.load('assets/P16.jpg').convert(),
    'P17': pygame.image.load('assets/P17.jpg').convert(),
    'P18': pygame.image.load('assets/P18.jpg').convert(),
    'P19': pygame.image.load('assets/P19.jpg').convert(),
    'P20': pygame.image.load('assets/P20.jpg').convert(),}

# Variables globales
# Ces variables contrôlent principalement l'apparence et l'état de l'interface.
afficher = False
afficher_s = False
vert=(150,255,150)
gris=(200,200,200)
rouge=(255,150,150)
normale=(240,240,240)
long=False
etat = "accueil"
running = True
saisie_active = False
texte_saisi = ""
infos_cours_result = None
options_ouvert = False
fonc={'calories' : "0", 'temps' : "0"}
etage = 5
chemins1B = []
chemins1 = []
chemins_cdi = []
chemins2 = []
chemins3 = []
chemins = [chemins1, chemins2, chemins3]
mode_long = False
time = 0
base_color = (100, 150, 255)
batiment_selectionne = None
show_image = False
current_image = None

#importation des données de la carte 
tmx_data = load_pygame("maps/map B300 x4.tmx")
tmx_data_b = load_pygame("maps/map B200-A200 x4.tmx")
tmx_data_c = load_pygame("maps/map CDI.tmx")
tmx_data_d = load_pygame("maps/map A100.tmx")
tmx_data_e = load_pygame("maps/B100.tmx")
TILE_SIZE = tmx_data.tileheight
map_width = tmx_data.width * TILE_SIZE
map_height = tmx_data.height * TILE_SIZE
offset_x = (screen.get_width() - map_width) // 2
offset_y = (screen.get_height() - map_height) // 2


#bouttons
menu_ouvert = False
afficher_loupe = classes.Button(1386, info.current_h-195, 140, 40, "🔍",font=pygame.font.Font("assets/DejaVuSans.ttf", 15))
afficher_loupe.font.set_bold(True)
afficher_salles = classes.Button(1386, info.current_h-245, 140, 40, "🏫",font=pygame.font.Font("assets/DejaVuSans.ttf", 15))
afficher_salles.font.set_bold(True)
etage_sup=classes.Button(1386, info.current_h-145, 40, 40, "↑",font=pygame.font.Font("assets/DejaVuSans.ttf", 15))
etage_inf=classes.Button(1386, info.current_h-105, 40, 40, "↓",font=pygame.font.Font("assets/DejaVuSans.ttf", 15))
etage_suivant=classes.Button(1286+40, info.current_h-105, 40, 40, "->",font=pygame.font.Font("assets/DejaVuSans.ttf", 15))
etage_precedent=classes.Button(1286, info.current_h-105, 40, 40, "<-",font=pygame.font.Font("assets/DejaVuSans.ttf", 15))
ui_1=classes.Button(info.current_w-340-50,236, 340, 50,text="",font=pygame.font.Font("assets/DejaVuSans.ttf", 15))
ui_2=classes.Button(info.current_w-340-50,236+50, 340, 50,text="",font=pygame.font.Font("assets/DejaVuSans.ttf", 15))
ui_3=classes.Button(info.current_w-340-50,236+50+50, 340, 50,text="",font=pygame.font.Font("assets/DejaVuSans.ttf", 15))
ui_4=classes.Button(info.current_w-340-50,236+50+50+50, 340, 50,text="",font=pygame.font.Font("assets/DejaVuSans.ttf", 15))
bouton_mode_long = None  # disabled
bat_a=classes.Button(info.current_w-447, info.current_h-145, 200, 80)
bat_b=classes.Button(info.current_w-447+200+5, info.current_h-145, 200, 80)
salles_par_etage = {
    "Bâtiment A - 3ème": ["Retour","A301","A302","A303","A304","A305","A306","A307","A308",""],
    "Bâtiment A - 2ème": ["Retour","A201","A202","A203","A204","A205","A206","A207","A208","A209","A210","A211",""],
    "Bâtiment A - 1er": ["Retour","A102","A103","A104","A105","A106",""],
    "Bâtiment A - RDC": ["Retour","A001","A002","A003","A004","A005","A006","A007","A008","A010","A011","A012","A013","A014",""],
    "Bâtiment B - 3ème": ["Retour","B311","B312","B313","B314","B315","B316","B317","B318","B319","B320","B321","B322","B323","B324","B325",""],
    "Bâtiment B - 2ème": ["Retour","B214","B215","B216","B217","B218","B219","B220","B221","B222","B223",""],
    "Bâtiment B - 1er": ["Retour","B111","B112","B113","B114","B115","B116","B117","B118",""]}
menu_deroulant= classes.Dropdown(50, 50, 250, 40, [
    "Bâtiment A - 3ème","Bâtiment A - 2ème","Bâtiment A - 1er","Bâtiment A - RDC",
    "Bâtiment B - 3ème","Bâtiment B - 2ème","Bâtiment B - 1er",""],sous_options=salles_par_etage)
menu_matiere= classes.Dropdown(320,50,250,40, [
    "maths","physique-chimie","francais", "histoire-geo", "hggsp", "hlp",
    "ses", "nsi", "sport", "italien", "anglais", "allemand", "espagnol",
    "russe", "fls", "cdm", "histoire-geo si", "chinois", ""],titre="Cours ?", single=True)
nom_etage=classes.Button(info.current_w//2-125, 13, 250, 30)
bouton_options_x = screen.get_width() - 250
bouton_options_y = 50
bouton_options_largeur = 200
bouton_options_hauteur = 40
couleur_bouton_options = (240, 240, 240)
couleur_bouton_options_a = (240, 240, 240)
couleur_bouton_options_b = (240, 240, 240)
ui_3.font.set_bold(True)
ui_2.font.set_bold(True)
ui_1.font.set_bold(True)
ui_4.font.set_bold(True)
# map_buttons_info: on associe des coordonnées, un étage et une image à chaque bouton
def create_map_button(x, y, floor, image):
    return {
        'button': classes.Button(offset_x + x, offset_y + y, 20, 20),
        'floors': [floor],
        'image': image}
map_data = {
    1: [('P1', 180, 650), ('P2', 220, 320), ('P3', 370, 270)],
    2: [('P4', 500, 145), ('P5', 220, 405), ('P6', 250, 665)],
    3: [('P7', 400, 260), ('P8', 215, 670)],
    4: [
        ('P9', 300, 100), ('P10', 170, 318), ('P11', 330, 330),
        ('P12', 370, 530), ('P13', 350, 690), ('P14', 415, 750),
        ('P15', 320, 895)
    ],
    5: [
        ('P16', 165, 130), ('P17', 185, 350), ('P18', 70, 592),
        ('P19', 300, 620), ('P20', 345, 872)]}
map_buttons_info = []
for floor, points in map_data.items():
    for image, x, y in points:
        map_buttons_info.append(create_map_button(x, y, floor, image))
# boutons_salles: on associe des coordonnée et un étage à chaque bouton
taille_txt = pygame.font.Font("assets/DejaVuSans.ttf", 18)
def create_button(label, x, y, floor):
    return {
        'label': label,
        'button': classes.Button(offset_x + x, offset_y + y, 60, 20, label, font=taille_txt),
        'floors': [floor],}
data = {
    1: [
        ('A001', 402, 272), ('A002', 430, 722), ('A003', 340, 722),
        ('A004', 340, 802), ('A005', 255, 722), ('A006', 155, 477),
        ('A007', 155, 432), ('A008', 155, 332), ('A009', 165, 272),
        ('A010', 15, 287), ('A011', 4, 352), ('A012', 4, 412),
        ('A013', 4, 477), ('A014', 20, 572),
    ],
    2: [
        ('B111', 206, 812), ('B112', 276, 717), ('B113', 315, 625),
        ('B114', 166, 333), ('B115', 153, 192), ('B116', 300, 205),
        ('B117', 407, 205), ('B118', 495, 205),
    ],
    3: [
        ('A101', 429, 86), ('A102', 312, 199), ('A103', 213, 199),
        ('A104', 117, 199), ('A105', 20, 199), ('A106', 131, 607),
        ('A107', 28, 607), ('A108', 28, 737), ('A109', 28, 808),
        ('A110', 28, 855),
    ],
    4: [
        ('A201', 113, 345), ('A202', 138, 302), ('A203', 180, 275),
        ('A204', 218, 302), ('A205', 261, 246), ('A206', 261, 170),
        ('A207', 261, 52), ('A208', 304, 368), ('A209', 304, 415),
        ('A210', 304, 457), ('A211', 307, 506), ('A212', 394, 514),
        ('B213', 389, 654), ('B214', 307, 647), ('B215', 254, 642),
        ('B216', 203, 690), ('B217', 285, 731), ('B218', 352, 731),
        ('B219', 362, 783), ('B220', 362, 826), ('B221', 362, 868),
        ('B222', 440, 914), ('B223', 320, 914),
    ],
    5: [
        ('A301', 33, 52), ('A302', 97, 52), ('A303', 155, 52),
        ('A304', 98, 90), ('A305', 98, 144), ('A306', 98, 204),
        ('A307', 98, 263), ('A308', 98, 318), ('A309', 203, 158),
        ('A310', 203, 246), ('B311', 200, 427), ('A312', 149, 530),
        ('B313', 20, 530), ('B314', 175, 633), ('B315', 280, 705),
        ('B316', 280, 763), ('B317', 280, 824), ('B318', 296, 889),
        ('B319', 369, 882), ('B320', 430, 882), ('B321', 501, 882),
        ('B322', 493, 842), ('B323', 435, 810), ('B324', 393, 842),
        ('B325', 359, 810),
    ]
}
boutons_salles = []
for floor, rooms in data.items():
    for label, x, y in rooms:
        boutons_salles.append(create_button(label, x, y, floor))
# Fermer bouton image
close_button = classes.Button(screen.get_width() - 50, 10, 40, 40, "X", font=pygame.font.Font("assets/DejaVuSans.ttf", 20))




_,chemins = fonctions.gps(None,None,tmx_data, tmx_data_b, tmx_data_d, tmx_data_c, tmx_data_e, layers_2, layers_3, layers_1, layers_cdi, layers_1B)
# boucle principale
# La boucle principale tourne tant que la variable 'running' est True.
# Elle gère l'état de l'application : "accueil" ou "itinéraire",
# l'affichage des éléments, et le traitement des événements utilisateur.
while running:
    # 1) Affichage selon l'état courant : accueil ou itinéraire
    # pages d'accueil et d'itinéraire
    if etat == "accueil":
        pygame.mixer.music.stop()
        pygame.mixer.music.play(-1)
        screen.blit(fond_image, (0, 0))
        titre_font = pygame.font.SysFont(None, 120)
        titre = titre_font.render("GPS CIV", True, (255, 255, 255))
        screen.blit(titre, (screen.get_width()//2 - titre.get_width()//2, 180))
        pygame.draw.rect(screen, (220, 220, 255), (screen.get_width()//2 - 200, 350, 400, 80))
        jouer_txt = pygame.font.SysFont(None, 60).render("ITINÉRAIRE", True, (0, 0, 0))
        screen.blit(jouer_txt, (screen.get_width()//2 - jouer_txt.get_width()//2, 375))
        pygame.draw.rect(screen, (220, 220, 255), (screen.get_width()//2 - 200, 450, 400, 80))
        opt_txt = pygame.font.SysFont(None, 60).render("DOCUMENTATION", True, (0, 0, 0))
        screen.blit(opt_txt, (screen.get_width()//2 - opt_txt.get_width()//2, 475))
    
    elif etat == "itinéraire":
        screen.fill((255, 255, 255))
        # Draw the map tiles
        for m in range(1):
            for  layer in chemins[etage-1]:
                for x, y, image in layer.tiles():
                    screen.blit(image, (offset_x + x * TILE_SIZE, offset_y + y * TILE_SIZE))
        pos_souris = pygame.mouse.get_pos()
        if bouton_options_x <= pos_souris[0] <= bouton_options_x + bouton_options_largeur and bouton_options_y <= pos_souris[1] <= bouton_options_y + bouton_options_hauteur:
            couleur_bouton_options = (180, 180, 180)
        else:
            couleur_bouton_options = (240, 240, 240)




    # 2) Gestion des événements de Pygame
    #    - fermeture de la fenêtre
    #    - défilement souris pour les menus déroulants
    #    - navigation clavier
    #    - clics souris sur boutons et éléments interactifs
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            # l'utilisateur ferme la fenêtre, on arrête la boucle
            running = False
        elif e.type == pygame.MOUSEWHEEL:
            if menu_deroulant.sous_menu_ouvert is not None:
                sous_menu = menu_deroulant.sous_menus[menu_deroulant.sous_menu_ouvert]
                sous_menu.offset_y += e.y * 20
                sous_menu.offset_y = min(-189, sous_menu.offset_y)
                sous_menu.offset_y = max(-189 - (len(sous_menu.options) - 9) * 40, sous_menu.offset_y)
                sous_menu.scroll_options()
            else:
                menu_deroulant.offset_y += e.y * 20
                menu_deroulant.offset_y = min(-189, menu_deroulant.offset_y)
                menu_deroulant.offset_y = max(-189, menu_deroulant.offset_y)
                menu_deroulant.scroll_options()
                menu_matiere.offset_y += e.y *20
                menu_matiere.offset_y = min(-189, menu_matiere.offset_y)
                menu_matiere.offset_y = max(-429, menu_matiere.offset_y)
                menu_matiere.scroll_options()
        elif e.type == pygame.KEYDOWN:
            if e.key == pygame.K_ESCAPE:
                if etat == "itinéraire":
                    etat = "accueil"
                else:
                    running = False
            if e.key == pygame.K_UP and etat == "itinéraire":
                etage = min(etage + 1, 5)
            if e.key == pygame.K_DOWN and etat == "itinéraire":
                etage = max(etage - 1, 1)
            if e.key == pygame.K_BACKSPACE and saisie_active:
                texte_saisi = texte_saisi[:-1]
            if e.key == pygame.K_RETURN and saisie_active and texte_saisi != "":
                infos_cours_result = fonctions.infos_cours(texte_saisi)
                saisie_active = False
                classes.départ_salle = texte_saisi
        elif e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
            mx, my = e.pos
            # Fermer l'image de la loupe si elle est affichée
            if show_image:
                show_image = False
                current_image = None
                continue
            # Réinitialiser les boutons loupe
            if afficher == True:
                for info_btn in map_buttons_info:
                    info_btn['button'].clicked = False
            if afficher_s == True:
                for info_btn in boutons_salles:
                    info_btn['button'].clicked = False
            if bat_a.is_clicked(e.pos):
                batiment_selectionne = "A"
                if etage == 2:
                    etage = 3
                son_clic.play()
            if bat_b.is_clicked(e.pos):
                batiment_selectionne = "B"
                if etage == 3:
                    etage = 2
                son_clic.play()
            if etat == "accueil":
                # Clic sur ITINÉRAIRE
                if (screen.get_width()//2 - 200 <= mx <= screen.get_width()//2 + 200 and
                    350 <= my <= 430):
                    son_clic.play()
                    etat = "itinéraire"
                # Clic sur DOCUMENTATION
                elif (screen.get_width()//2 - 200 <= mx <= screen.get_width()//2 + 200 and
                    450 <= my <= 530):
                    son_clic.play()
                    # Ouvrir le fichier DOCUMENTATION.txt avec le programme par défaut
                    os.startfile("DOCUMENTATION.txt")


            elif etat == "itinéraire":
                if menu_deroulant.sous_menu_ouvert is not None:
                    sous_menu = menu_deroulant.sous_menus[menu_deroulant.sous_menu_ouvert]
                    sous_menu.type = selection_type
                    sous_menu.handle_click(e.pos)
                    selection_type = sous_menu.type
                    if sous_menu.action:
                        menu_deroulant.action = True
                        sous_menu.action = False
                        sous_menu.open = False
                        sous_menu.reset_colors()
                        menu_deroulant.sous_menu_ouvert = None
                        selection_type = "start"
                    if not sous_menu.open:
                        menu_deroulant.sous_menu_ouvert = None
                        menu_deroulant.open = True
                else:
                    menu_deroulant.handle_click(e.pos)
                if menu_deroulant.open:
                    infos_cours_result = None
                if saisie_active and not menu_deroulant.open:
                    menu_matiere.handle_click(e.pos)
                if etage_sup.is_clicked(e.pos):
                    etage = min(etage + 1, 5)
                    son_clic.play()
                if etage_inf.is_clicked(e.pos):
                    etage = max(etage - 1, 1)
                    son_clic.play()
                if etage_precedent.is_clicked(e.pos):
                    for x in liste_etage:
                        if x==etage and liste_etage.index(x)>0:
                            etage = liste_etage[liste_etage.index(etage)-1]
                            break
                    son_clic.play() 
                if etage_suivant.is_clicked(e.pos):
                    for x in liste_etage:
                        if x==etage and liste_etage.index(x)<len(liste_etage)-1:
                            etage = liste_etage[liste_etage.index(etage)+1]
                            break
                    son_clic.play()
                if e.pos[0] >= 1386 and e.pos[0] <= 1426 and e.pos[1] >= 934 and e.pos[1] <= 974:
                    son_clic.play()
                # Afficher boutons loupe filtrés par étage
                if afficher_loupe.is_clicked(e.pos):
                    afficher = not afficher
                    son_clic.play()
                if afficher_salles.is_clicked(e.pos):
                    afficher_s = not afficher_s
                    son_clic.play()
                # Boutons loupe sur la carte
                if afficher == True:
                    for info_btn in map_buttons_info:
                        btn = info_btn['button']
                        if etage not in info_btn['floors']:
                            continue
                        if btn.is_clicked(e.pos):
                            btn.clicked = True
                            show_image = True
                            current_image = images[info_btn['image']]
                            son_clic.play()
                            break




    # 3) Mise à jour de l'affichage de l'itinéraire et du menu déroulant
    #    Cette section se charge de :
    #      - mettre en surbrillance les boutons d'étage et de bâtiment
    #      - calculer et afficher les informations de cours / itinéraire
    #      - afficher les contrôles et menus interactifs
    if etat == "itinéraire":
        # fonctionnement boutons étages et bâtiments
        if etage == 1 :
            couleur_bouton_options_a = gris
            couleur_bouton_options_b = gris
        elif etage == 3 :
            couleur_bouton_options_a = normale
            couleur_bouton_options_b = normale
        elif etage == 2 :
            couleur_bouton_options_a = normale
            couleur_bouton_options_b = normale
        elif etage == 4 :
            couleur_bouton_options_a = gris
            couleur_bouton_options_b = gris
        elif etage == 5 :
            couleur_bouton_options_a = gris
            couleur_bouton_options_b = gris
        if batiment_selectionne == "A" and etage in [2, 3]:
            couleur_bouton_options_a = vert
            couleur_bouton_options_b = normale
        elif batiment_selectionne == "B" and etage in [2, 3]:
            couleur_bouton_options_a = normale
            couleur_bouton_options_b = vert
        else:
            batiment_selectionne = None

        etage_sup.draw(screen, top_left=5, top_right=5, bottom_right=0, bottom_left=00)
        etage_inf.draw(screen, top_left=0, top_right=0, bottom_right=5, bottom_left=5)
        nom_etage.draw(screen, text=noms_etages[etage], top_left=10, top_right=10, bottom_right=10, bottom_left=10)
        afficher_loupe.draw(screen, text="Afficher loupes", top_left=10, top_right=10, bottom_right=10, bottom_left=10)
        afficher_salles.draw(screen, text="Afficher salles", top_left=10, top_right=10, bottom_right=10, bottom_left=10)
        menu_deroulant.draw(screen, font)
        menu_deroulant.survol(pygame.mouse.get_pos())
        etage_sup.survol(pygame.mouse.get_pos())
        etage_inf.survol(pygame.mouse.get_pos())
        if menu_matiere.action == True:
            infos_cours_result = fonctions.infos_cours(classes.matiere_choisie)
            saisie_active = False
            menu_matiere.action = False
        if menu_deroulant.opening==True:
            menu_deroulant.opening=False
            infos_cours_result = None
        if menu_deroulant.action==True:
            infos_cours_result = None
            _,chemins = fonctions.gps(classes.départ_salle, classes.arrivée_salle, tmx_data, tmx_data_b, tmx_data_d, tmx_data_c,tmx_data_e, layers_2, layers_3, layers_1, layers_cdi,layers_1B,mode_long)
            fonc=fonctions.fonctionnalitees(classes.départ_salle, classes.arrivée_salle)
            for layer in layers:
                if classes.départ_salle in layer:
                    break
            for cle, v in dico_etage.items():
                if v == layer:
                    etage = cle
                    break
            menu_deroulant.action=False
            menu_deroulant.open=False
            saisie_active = True
            texte_saisi = ""
            infos_cours_result = None

        if infos_cours_result is not None and not saisie_active:
            texte_ennui = "Ennui : " + infos_cours_result['message_ennui']
            texte_message = infos_cours_result['message']
            screen.blit(font.render(texte_ennui, True, (0, 0, 0)), (50, 150))
            lignes_message = texte_message.split("\n")
            for i, ligne in enumerate(lignes_message):
                screen.blit(font.render(ligne.strip(), True, (0, 0, 0)), (50, 190 + i * 40))
        if liste_etage:
            etage_suivant.draw(screen, text="→", top_left=0, top_right=5, bottom_right=5, bottom_left=0)
            etage_precedent.draw(screen, text="←", top_left=5, top_right=0, bottom_right=0, bottom_left=5)
        nom_etage.draw(screen, text=noms_etages[etage], top_left=10, top_right=10, bottom_right=10, bottom_left=10)
        menu_deroulant.survol(pygame.mouse.get_pos())
        fonctions_ = str("calories : " + fonc['calories']+" Kcal")
        ui_1.draw(screen, top_left=10, top_right=10, bottom_left=0, bottom_right=0, text=fonctions_)
        fonctions_= "  " +str("temps : " + fonc["temps"]+" s")
        ui_2.draw(screen, top_left=0, top_right=0, bottom_left=0, bottom_right=0, text=fonctions_)
        ui_3.draw(screen,text=classes.départ_salle+"→"+classes.arrivée_salle,top_left=0, top_right=0, bottom_right=0, bottom_left=0)
        ui_4.draw(screen, text="parcoure : " + "→".join(noms_etages[e] for e in liste_etage), top_left=0, top_right=0, bottom_left=10, bottom_right=10)
        bat_a.draw(screen, text="Bâtiment : A", color=couleur_bouton_options_a,
           top_left=10, top_right=10, bottom_right=10, bottom_left=10)
        bat_b.draw(screen, text="Bâtiment : B", color=couleur_bouton_options_b,
           top_left=10, top_right=10, bottom_right=10, bottom_left=10)
        if afficher == True:
                        for info_btn in map_buttons_info:
                            btn = info_btn['button']
                            if etage not in info_btn['floors']:
                                continue
                            color = (0, 255, 0) if btn.is_clicked else (255, 0, 0)
                            btn.draw(screen, top_left=0, top_right=0, bottom_right=0, bottom_left=0, color=color)
        if afficher_s == True:
                        for info_btn in boutons_salles:
                            btn = info_btn['button']
                            if etage not in info_btn['floors']:
                                continue
                            color = (200, 200, 200)
                            btn.draw(screen, top_left=5, top_right=5, bottom_right=5, bottom_left=5, color=color)
    if saisie_active and not options_ouvert:
        menu_matiere.draw(screen, font)
        menu_matiere.survol(pygame.mouse.get_pos())




    # Affichage de l'image de la loupe lorsqu'un bouton est cliqué
    if show_image and current_image is not None:
        # Afficher un fond semi-transparent
        overlay = pygame.Surface((screen.get_width(), screen.get_height()))
        overlay.set_alpha(128)
        overlay.fill((0, 0, 0))
        screen.blit(overlay, (0, 0))

        # Redimensionner l'image si elle est trop grande
        img_width, img_height = current_image.get_size()
        max_width = screen.get_width() * 0.8
        max_height = screen.get_height() * 0.8

        if img_width > max_width or img_height > max_height:
            ratio = min(max_width / img_width, max_height / img_height)
            new_width = int(img_width * ratio)
            new_height = int(img_height * ratio)
            scaled_image = pygame.transform.scale(current_image, (new_width, new_height))
        else:
            scaled_image = current_image

        # Centrer l'image
        img_x = (screen.get_width() - scaled_image.get_width()) // 2
        img_y = (screen.get_height() - scaled_image.get_height()) // 2
        screen.blit(scaled_image, (img_x, img_y))

        # Afficher un message pour fermer
        close_text = font.render("Cliquez n'importe où pour fermer", True, (255, 255, 255))
        screen.blit(close_text, (screen.get_width()//2 - close_text.get_width()//2, img_y + scaled_image.get_height() + 20))

    pygame.display.flip()
pygame.quit()
