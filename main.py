#
# from pydoc import text
import pygame
from pygame.draw import rect 
from pytmx.util_pygame import load_pygame
import classes 
import fonctions
from layers import layers_1, layers_2, layers_3, layers_cdi, layers_1B, noms_etages
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


# Variables globales
long=False
etat = "accueil"
running = True
saisie_active = False
texte_saisi = ""
infos_cours_result = None
options_ouvert = False
fonc={
    'calories' : "0",
    'temps' : "0"
}
etage = 5
chemins1B = []
chemins1 = []
chemins_cdi = []
chemins2 = []
chemins3 = []
chemins = [chemins1, chemins2, chemins3]
mode_long = False

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
coodonnées_souris=classes.Button(10,10,200,40,)
etage_sup=classes.Button(1386, info.current_h-145, 40, 40, "↑",font=pygame.font.Font("assets/DejaVuSans.ttf", 15))
etage_inf=classes.Button(1386, info.current_h-105, 40, 40, "↓",font=pygame.font.Font("assets/DejaVuSans.ttf", 15))
ui_1=classes.Button(info.current_w-340-50,236, 340, 50,text="",font=pygame.font.Font("assets/DejaVuSans.ttf", 15))
ui_2=classes.Button(info.current_w-340-50,236+50, 340, 50,text="",font=pygame.font.Font("assets/DejaVuSans.ttf", 15))
bouton_mode_long = classes.Button(info.current_w//2-160,info.current_h//2-25, 320, 50, 
                                  "Itinéraire le plus long")
menu_deroulant= classes.Dropdown(50, 50, 250, 40, [
    "A301","A302","A303","A304","A305","A306","A307","A308",

    "A201","A202","A203","A204","A205","A206","A207","A208","A209","A210",
    "A211","A102","A103", "A104","A105","A106","A001","A002","A003","A004",
    "A005","A006","A007","A008","A010","A011","A012","A013","A014",

    "B111","B112","B113","B114","B115","B116","B117","B118",

    "B214","B215","B216","B217","B218","B219","B220","B221","B222","B223",

    "B311","B312","B313","B314","B315","B316","B317","B318","B319","B320",
    "B321","B322","B323","B324","B325",""
])
menu_matiere= classes.Dropdown(320,50,250,40, [
    "maths","physique-chimie","francais", "histoire-geo", "hggsp", "hlp",
    "ses", "nsi", "sport", "italien", "anglais", "allemand", "espagnol",
    "russe", "fls", "cdm", "histoire-geo si", "chinois", ""
],titre="Cours ?")
nom_etage=classes.Button(info.current_w//2-125, 13, 250, 30)
bouton_options_x = screen.get_width() - 250
bouton_options_y = 50
bouton_options_largeur = 200
bouton_options_hauteur = 40
couleur_bouton_options = (240, 240, 240)
couleur_bouton_options_a = (240, 240, 240)
couleur_bouton_options_b = (240, 240, 240)
bat_a=classes.Button(info.current_w-447, info.current_h-145, 200, 80)
bat_b=classes.Button(info.current_w-447+200+5, info.current_h-145, 200, 80)
batiment_selectionne = None


_,chemins = fonctions.gps(None,None,tmx_data, tmx_data_b, tmx_data_d, tmx_data_c, tmx_data_e, layers_2, layers_3, layers_1, layers_cdi, layers_1B)

#boucle principale
while running:
    #pages d'accueil et d'itinéraire
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
        opt_txt = pygame.font.SysFont(None, 60).render("OPTIONS", True, (0, 0, 0))
        screen.blit(opt_txt, (screen.get_width()//2 - opt_txt.get_width()//2, 475))
    elif etat == "itinéraire":
        screen.fill((255, 255, 255))
        
        # Draw the map tiles         
        for m in range(1):
            for  layer in chemins[etage-1]:
                for x, y, image in layer.tiles():
                    screen.blit(image, (offset_x + x * TILE_SIZE, offset_y + y * TILE_SIZE))
        
        pygame.draw.rect(screen, couleur_bouton_options, (bouton_options_x, bouton_options_y, bouton_options_largeur, bouton_options_hauteur))
        texte_options = font.render("Options", True, (0, 0, 0))
        screen.blit(texte_options, (bouton_options_x + 60, bouton_options_y + 8))
        
        pos_souris = pygame.mouse.get_pos()
        if bouton_options_x <= pos_souris[0] <= bouton_options_x + bouton_options_largeur and bouton_options_y <= pos_souris[1] <= bouton_options_y + bouton_options_hauteur:
            couleur_bouton_options = (180, 180, 180)
        else:
            couleur_bouton_options = (240, 240, 240)

    # Gérer les événements
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
        elif e.type == pygame.MOUSEWHEEL:
            menu_deroulant.offset_y += e.y *20
            menu_deroulant.offset_y = min(-189, menu_deroulant.offset_y)
            menu_deroulant.offset_y = max(-2669, menu_deroulant.offset_y)
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
                print("Salle sélectionnée :", texte_saisi)
                classes.départ_salle = texte_saisi
        elif e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
            mx, my = e.pos

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
                    print("ITINÉRAIRE cliqué: passage à l'itinéraire")
                
    
                # option de puis accueil
                if (screen.get_width()//2 - 200 <= mx <= screen.get_width()//2 + 200 and
                    450 <= my <= 530):
                    options_ouvert = True
                    print("OPTIONS cliqué depuis l'accueil !")
            
            elif etat == "itinéraire":
                menu_deroulant.handle_click(e.pos)
                if saisie_active:
                    menu_matiere.handle_click(e.pos)
                if etage_sup.is_clicked(e.pos):
                    etage = min(etage + 1, 5)
                    son_clic.play()
                    
                if etage_inf.is_clicked(e.pos):
                    etage = max(etage - 1, 1)
                    son_clic.play()
                
                if e.pos[0] >= 1386 and e.pos[0] <= 1426 and e.pos[1] >= 934 and e.pos[1] <= 974:
                    son_clic.play()

                
                # Bouton Options du gps
                if bouton_options_x <= mx <= bouton_options_x + bouton_options_largeur and bouton_options_y <= my <= bouton_options_y + bouton_options_hauteur:
                    options_ouvert = not options_ouvert
                    print("Options du gps cliqué")
                
            if options_ouvert:
                retour_x = screen.get_width()//2 - 80
                retour_y = screen.get_height()//2 + 40

                if bouton_mode_long.is_clicked(e.pos):
                    mode_long = not mode_long
                    son_clic.play()
                    
                if retour_x <= mx <= retour_x + 160 and retour_y <= my <= retour_y + 50:
                    options_ouvert = False
                    son_clic.play()
                    print("Retour cliqué")

    # Affichage de l'itinéraire et du menu déroulant
    if etat == "itinéraire":
        vert=(150,255,150)
        gris=(200,200,200)
        normale=(240,240,240)
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
            #chemins_affichés = list(chemins)
            #del chemins_affichés[2]
        elif batiment_selectionne == "B" and etage in [2, 3]:
            couleur_bouton_options_a = normale
            couleur_bouton_options_b = vert
            #chemins_affichés = list(chemins)
            #del chemins_affichés[1]
        else:
            batiment_selectionne = None
        

        bat_a.draw(screen, text="Bâtiment : A", color=couleur_bouton_options_a,
           top_left=10, top_right=10, bottom_right=10, bottom_left=10)

        bat_b.draw(screen, text="Bâtiment : B", color=couleur_bouton_options_b,
           top_left=10, top_right=10, bottom_right=10, bottom_left=10)
        etage_sup.draw(screen, top_left=5, top_right=5, bottom_right=0, bottom_left=00)
        etage_inf.draw(screen, top_left=0, top_right=0, bottom_right=5, bottom_left=5)
        nom_etage.draw(screen, text=noms_etages[etage], top_left=10, top_right=10, bottom_right=10, bottom_left=10)
        
    #if etage == 2 and batiment_selectionne == "A":
     #   etage=3
    #elif etage == 3 and batiment_selectionne == "B":
     #   etage=2"""


        menu_deroulant.draw(screen, font)
        menu_deroulant.survol(pygame.mouse.get_pos())
        if menu_matiere.action == True:
            infos_cours_result = fonctions.infos_cours(classes.matiere_choisie)
            saisie_active = False
            menu_matiere.action = False
        
        if menu_deroulant.opening==True:
            #chemins = [tmx_data.layers[6]]
            menu_deroulant.opening=False
        if menu_deroulant.action==True:
            infos_cours_result = None
            print("ok")
            #print(gps(depart_salle, arrivée_salle))
            _,chemins = fonctions.gps(classes.départ_salle, classes.arrivée_salle, tmx_data, tmx_data_b, tmx_data_d, tmx_data_c,tmx_data_e, layers_2, layers_3, layers_1, layers_cdi,layers_1B,mode_long)
            fonc=fonctions.fonctionnalitees(classes.départ_salle, classes.arrivée_salle)
            menu_deroulant.action=False
            menu_deroulant.open=False
            saisie_active = True
            texte_saisi = ""
            infos_cours_result = None
        fonctions_ = str("calories : " + fonc['calories']) + "  " +str("temps : " + fonc["temps"]+" min")
        ui_1.draw(screen, top_left=10, top_right=10, bottom_left=0, bottom_right=0, text=fonctions_)
        ui_2.draw(screen, top_left=0, top_right=0, bottom_left=10, bottom_right=10, text=fonctions_)
        if infos_cours_result is not None and not saisie_active:
            texte_ennui = "Ennui : " + infos_cours_result['message_ennui']
            texte_message = infos_cours_result['message']
            screen.blit(font.render(texte_ennui, True, (0, 0, 0)), (50, 150))
            screen.blit(font.render(texte_message, True, (0, 0, 0)), (50, 190)) 
    # Affichage du menu d'options
    if options_ouvert:
        pygame.draw.rect(screen, (80, 80, 80, 180), (0, 0, screen.get_width(), screen.get_height()))
        
        texte = font.render("Menu Options", True, (255, 255, 255))
        screen.blit(texte, (screen.get_width()//2 - 80, screen.get_height()//2 - 50))
           
        retour_x = screen.get_width()//2 - 80
        retour_y = screen.get_height()//2 + 40
        pygame.draw.rect(screen, (220, 220, 220), (retour_x, retour_y, 160, 50))
            
        texte_retour = font.render("Retour", True, (0, 0, 0))
        screen.blit(texte_retour, (retour_x + 40, retour_y + 12))
        bouton_mode_long.draw(screen, top_left=10, top_right=10, bottom_right=10, bottom_left=10, text="Itinéraire le plus long",color=(200, 200, 200))
    
    coodonnées_souris.draw(screen,top_left=10, top_right=10, bottom_right=10, bottom_left=10, text=f"X: {pygame.mouse.get_pos()[0]} Y: {pygame.mouse.get_pos()[1]}")
    
    if saisie_active:
        menu_matiere.draw(screen, font)
        menu_matiere.survol(pygame.mouse.get_pos())

    pygame.display.flip()
pygame.quit()
