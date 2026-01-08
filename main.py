from pydoc import text
import pygame 
running = True
pygame.init()
colore=(255, 255, 255)
coloree=True
# Crée une fenêtre en plein écran
screen = pygame.display.set_mode()
clock = pygame.time.Clock()
# Définir la police et le texte à afficherSSS
font = pygame.font.SysFont(None, 36)
texte = font.render("bienvenue dans le version test de cette application", True, (0, 0, 0)) 
#menu déroulant
menu_ouvert = False
menu_deroulant = pygame.Rect(50, 50, 200, 40)
#options = ["A200","A201","A202","A203","A204","A205","A206","A207","A208","A209"]
#option_rects = [pygame.Rect(50, 90 + i*40, 120, 40) for i in range(len(options))]

color = (100, 100, 100)
texte_rect = texte.get_rect()
texte_rect.center = ((1000, 500))

class Button:
    def __init__(self, x, y, width, height, text,):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = (240, 240, 240)

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
    def __init__(self, x, y, width, height, options):
        self.main=Button(x, y, width, height, "salles disponibles")
        self.open = False
        self.options = []
        self.type = "start"

        for i, opt in enumerate(options):
            self.options.append(
                Button(x, y + (i + 1) * height, width, height, opt)
                )
    def draw(self, screen, font):
        self.main.draw(screen, top_left=10, top_right=10, bottom_right=10, bottom_left=10)
        if self.open:
            self.main.draw(screen, top_left=10, top_right=10, bottom_right=0, bottom_left=0)
            for i, option in enumerate(self.options):
                if i == len(self.options) - 1:
                    option.draw(screen, top_left=0, top_right=0, bottom_right=10, bottom_left=10)
                else:
                    option.draw(screen, top_left=0, top_right=0, bottom_right=0, bottom_left=0)

    def handle_click(self, pos):
        global coloree
        if self.main.is_clicked(pos):
            self.open = not self.open
        elif self.open:
            for opt in self.options:
                if opt.is_clicked(pos):
                    coloree= not coloree
                    if self.type == "start":
                        opt.color = (150, 255, 150)
                        self.type = "stop"
                    elif self.type == "stop":
                        opt.color = (255, 150, 150)
                        self.type = "None"
                    elif self.type == "None":
                        self.type = None
                if self.type == None:
                    for opt in self.options:
                        opt.color = (240, 240, 240)
                    self.type = "start"

                    #self.open = False
        
menu_deroulant= Dropdown(50, 50, 250, 40, ["A200","A201","A202","A203","A204","A205","A206","A207","A208","A209"])

while running:
    screen.fill(colore)
    menu_deroulant.draw(screen, font)
        
    # Gérer les événements
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
        elif e.type == pygame.KEYDOWN:
            if e.key == pygame.K_ESCAPE:       
                running = False
        elif e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
            menu_deroulant.handle_click(e.pos)


    if coloree == True:
        colore=(255, 255, 255)
    else:
        colore=(0,0,0) 
    pygame.display.flip()
    clock.tick(60)   
pygame.quit()
