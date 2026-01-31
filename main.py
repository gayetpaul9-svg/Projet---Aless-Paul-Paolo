#
# from pydoc import text
import math
import algo
import pygame 
from pytmx.util_pygame import load_pygame
running = True
options_ouvert = False
pygame.init()
pygame.mixer.init()

etat = "accueil"
pygame.mixer.music.load("sons_fond.mp3")
pygame.mixer.music.set_volume(1)
pygame.mixer.music.play(-1)
son_clic = pygame.mixer.Sound("effet_sonore.mp3")


# Crée une fenêtre en plein écran
screen = pygame.display.set_mode()

fond_image = pygame.image.load("civ.png").convert()
fond_image = pygame.transform.scale(fond_image, screen.get_size())

tmx_data = load_pygame("map B300 x4..tmx")
#tmx_data_b = load_pygame("map B200-A200 x4.tmx")
TILE_SIZE = tmx_data.tileheight
chemins = [tmx_data.layers[6]]
layers =  {
    "sol": tmx_data.layers[0],
    "COULOIR_A": tmx_data.layers[1],
    "COULOIR_B": tmx_data.layers[2],
    "COULOIR_C": tmx_data.layers[3],
    "COULOIR_D": tmx_data.layers[4],
    "COULOIR_E": tmx_data.layers[5],
    "murs_": tmx_data.layers[6],
    
}
#print(layers["sol"])

map_width = tmx_data.width * TILE_SIZE
map_height = tmx_data.height * TILE_SIZE
offset_x = (screen.get_width() - map_width) // 2
offset_y = (screen.get_height() - map_height) // 2
#resultat = tmx_data.layers

# Définir la police et le texte à afficherSSS
font = pygame.font.SysFont(None, 36)
#menu déroulant
menu_ouvert = False
menu_deroulant = pygame.Rect(50, 50, 200, 40)

départ_salle = None
arrivée_salle = None



icone = pygame.image.load("verifier.png").convert_alpha()
icone = pygame.transform.scale(icone, (50, 50))

class Button:
    def __init__(self, x, y, width, height, text,):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = (240, 240, 240)
        self.is_clickedv=False

    def draw(self, screen, top_left, top_right, bottom_right, bottom_left):
        pygame.draw.rect(
            screen, self.color, self.rect, border_radius=0,
            border_top_left_radius=top_left,
            border_top_right_radius=top_right,
            border_bottom_left_radius=bottom_left,
            border_bottom_right_radius=bottom_right
            )
        
        font = pygame.font.SysFont(None, 36)
        text_surf = font.render(self.text, True, (0, 0, 0))
        text_rect = text_surf.get_rect(center=self.rect.center)
        screen.blit(text_surf, text_rect)
    
    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)



class Dropdown:
    def __init__(self, x, y, width, height, options, Validation=False):
        self.main=Button(x, y, width, height, "salles disponibles")
        self.open = False
        self.options = []
        self.type = "start"
        self.action=False
        self.opening=False
        self.offset_y=-189
        self.index_y=7
        

        for i, opt in enumerate(options):
            if Validation==False:
                self.options.append(
                    Button(x, y + (i + 1) * height, width, height, opt)
                )
            else:
                self.options.append(
                    Button(x, y + (i + 1) * height, width, height, opt)
                )
        self.options_affichées = list(self.options[0:8])
        self.options_affichées.append(self.options[-1])  

    def scroll_options(self):
        self.index_y=7 + ( (-189 - self.offset_y) / 40 )
        #print(self.index_y,self.offset_y)
        if self.index_y % 1 == 0.5 or self.index_y==39.0:
            self.index_y = math.floor(self.index_y)
            self.index_y= max(7, min(self.index_y, len(self.options)-7))  
            self.options_affichées = list(self.options[self.index_y-7:self.index_y+2]+[self.options[-1]])
        else:  
            print(self.index_y,self.offset_y)
            self.index_y = math.floor(self.index_y)
        #self.index_y= min(self.index_y, self.index_y-0.5)
        #self.index_y= int(self.index_y)
            self.index_y= max(7, min(self.index_y, len(self.options)-7))
            self.options_affichées = list(self.options[self.index_y-7:self.index_y+1]+[self.options[-1]])
        
    
    def draw(self, screen, font):
        global icone
        if self.open:
            #self.main.draw(screen, top_left=10, top_right=10, bottom_right=0, bottom_left=0)
            for i, option in enumerate(self.options_affichées):
                if i == len(self.options_affichées) - 1:
                    option.rect.y = y + (8+1) * self.main.rect.height - 189
                    icone_rect = icone.get_rect(center=option.rect.center)
                    option.draw(screen, top_left=0, top_right=0, bottom_right=10, bottom_left=10)
                    screen.blit(icone, icone_rect)

                else:
                    option.rect.y = y + (i + 1) * self.main.rect.height + self.offset_y +(self.index_y-7)*self.main.rect.height
                    option.draw(screen, top_left=0, top_right=0, bottom_right=0, bottom_left=0)

            self.main.draw(screen, top_left=10, top_right=10, bottom_right=0, bottom_left=0)
        else:
            self.main.draw(screen, top_left=10, top_right=10, bottom_right=10, bottom_left=10)

    def survol(self, pos):
        if self.main.is_clicked(pos):
            self.main.color = (200, 200, 200)
            #return True
        elif self.open:
            for opt in self.options_affichées:
                if opt.is_clicked(pos) and not opt.is_clickedv:
                    opt.color = (200, 200, 200)
                elif not opt.is_clickedv:
                    opt.color = (240, 240, 240)
        else:
            self.main.color = (240, 240, 240)
        
        #return False

    def reset_colors(self):
        """Réinitialise les couleurs et états des options"""
        for opt in self.options_affichées:
            opt.is_clickedv = False
            opt.color = (240, 240, 240)
        self.type = "start"

    def handle_click(self, pos):
        global depart_salle
        global arrivée_salle
        if self.main.is_clicked(pos):
            self.open = not self.open
            self.opening=True
            # Réinitialiser quand on ferme le menu
            if not self.open:
                self.reset_colors()
        elif self.open:
            for opt in self.options_affichées:
                if opt.is_clicked(pos) and opt.text != "":
                    if self.type == "start":
                        opt.color = (150, 255, 150)
                        depart_salle = opt.text
                        self.type = "stop"
                        opt.is_clickedv = not opt.is_clickedv
                    elif self.type == "stop":
                        opt.color = (255, 150, 150)
                        arrivée_salle = opt.text
                        self.type = "None"
                        opt.is_clickedv = not opt.is_clickedv
                    elif self.type == "None":
                        self.type = None
                if self.type == None or self.open==False:
                    for opt in self.options:
                        opt.is_clickedv = False
                        opt.color = (240, 240, 240)
                    self.type = "start"
                if opt.is_clicked(pos) and opt.text == "":
                    self.action = True
                    self.open = False
                    self.reset_colors()

                    #self.open = False
        
menu_deroulant= Dropdown(50, 50, 250, 40, [
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

#resultat_chemin = None
#resultat_distance = None

def gps(depart, arrivee):
    resultat = algo.dijkstra(depart, arrivee)
    print("Chemin trouvé :", resultat)
    for i in resultat:
        chemins.append(layers[i])
    return resultat

clock = pygame.time.Clock()

while running:
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
        for layer in chemins:
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

    if etat == "itinéraire":
        menu_deroulant.draw(screen, font)
        menu_deroulant.survol(pygame.mouse.get_pos())
        
        if menu_deroulant.opening==True:
            chemins = [tmx_data.layers[6]]
            menu_deroulant.opening=False
        if menu_deroulant.action==True:
            print("ok")
            #print(gps(depart_salle, arrivée_salle))
            a=gps(depart_salle, arrivée_salle)
            menu_deroulant.action=False
            menu_deroulant.open=False
            
    if options_ouvert:
        pygame.draw.rect(screen, (80, 80, 80, 180), (0, 0, screen.get_width(), screen.get_height()))
        
        texte = font.render("Menu Options", True, (255, 255, 255))
        screen.blit(texte, (screen.get_width()//2 - 80, screen.get_height()//2 - 50))
           
        retour_x = screen.get_width()//2 - 80
        retour_y = screen.get_height()//2 + 40
        pygame.draw.rect(screen, (220, 220, 220), (retour_x, retour_y, 160, 50))
            
        texte_retour = font.render("Retour", True, (0, 0, 0))
        screen.blit(texte_retour, (retour_x + 40, retour_y + 12))
    
    pygame.display.flip()
    clock.tick(60) 
pygame.quit()
