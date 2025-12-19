from pydoc import text
import pygame 
running = True
pygame.init()

# Crée une fenêtre en plein écran
screen = pygame.display.set_mode()
clock = pygame.time.Clock()
# Définir la police et le texte à afficher
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
    def __init__(self, x, y, width, height, text):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = (240, 240, 240)
        self.rounded = 0
    
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
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
        self.main.draw(screen)
        if self.open:
            for option in self.options:
                option.draw(screen)

    def handle_click(self, pos):
        if self.main.is_clicked(pos):
            self.open = not self.open
        elif self.open:
            for opt in self.options:
                if opt.is_clicked(pos):
                    if self.type == "start":
                        opt.color = (150, 255, 150)
                        self.type = "stop"
                    elif self.type == "stop":
                        opt.color = (255, 150, 150)
                        self.type = None
                    #self.open = False
        
menu_deroulant= Dropdown(50, 50, 250, 40, ["A200","A201","A202","A203","A204","A205","A206","A207","A208","A209"])

while running:
    screen.fill((255, 255, 255))
    menu_deroulant.draw(screen, font)
        
    # Gérer les événements
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
        elif e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
            menu_deroulant.handle_click(e.pos)
        
    pygame.display.flip()
    clock.tick(60)   
pygame.quit()
    
