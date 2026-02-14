#
# from pydoc import text
import pygame 
from pytmx.util_pygame import load_pygame
import classes 
import fonctions




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

# Variables globales
etat = "accueil"
running = True
options_ouvert = False
fonc={
    'calories' : "0",
    'temps' : "0"
}
etage = 4
chemins1 = []
chemins_cdi = []
chemins2 = []
chemins3 = []
chemins = [chemins1, chemins2, chemins3]

#importation des données de la carte
tmx_data = load_pygame("maps/map B300 x4.tmx")
tmx_data_b = load_pygame("maps/map B200-A200 x4.tmx")
tmx_data_c = load_pygame("maps/map CDI.tmx")
tmx_data_d = load_pygame("maps/map A100.tmx")
TILE_SIZE = tmx_data.tileheight
layers_3 =  {
    "sol3": tmx_data.layers[0],
    "COULOIR_A": tmx_data.layers[1],
    "COULOIR_B": tmx_data.layers[2],
    "COULOIR_N": tmx_data.layers[3],
    "COULOIR_C": tmx_data.layers[4],
    "COULOIR_D": tmx_data.layers[5],
    "COULOIR_E": tmx_data.layers[6],
    "ESCALIER_1": tmx_data.layers[7],
    "ESCALIER_2": tmx_data.layers[8],
    "ESCALIER_3": tmx_data.layers[9],
    "ESCALIER_4": tmx_data.layers[10],
    "ESCALIER_8": tmx_data.layers[11],
    "murs3": tmx_data.layers[12],
}
layers_2 = {
    "sol2": tmx_data_b.layers[0],
    "ESCALIER_1": tmx_data_b.layers[1],
    "ESCALIER_2": tmx_data_b.layers[2],
    "ESCALIER_3": tmx_data_b.layers[3],
    "ESCALIER_4": tmx_data_b.layers[4],
    "ESCALIER_5": tmx_data_b.layers[5],
    "ESCALIER_6": tmx_data_b.layers[6],
    "COULOIR_F": tmx_data_b.layers[7],
    "COULOIR_G": tmx_data_b.layers[8],
    "COULOIR_H": tmx_data_b.layers[9],
    "COULOIR_I": tmx_data_b.layers[10],
    "COULOIR_J": tmx_data_b.layers[11],
    "COULOIR_K": tmx_data_b.layers[12],
    "COULOIR_L": tmx_data_b.layers[13],
    "COULOIR_M": tmx_data_b.layers[14],
    "murs2": tmx_data_b.layers[15],
    
}
layers_1 = {
    "sol1": tmx_data_b.layers[0],
    "COULOIR_O": tmx_data_d.layers[1],
    "COULOIR_P": tmx_data_d.layers[2],
    "COULOIR_Q": tmx_data_d.layers[3],
    "COULOIR_R": tmx_data_d.layers[4],
    "ESCALIER_6": tmx_data_d.layers[5],
    "ESCALIER_7": tmx_data_d.layers[6],
    "ESCALIER_9": tmx_data_d.layers[7],
    "murs1": tmx_data_d.layers[8],
}
layers_cdi = {
    "sol_cdi": tmx_data_c.layers[0],
    "COULOIR_S": tmx_data_c.layers[1],
    "COULOIR_T": tmx_data_c.layers[2],
    "COULOIR_U": tmx_data_c.layers[3],
    "COULOIR_V": tmx_data_c.layers[4],
    "COULOIR_W": tmx_data_c.layers[5],
    "COULOIR_X": tmx_data_c.layers[6],
    "ESCALIER_6": tmx_data_c.layers[7],
    "ESCALIER_9": tmx_data_c.layers[8],
    "murs_cdi": tmx_data_c.layers[9],}
map_width = tmx_data.width * TILE_SIZE
map_height = tmx_data.height * TILE_SIZE
offset_x = (screen.get_width() - map_width) // 2
offset_y = (screen.get_height() - map_height) // 2


#bouttons
menu_ouvert = False
coodonnées_souris=classes.Button(10,10,200,40,)
etage_sup=classes.Button(1386, 934, 40, 40, "↑",font=pygame.font.Font("assets/DejaVuSans.ttf", 15))
etage_inf=classes.Button(1386, 934+40, 40, 40, "↓",font=pygame.font.Font("assets/DejaVuSans.ttf", 15))
ui=classes.Button(1529,236, 340, 200,text="",font=pygame.font.Font("assets/DejaVuSans.ttf", 15))
menu_deroulant= classes.Dropdown(50, 50, 250, 40, [
    "A301","A302","A303","A304","A305","A306","A307","A308",

    "A201","A202","A203","A204","A205","A206","A207","A208","A209","A210","A211",

    "B214","B215","B216","B217","B218","B219","B220","B221","B222","B223",

    "B311","B312","B313","B314","B315","B316","B317","B318","B319","B320",
    "B321","B322","B323","B324","B325",""
])
bouton_options_x = screen.get_width() - 250
bouton_options_y = 50
bouton_options_largeur = 200
bouton_options_hauteur = 40
couleur_bouton_options = (240, 240, 240)


_,chemins = fonctions.gps(None,None,tmx_data, tmx_data_b, tmx_data_d, tmx_data_c, layers_2, layers_3, layers_1, layers_cdi)

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
            menu_deroulant.offset_y = max(-1469, menu_deroulant.offset_y)
            menu_deroulant.scroll_options()
        elif e.type == pygame.KEYDOWN:
            if e.key == pygame.K_ESCAPE:       
                if etat == "itinéraire":
                    etat = "accueil"
                else:
                    running = False
        elif e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
            mx, my = e.pos
    
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
                if etage_sup.is_clicked(e.pos):
                    etage = min(etage + 1, 4)
                    son_clic.play()
                    
                if etage_inf.is_clicked(e.pos):
                    etage = max(etage - 1, 1)
                    son_clic.play()
                
                
                # Bouton Options du gps
                if bouton_options_x <= mx <= bouton_options_x + bouton_options_largeur and bouton_options_y <= my <= bouton_options_y + bouton_options_hauteur:
                    options_ouvert = not options_ouvert
                    print("Options du gps cliqué")
                
            if options_ouvert:
                retour_x = screen.get_width()//2 - 80
                retour_y = screen.get_height()//2 + 40
                    
                if retour_x <= mx <= retour_x + 160 and retour_y <= my <= retour_y + 50:
                    options_ouvert = False
                    son_clic.play()
                    print("Retour cliqué")
    
    # Affichage de l'itinéraire et du menu déroulant
    if etat == "itinéraire":
        
        etage_sup.draw(screen, top_left=5, top_right=5, bottom_right=0, bottom_left=00)
        etage_inf.draw(screen, top_left=0, top_right=0, bottom_right=5, bottom_left=5)
        
        menu_deroulant.draw(screen, font)
        menu_deroulant.survol(pygame.mouse.get_pos())
        
        if menu_deroulant.opening==True:
            #chemins = [tmx_data.layers[6]]
            menu_deroulant.opening=False
        if menu_deroulant.action==True:
            print("ok")
            #print(gps(depart_salle, arrivée_salle))
            _,chemins = fonctions.gps(classes.départ_salle, classes.arrivée_salle, tmx_data, tmx_data_b, tmx_data_d, tmx_data_c, layers_2, layers_3, layers_1, layers_cdi)
            fonc=fonctions.fonctionnalitees(classes.départ_salle, classes.arrivée_salle)
            menu_deroulant.action=False
            menu_deroulant.open=False
        fonctions_ = str("calories : " + fonc['calories']) + "  " +str("temps : " + fonc["temps"]+" min")
        ui.draw(screen, top_left=10, top_right=10, bottom_left=10, bottom_right=10, text=fonctions_)
    
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
    
    coodonnées_souris.draw(screen,top_left=10, top_right=10, bottom_right=10, bottom_left=10, text=f"X: {pygame.mouse.get_pos()[0]} Y: {pygame.mouse.get_pos()[1]}")
    
    pygame.display.flip()
pygame.quit()
