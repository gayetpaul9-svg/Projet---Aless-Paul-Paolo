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
options = ["A200","A201","A202","A203","A204","A205","A206","A207","A208","A209"]
#option_rects = [pygame.Rect(50, 90 + i*40, 120, 40) for i in range(len(options))]

color = (100, 100, 100)
texte_rect = texte.get_rect()
texte_rect.center = ((1000, 500))

class Button:
    def __init__(self, x, y, width, height, text):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = (200, 200, 200)
    
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        font = pygame.font.SysFont(None, 36)
        text_surf = font.render(self.text, True, (0, 0, 0))
        text_rect = text_surf.get_rect(center=self.rect.center)
        screen.blit(text_surf, text_rect)

class Option(Button):
    def __init__(self, x, y, width, height, text):
        super().__init__(x, y, width, height, text)
        self.color = (0, 255, 0)
        self.selected = False
        self.position = 0
        
class main_button(Button):
    def __init__(self, x, y, width, height, text):
        super().__init__(x, y, width, height, text)
        self.color = (255, 0, 0)
    
while running:
    screen.fill((255, 255, 255))
    #menu_text = font.render("Sélectionner une option", True, (255, 255, 255))
    #screen.blit(menu_text, (menu_deroulant.x + 10, menu_deroulant.y + 5))
    
    
    
    # Gérer les événements
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
        elif e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
            if menu_deroulant.collidepoint(e.pos):
                menu_ouvert = not menu_ouvert
        

    if menu_ouvert:
        option_rects = [pygame.Rect(50, 90 + i*40, 200, 40) for i in range(len(options))]
        for rect in option_rects:
            pygame.draw.rect(screen, (150, 150, 150), rect)
        for i, option in enumerate(options):

            option_text = font.render(option, True, (0, 0, 0))
            screen.blit(option_text, (60, 100 + i*40))
            if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
                if pygame.Rect(50, 90 + i*40, 200, 40).collidepoint(e.pos):
                    print(f"Option sélectionnée : {option}")
                    
        #pygame.draw.rect(screen, (200, 200, 200), (50, 50, 200, 90*len(options)))        
    pygame.draw.rect(screen, color, (50, 50, 200, 40), border_top_left_radius=15, border_top_right_radius=15)
    screen.blit(texte, texte_rect)
    pygame.display.flip()
    clock.tick(60)