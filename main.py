import pygame 
running = True
pygame.init()

# Crée une fenêtre en plein écran
screen = pygame.display.set_mode()
clock = pygame.time.Clock()
# Définir la police et le texte à afficher
font = pygame.font.SysFont(None, 36)
texte = font.render("bienvenue dans le version test de cette application", True, (0, 0, 0)) 


texte_rect = texte.get_rect()
texte_rect.center = ((1000, 500))
while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
    
    screen.fill((255, 255, 255))
    screen.blit(texte, texte_rect)
    pygame.display.flip()
    clock.tick(60)