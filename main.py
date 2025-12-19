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
menu_deroulant = pygame.Rect(50, 50, 200, 30)
options = ["A200","A201","A202","A203","A204","A205","A206","A207","A208","A209"]
option_rects = [pygame.Rect(50, 90 + i*40, 120, 40) for i in range(len(options))]


texte_rect = texte.get_rect()
texte_rect.center = ((1000, 500))
while running:
    pygame.draw.rect(screen, (100, 100, 100), menu_deroulant)
    menu_text = font.render("Sélectionner une option", True, (255, 255, 255))
    screen.blit(menu_text, (menu_deroulant.x + 5, menu_deroulant.y + 5))
    
    
    if menu_ouvert:
        pygame.draw.rect(screen, (200, 200, 200), menu_deroulant)
        for i, option_rect in enumerate(option_rects):
            pygame.draw.rect(screen, (150, 150, 150), option_rect)
            option_text = font.render(options[i], True, (0, 0, 0))
            screen.blit(option_text, (option_rect.x + 5, option_rect.y + 5))
    
    # Gérer les événements
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
        elif e.type == pygame.MOUSEBUTTONDOWN:
            if menu_deroulant.collidepoint(e.pos):
                menu_ouvert = not menu_ouvert
            elif menu_ouvert:
                for i, option_rect in enumerate(option_rects):
                    if option_rect.collidepoint(e.pos):
                        print(f"Option sélectionnée: {options[i]}")
                        menu_ouvert = False
                        break
                else:
                    menu_ouvert = False
    screen.fill((255, 255, 255))
    screen.blit(texte, texte_rect,)
    pygame.display.flip()
    clock.tick(60)