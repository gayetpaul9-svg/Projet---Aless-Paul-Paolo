import pygame
import math
pygame.init()
départ_salle = ""
arrivée_salle = ""
matiere_choisie = ""
screen = pygame.display.set_mode()

icone = pygame.image.load("assets/verifier.png").convert_alpha()
icone = pygame.transform.scale(icone, (50, 50))

class Button:
    def __init__(self, x, y, width, height, text=None,font =None):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = (240, 240, 240)
        self.is_clickedv=False
        if font is None:
            self.font = pygame.font.SysFont(None, 36)
        else:
            self.font=font
    def draw(self, screen, top_left, top_right, bottom_right, bottom_left, text=None,font=None, color=None):
        if text is not None:
            self.text = text
        if font is not None:
            self.font=font
        if color is not None:
            self.color = color
        pygame.draw.rect(
            screen, self.color, self.rect, border_radius=0,
            border_top_left_radius=top_left,
            border_top_right_radius=top_right,
            border_bottom_left_radius=bottom_left,
            border_bottom_right_radius=bottom_right
            )
        
        #font = pygame.font.SysFont(None, 36)
        text_surf = self.font.render(self.text, True, (0, 0, 0))
        text_rect = text_surf.get_rect(center=self.rect.center)
        screen.blit(text_surf, text_rect)
        
    
        
    
    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)


class Dropdown:
    """Menu déroulant de sélection avec défilement pour les salles et matières."""

    def __init__(self, x, y, width, height, options, Validation=False, titre="salles disponibles", single=False, sous_options=None):
        """Initialise un Dropdown.

        options: liste de libellés à afficher.
        Validation: booléen de mode validation (à usage spécifique du projet).
        single: si True, sélection unique puis fermeture automatique.
        """
    
        self.single = single
        self.main=Button(x, y, width, height, titre)
        self.open = False
        self.options = []
        self.type = "start"
        self.action=False
        self.opening=False
        self.offset_y=-189
        self.index_y=7
        self.y = y
        self.sous_menu_ouvert = None
        self.sous_menus = {}
        if sous_options is not None:
            for option in options:
                if option == "":
                    continue
                salles = sous_options[option]
                self.sous_menus[option] = Dropdown(x, y, width, height, salles)
        print(len(options)-1)
        

        for i, opt in enumerate(options):
            if Validation==False:
                self.options.append(
                    Button(x, self.y + (i + 1) * height, width, height, opt)
                )
            else:
                self.options.append(
                    Button(x, self.y + (i + 1) * height, width, height, opt)
                )
        self.options_affichées = list(self.options[0:8])
        self.options_affichées.append(self.options[-1])  
        print(self.options[70-7:70+1])

    def scroll_options(self):
        self.index_y=7 + ( (-189 - self.offset_y) / 40 )
        if self.index_y % 1 == 0.5 or self.index_y==len(self.options)-1:
            self.index_y = math.floor(self.index_y)
            self.index_y= max(7, min(self.index_y, len(self.options)-2))  
            self.options_affichées = list(self.options[self.index_y-7:self.index_y+2]+[self.options[-1]])
        else:  
            self.index_y = math.floor(self.index_y)
            self.index_y= max(7, min(self.index_y, len(self.options)-2))
            self.options_affichées = list(self.options[self.index_y-7:self.index_y+1]+[self.options[-1]])
        
    
    def draw(self, screen,  font):
        global icone
        if self.open:
            #self.main.draw(screen, top_left=10, top_right=10, bottom_right=0, bottom_left=0)
            for i, option in enumerate(self.options_affichées):
                if i == len(self.options_affichées) - 1:
                    option.rect.y = self.y + (8+1) * self.main.rect.height #- 189
                    icone_rect = icone.get_rect(center=option.rect.center)
                    option.draw(screen, top_left=0, top_right=0, bottom_right=10, bottom_left=10)
                    screen.blit(icone, icone_rect)

                else:
                    option.rect.y = self.y + (i + 1) * self.main.rect.height + self.offset_y +(self.index_y-7)*self.main.rect.height+189
                    option.draw(screen, top_left=0, top_right=0, bottom_right=0, bottom_left=0)

            self.main.draw(screen, top_left=10, top_right=10, bottom_right=0, bottom_left=0)
        else:
            self.main.draw(screen, top_left=10, top_right=10, bottom_right=10, bottom_left=10)
        if self.sous_menu_ouvert is not None:
            self.sous_menus[self.sous_menu_ouvert].draw(screen, font)

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
        global départ_salle
        global arrivée_salle
        global matiere_choisie
        if self.main.is_clicked(pos):
            self.open = not self.open
            # Réinitialiser quand on ferme le menu
            if not self.open:
                self.reset_colors()
        elif self.open:
            for opt in self.options_affichées:
                if opt.is_clicked(pos) and opt.text == "":
                    self.action = True
                    #print(self.action)
                    self.open = False
                    self.reset_colors()
                    return
                if opt.is_clicked(pos) and opt.text == "Retour":
                    self.open = False
                    self.reset_colors()
                    self.action = False
                    if départ_salle != "":
                        self.type = "stop"
                    return
                if opt.is_clicked(pos) and opt.text != "":
                    if self.sous_menus:
                        self.sous_menus[opt.text].open = True
                        self.sous_menu_ouvert = opt.text
                        self.open = False
                        if opt.text == "":
                            return
                    elif self.type == "start":
                        opt.color = (150, 255, 150)
                        départ_salle = opt.text
                        matiere_choisie = opt.text
                        opt.is_clickedv = not opt.is_clickedv
                        if self.single:
                            self.action = True
                            self.open = False
                            self.reset_colors()
                            return
                        self.type = "stop"
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
