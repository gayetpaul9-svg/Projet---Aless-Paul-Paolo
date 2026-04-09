#
# from pydoc import text
import pygame
from pygame.draw import rect 
from pytmx.util_pygame import load_pygame
import classes 
import fonctions
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


# Variables globales
afficher = False
afficher_s = False
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


# Photos des couloirs pour les boutons loupe
show_image = False
current_image = None
images = {
    'civ': pygame.image.load("assets/civ.png").convert(),
    'marque': pygame.image.load("assets/marque.png").convert(),
    'verifier': pygame.image.load("assets/verifier.png").convert(),
}
# map_buttons_info: on associe des coordonnées, un étage et une image à chaque bouton
map_buttons_info = [
    {
        #P1
        'button': classes.Button(offset_x + 180, offset_y + 650, 20, 20),
        'floors': [1],
        'image': 'civ'
    },
    {
        #P2
        'button': classes.Button(offset_x + 220, offset_y + 320, 20, 20),
        'floors': [1],
        'image': 'marque'
    },
    {
        #P3
        'button': classes.Button(offset_x + 370, offset_y + 270, 20, 20),
        'floors': [1],
        'image': 'verifier'
    },
    {
        #P4
        'button': classes.Button(offset_x + 500, offset_y + 145, 20, 20),
        'floors': [2],
        'image': 'civ'
    },
    {
        #P5
        'button': classes.Button(offset_x + 220, offset_y + 405, 20, 20),
        'floors': [2],
        'image': 'marque'
    },
    {
        #P6
        'button': classes.Button(offset_x + 250, offset_y + 665, 20, 20),
        'floors': [2],
        'image': 'verifier'
    },
    {
        #P7
        'button': classes.Button(offset_x + 400, offset_y + 260, 20, 20),
        'floors': [3],
        'image': 'civ'
    },
    {
        #P8
        'button': classes.Button(offset_x + 215, offset_y + 670, 20, 20),
        'floors': [3],
        'image': 'marque'
    },
    {
        #P9
        'button': classes.Button(offset_x + 300, offset_y + 100, 20, 20),
        'floors': [4],
        'image': 'verifier'
    },
    {
        #P10
        'button': classes.Button(offset_x + 170, offset_y + 318, 20, 20),
        'floors': [4],
        'image': 'civ'
    },
    {
        #P11
        'button': classes.Button(offset_x + 330, offset_y + 330, 20, 20),
        'floors': [4],
        'image': 'marque'
    },
    {
        #P12
        'button': classes.Button(offset_x + 370, offset_y + 530, 20, 20),
        'floors': [4],
        'image': 'verifier'
    },
    {
        #P13
        'button': classes.Button(offset_x + 350, offset_y + 690, 20, 20),
        'floors': [4],
        'image': 'marque'
    },
    {
        #P14
        'button': classes.Button(offset_x + 415, offset_y + 750, 20, 20),
        'floors': [4],
        'image': 'verifier'
    },
    {
        #P15
        'button': classes.Button(offset_x + 320, offset_y + 895, 20, 20),
        'floors': [4],
        'image': 'civ'
    },
    {
        #P16
        'button': classes.Button(offset_x + 165, offset_y + 130, 20, 20),
        'floors': [5],
        'image': 'marque'
    },
    {
        #P17
        'button': classes.Button(offset_x + 185, offset_y + 350, 20, 20),
        'floors': [5],
        'image': 'verifier'
    },
    {
        #P18
        'button': classes.Button(offset_x + 70, offset_y + 592, 20, 20),
        'floors': [5],
        'image': 'civ'
    },
    {
        #P19
        'button': classes.Button(offset_x + 300, offset_y + 620, 20, 20),
        'floors': [5],
        'image': 'civ'
    },
    {
        #P20
        'button': classes.Button(offset_x + 345, offset_y + 872, 20, 20),
        'floors': [5],
        'image': 'marque'
    },
]
# boutons_salles: on associe des coordonnée et un étage à chaque bouton
taille_txt = pygame.font.Font("assets/DejaVuSans.ttf", 18)
boutons_salles = [
    {
        'label': 'A001',
        'button': classes.Button(offset_x + 402, offset_y + 272, 60, 20, 'A001', font=taille_txt),
        'floors': [1],
    },
    {
        'label': 'A002',
        'button': classes.Button(offset_x + 430, offset_y + 722, 60, 20, 'A002', font=taille_txt),
        'floors': [1],
    },
    {
        'label': 'A003',
        'button': classes.Button(offset_x + 340, offset_y + 722, 60, 20, 'A003', font=taille_txt),
        'floors': [1],
    },
    {
        'label': 'A004',
        'button': classes.Button(offset_x + 340, offset_y + 802, 60, 20, 'A004', font=taille_txt),
        'floors': [1],
    },
    {
        'label': 'A005',
        'button': classes.Button(offset_x + 255, offset_y + 722, 60, 20, 'A005', font=taille_txt),
        'floors': [1],
    },
    {
        'label': 'A006',
        'button': classes.Button(offset_x + 155, offset_y + 477, 60, 20, 'A006', font=taille_txt),
        'floors': [1],
    },
    {
        'label': 'A007',
        'button': classes.Button(offset_x + 155, offset_y + 432, 60, 20, 'A007', font=taille_txt),
        'floors': [1],
    },
    {
        'label': 'A008',
        'button': classes.Button(offset_x + 155, offset_y + 332, 60, 20, 'A008', font=taille_txt),
        'floors': [1],
    },
    {
        'label': 'A009',
        'button': classes.Button(offset_x + 165, offset_y + 272, 60, 20, 'A009', font=taille_txt),
        'floors': [1],
    },
    {
        'label': 'A010',
        'button': classes.Button(offset_x + 15, offset_y + 287, 60, 20, 'A010', font=taille_txt),
        'floors': [1],
    },
    {
        'label': 'A011',
        'button': classes.Button(offset_x + 4, offset_y + 352, 60, 20, 'A011', font=taille_txt),
        'floors': [1],
    },
    {
        'label': 'A012',
        'button': classes.Button(offset_x + 4, offset_y + 412, 60, 20, 'A012', font=taille_txt),
        'floors': [1],
    },
    {
        'label': 'A013',
        'button': classes.Button(offset_x + 4, offset_y + 477, 60, 20, 'A013', font=taille_txt),
        'floors': [1],
    },
    {
        'label': 'A014',
        'button': classes.Button(offset_x + 20, offset_y + 572, 60, 20, 'A014', font=taille_txt),
        'floors': [1],
    },
    {
        'label': 'B111',
        'button': classes.Button(offset_x + 206, offset_y + 812, 60, 20, 'B111', font=taille_txt),
        'floors': [2],
    },
    {
        'label': 'B112',
        'button': classes.Button(offset_x + 276, offset_y + 717, 60, 20, 'B112', font=taille_txt),
        'floors': [2],
    },
    {
        'label': 'B113',
        'button': classes.Button(offset_x + 315, offset_y + 625, 60, 20, 'B113', font=taille_txt),
        'floors': [2],
    },
    {
        'label': 'B114',
        'button': classes.Button(offset_x + 166, offset_y + 333, 60, 20, 'B114', font=taille_txt),
        'floors': [2],
    },
    {
        'label': 'B115',
        'button': classes.Button(offset_x + 153, offset_y + 192, 60, 20, 'B115', font=taille_txt),
        'floors': [2],
    },
    {
        'label': 'B116',
        'button': classes.Button(offset_x + 300, offset_y + 205, 60, 20, 'B116', font=taille_txt),
        'floors': [2],
    },
    {
        'label': 'B117',
        'button': classes.Button(offset_x + 407, offset_y + 205, 60, 20, 'B117', font=taille_txt),
        'floors': [2],
    },
    {
        'label': 'B118',
        'button': classes.Button(offset_x + 495, offset_y + 205, 60, 20, 'B118', font=taille_txt),
        'floors': [2],
    },
    {
        'label': 'A101',
        'button': classes.Button(offset_x + 429, offset_y + 86, 60, 20, 'A101', font=taille_txt),
        'floors': [3],
    },
    {
        'label': 'A102',
        'button': classes.Button(offset_x + 312, offset_y + 199, 60, 20, 'A102', font=taille_txt),
        'floors': [3],
    },
    {
        'label': 'A103',
        'button': classes.Button(offset_x + 213, offset_y + 199, 60, 20, 'A103', font=taille_txt),
        'floors': [3],
    },
    {
        'label': 'A104',
        'button': classes.Button(offset_x + 117, offset_y + 199, 60, 20, 'A104', font=taille_txt),
        'floors': [3],
    },
    {
        'label': 'A105',
        'button': classes.Button(offset_x + 20, offset_y + 199, 60, 20, 'A105', font=taille_txt),
        'floors': [3],
    },
    {
        'label': 'A106',
        'button': classes.Button(offset_x + 131, offset_y + 607, 60, 20, 'A106', font=taille_txt),
        'floors': [3],
    },
    {
        'label': 'A107',
        'button': classes.Button(offset_x + 28, offset_y + 607, 60, 20, 'A107', font=taille_txt),
        'floors': [3],
    },
    {
        'label': 'A108',
        'button': classes.Button(offset_x + 28, offset_y + 737, 60, 20, 'A108', font=taille_txt),
        'floors': [3],
    },
    {
        'label': 'A109',
        'button': classes.Button(offset_x + 28, offset_y + 808, 60, 20, 'A109', font=taille_txt),
        'floors': [3],
    },
    {
        'label': 'A110',
        'button': classes.Button(offset_x + 28, offset_y + 855, 60, 20, 'A110', font=taille_txt),
        'floors': [3],
    },
    {
        'label': 'A201',
        'button': classes.Button(offset_x + 113, offset_y + 345, 60, 20, 'A201', font=taille_txt),
        'floors': [4],
    },
    {
        'label': 'A202',
        'button': classes.Button(offset_x + 138, offset_y + 302, 60, 20, 'A202', font=taille_txt),
        'floors': [4],
    },
    {
        'label': 'A203',
        'button': classes.Button(offset_x + 180, offset_y + 275, 60, 20, 'A203', font=taille_txt),
        'floors': [4],
    },
    {
        'label': 'A204',
        'button': classes.Button(offset_x + 218, offset_y + 302, 60, 20, 'A204', font=taille_txt),
        'floors': [4],
    },
    {
        'label': 'A205',
        'button': classes.Button(offset_x + 261, offset_y + 246, 60, 20, 'A205', font=taille_txt),
        'floors': [4],
    },
    {
        'label': 'A206',
        'button': classes.Button(offset_x + 261, offset_y + 170, 60, 20, 'A206', font=taille_txt),
        'floors': [4],
    },
    {
        'label': 'A207',
        'button': classes.Button(offset_x + 261, offset_y + 52, 60, 20, 'A207', font=taille_txt),
        'floors': [4],
    },
    {
        'label': 'A208',
        'button': classes.Button(offset_x + 304, offset_y + 368, 60, 20, 'A208', font=taille_txt),
        'floors': [4],
    },
    {
        'label': 'A209',
        'button': classes.Button(offset_x + 304, offset_y + 415, 60, 20, 'A209', font=taille_txt),
        'floors': [4],
    },
    {
        'label': 'A210',
        'button': classes.Button(offset_x + 304, offset_y + 457, 60, 20, 'A210', font=taille_txt),
        'floors': [4],
    },
    {
        'label': 'A211',
        'button': classes.Button(offset_x + 307, offset_y + 506, 60, 20, 'A211', font=taille_txt),
        'floors': [4],
    },
    {
        'label': 'A212',
        'button': classes.Button(offset_x + 394, offset_y + 514, 60, 20, 'A212', font=taille_txt),
        'floors': [4],
    },
    {
        'label': 'B213',
        'button': classes.Button(offset_x + 389, offset_y + 654, 60, 20, 'B213', font=taille_txt),
        'floors': [4],
    },
    {
        'label': 'B214',
        'button': classes.Button(offset_x + 307, offset_y + 647, 60, 20, 'B214', font=taille_txt),
        'floors': [4],
    },
    {
        'label': 'B215',
        'button': classes.Button(offset_x + 254, offset_y + 642, 60, 20, 'B215', font=taille_txt),
        'floors': [4],
    },
    {
        'label': 'B216',
        'button': classes.Button(offset_x + 203, offset_y + 690, 60, 20, 'B216', font=taille_txt),
        'floors': [4],
    },
    {
        'label': 'B217',
        'button': classes.Button(offset_x + 285, offset_y + 731, 60, 20, 'B217', font=taille_txt),
        'floors': [4],
    },
    {
        'label': 'B218',
        'button': classes.Button(offset_x + 352, offset_y + 731, 60, 20, 'B218', font=taille_txt),
        'floors': [4],
    },
    {
        'label': 'B219',
        'button': classes.Button(offset_x + 362, offset_y + 783, 60, 20, 'B219', font=taille_txt),
        'floors': [4],
    },
    {
        'label': 'B220',
        'button': classes.Button(offset_x + 362, offset_y + 826, 60, 20, 'B220', font=taille_txt),
        'floors': [4],
    },
    {
        'label': 'B221',
        'button': classes.Button(offset_x + 362, offset_y + 868, 60, 20, 'B221', font=taille_txt),
        'floors': [4],
    },
    {
        'label': 'B222',
        'button': classes.Button(offset_x + 440, offset_y + 914, 60, 20, 'B222', font=taille_txt),
        'floors': [4],
    },
    {
        'label': 'B223',
        'button': classes.Button(offset_x + 320, offset_y + 914, 60, 20, 'B223', font=taille_txt),
        'floors': [4],
    },
    {
        'label': 'A301',
        'button': classes.Button(offset_x + 33, offset_y + 52, 60, 20, 'A301', font=taille_txt),
        'floors': [5],
    },
    {
        'label': 'A302',
        'button': classes.Button(offset_x + 97, offset_y + 52, 60, 20, 'A302', font=taille_txt),
        'floors': [5],
    },
    {
        'label': 'A303',
        'button': classes.Button(offset_x + 155, offset_y + 52, 60, 20, 'A303', font=taille_txt),
        'floors': [5],
    },
    {
        'label': 'A304',
        'button': classes.Button(offset_x + 98, offset_y + 90, 60, 20, 'A304', font=taille_txt),
        'floors': [5],
    },
    {
        'label': 'A305',
        'button': classes.Button(offset_x + 98, offset_y + 144, 60, 20, 'A305', font=taille_txt),
        'floors': [5],
    },
    {
        'label': 'A306',
        'button': classes.Button(offset_x + 98, offset_y + 204, 60, 20, 'A306', font=taille_txt),
        'floors': [5],
    },
    {
        'label': 'A307',
        'button': classes.Button(offset_x + 98, offset_y + 263, 60, 20, 'A307', font=taille_txt),
        'floors': [5],
    },
    {
        'label': 'A308',
        'button': classes.Button(offset_x + 98, offset_y + 318, 60, 20, 'A308', font=taille_txt),
        'floors': [5],
    },
    {
        'label': 'A309',
        'button': classes.Button(offset_x + 203, offset_y + 158, 60, 20, 'A309', font=taille_txt),
        'floors': [5],
    },
    {
        'label': 'A310',
        'button': classes.Button(offset_x + 203, offset_y + 246, 60, 20, 'A310', font=taille_txt),
        'floors': [5],
    },
    {
        'label': 'B311',
        'button': classes.Button(offset_x + 200, offset_y + 427, 60, 20, 'B311', font=taille_txt),
        'floors': [5],
    },
    {
        'label': 'A312',
        'button': classes.Button(offset_x + 149, offset_y + 530, 60, 20, 'A312', font=taille_txt),
        'floors': [5],
    },
    {
        'label': 'B313',
        'button': classes.Button(offset_x + 20, offset_y + 530, 60, 20, 'B313', font=taille_txt),
        'floors': [5],
    },
    {
        'label': 'B314',
        'button': classes.Button(offset_x + 175, offset_y + 633, 60, 20, 'B314', font=taille_txt),
        'floors': [5],
    },
    {
        'label': 'B315',
        'button': classes.Button(offset_x + 280, offset_y + 705, 60, 20, 'B315', font=taille_txt),
        'floors': [5],
    },
    {
        'label': 'B316',
        'button': classes.Button(offset_x + 280, offset_y + 763, 60, 20, 'B316', font=taille_txt),
        'floors': [5],
    },
    {
        'label': 'B317',
        'button': classes.Button(offset_x + 280, offset_y + 824, 60, 20, 'B317', font=taille_txt),
        'floors': [5],
    },
    {
        'label': 'B318',
        'button': classes.Button(offset_x + 296, offset_y + 889, 60, 20, 'B318', font=taille_txt),
        'floors': [5],
    },
    {
        'label': 'B319',
        'button': classes.Button(offset_x + 369, offset_y + 882, 60, 20, 'B319', font=taille_txt),
        'floors': [5],
    },
    {
        'label': 'B320',
        'button': classes.Button(offset_x + 430, offset_y + 882, 60, 20, 'B320', font=taille_txt),
        'floors': [5],
    },
    {
        'label': 'B321',
        'button': classes.Button(offset_x + 501, offset_y + 882, 60, 20, 'B321', font=taille_txt),
        'floors': [5],
    },
    {
        'label': 'B322',
        'button': classes.Button(offset_x + 493, offset_y + 842, 60, 20, 'B322', font=taille_txt),
        'floors': [5],
    },
    {
        'label': 'B323',
        'button': classes.Button(offset_x + 435, offset_y + 810, 60, 20, 'B323', font=taille_txt),
        'floors': [5],
    },
    {
        'label': 'B324',
        'button': classes.Button(offset_x + 393, offset_y + 842, 60, 20, 'B324', font=taille_txt),
        'floors': [5],
    },
    {
        'label': 'B325',
        'button': classes.Button(offset_x + 359, offset_y + 810, 60, 20, 'B325', font=taille_txt),
        'floors': [5],
    },
]


# Fermer bouton image
close_button = classes.Button(screen.get_width() - 50, 10, 40, 40, "X", font=pygame.font.Font("assets/DejaVuSans.ttf", 20))


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
afficher_loupe = classes.Button(info.current_w-447+200,info.current_h-735, 200, 50)
afficher_salles = classes.Button(info.current_w-447+200,info.current_h-535, 200, 50)
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
                    print("ITINÉRAIRE cliqué: passage à l'itinéraire")
                
    
                # option de puis accueil
                if (screen.get_width()//2 - 200 <= mx <= screen.get_width()//2 + 200 and
                    450 <= my <= 530):
                    options_ouvert = True
                    print("OPTIONS cliqué depuis l'accueil !")
            
            elif etat == "itinéraire":
                menu_deroulant.handle_click(e.pos)
                if menu_deroulant.open:
                    infos_cours_result = None
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

                # Afficher boutons loupe filtrés par étage
                if afficher_loupe.is_clicked(e.pos):
                    afficher = not afficher
                    son_clic.play()

                if afficher_salles.is_clicked(e.pos):
                    afficher_s = not afficher_s
                    son_clic.play()
                
                # Bouton Options du gps
                if bouton_options_x <= mx <= bouton_options_x + bouton_options_largeur and bouton_options_y <= my <= bouton_options_y + bouton_options_hauteur:
                    options_ouvert = not options_ouvert
                    print("Options du gps cliqué")
                
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

            # Fermer l'image si le bouton X est cliqué
            if show_image and close_button.is_clicked(e.pos):
                show_image = False
                son_clic.play()

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
        afficher_loupe.draw(screen, text="Afficher loupes", top_left=10, top_right=10, bottom_right=10, bottom_left=10)
        afficher_salles.draw(screen, text="Afficher salles", top_left=10, top_right=10, bottom_right=10, bottom_left=10)
        if afficher == True:
                        for info_btn in map_buttons_info:
                            btn = info_btn['button']
                            if etage not in info_btn['floors']:
                                continue
                            color = (0, 255, 0) if btn.clicked else (255, 0, 0)
                            btn.draw(screen, top_left=0, top_right=0, bottom_right=0, bottom_left=0, color=color)
        if afficher_s == True:
                        for info_btn in boutons_salles:
                            btn = info_btn['button']
                            if etage not in info_btn['floors']:
                                continue
                            color = (200, 200, 200)
                            btn.draw(screen, top_left=5, top_right=5, bottom_right=5, bottom_left=5, color=color)
        
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
            infos_cours_result = None
        if menu_deroulant.action==True:
            infos_cours_result = None
            print("ok")

            for cle, v in dico_etage.items():
                if v == layer:
                    etage = cle
                    break
            menu_deroulant.action=False
            menu_deroulant.open=False
            saisie_active = True
            texte_saisi = ""
            infos_cours_result = None
        fonctions_ = str("calories : " + fonc['calories']+" Kcal")
        ui_1.draw(screen, top_left=10, top_right=10, bottom_left=0, bottom_right=0, text=fonctions_)
        fonctions_= "  " +str("temps : " + fonc["temps"]+" s")
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

    # Afficher image si bouton loupe cliqué
    if show_image:
        max_w, max_h = 500, 400
        img_w, img_h = current_image.get_size()
        scale = min(max_w / img_w, max_h / img_h, 1)
        new_w = int(img_w * scale)
        new_h = int(img_h * scale)

        scaled_image = pygame.transform.smoothscale(current_image, (new_w, new_h))
        screen_rect = screen.get_rect()
        img_rect = scaled_image.get_rect(center=screen_rect.center)

        overlay = pygame.Surface(screen.get_size(), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 120))
        screen.blit(overlay, (0, 0))

        pygame.draw.rect(screen, (255, 255, 255), img_rect.inflate(10, 10), 3)
        screen.blit(scaled_image, img_rect)

        close_button.draw(screen, top_left=5, top_right=5, bottom_right=5, bottom_left=5, color=(200, 200, 200))

    pygame.display.flip()
pygame.quit()
