"""
Fonctions utilitaires du GPS du lycée.
Contient:
- calculs de chemin (gps), dijkstra par algo module.
- métriques ennui et messages pédagogiques.
- modes long, calories, temps.
"""

import algo
from algo import graphe
from layers import *
import random
from data_cours import ennui_par_cours, messages_par_cours
import unicodedata
liste_etage = []
# =========================
# SELECTION ETAPE INTERMEDIAIRE LOINTAINE
# =========================
def trouver_nombre_eloigne(debut, fin):
    """Retourne un étage éloigné de l'intervalle [debut, fin] parmi 1..5.

    Utilisé par le mode long pour choisir une étape intermédiaire.
    """
    # Création de la liste de nombres de 1 à 5
    nombres = [1, 2, 3, 4, 5]
    
    # Créer le chemin entre début et fin
    chemin = list(range(min(debut, fin), max(debut, fin) + 1))
    
    # Exclure les nombres du chemin
    autres_nombres = [n for n in nombres if n not in chemin]
    
    # Trouver les nombres les plus éloignés
    distance_max = -1
    nombre_eloigne = None
    
    for n in autres_nombres:
        # Calculer la distance à l'un des bords du chemin
        distance = min(abs(debut - n), abs(fin - n))
        
        if distance > distance_max:
            distance_max = distance
            nombre_eloigne = n
            
    return nombre_eloigne



# =========================
# FONCTION GPS
# =========================

def gps(depart, arrivee, tmx_data, tmx_data_b, tmx_data_d, tmx_data_c, tmx_data_e, layers_2, layers_3, layers_1, layers_cdi, layers_1B, long=False):
    """Calcule l'itinéraire entre départ et arrivée.

    Args:
        depart (str): identifiant de la salle de départ.
        arrivee (str): identifiant de la salle d'arrivée.
        tmx_data...: données de carte pour chaque niveau.
        layers_* : couches de cartes par étage.
        long (bool): mode itinéraire le plus long via étape intermédiaire.

    Retourne:
        tuple(resultat, chemins)
    """

    chemins1 = []
    chemins_cdi = []
    chemins2 = []
    chemins3 = []
    chemins1B = []


    if not depart or not arrivee:
        chemins1.append(tmx_data_d.layers[8])
        chemins_cdi.append(tmx_data_c.layers[9])
        chemins3.append(tmx_data.layers[12])
        chemins2.append(tmx_data_b.layers[17])
        chemins1B.append(tmx_data_e.layers[10])
        chemins = [chemins_cdi,chemins1B, chemins1, chemins2, chemins3]        
        return None, chemins
    if long == False:
        resultat, _ = algo.dijkstra(depart, arrivee)
    else:
        #recherche etage depart
        for layer in layers:
            for cle in layer.keys():
                 if cle == arrivee:
                    b=layer
        for layer in layers:
            for cle in layer.keys():
                if cle == depart:
                    a=layer
        for cle, val in dico_etage.items():
            if val == b:
                b=cle
            if val == a:
                a=cle
        c=dico_etage[trouver_nombre_eloigne(a,b)]
        e=list(c.values())
        d=e[random.randint(len(e)-7,len(e)-1)]
        for cle, val in c.items():
            if val==d:
                d=cle
        resultata, _ = algo.dijkstra(depart, d)
        resultatb, _ = algo.dijkstra(d, arrivee)
        resultat=resultata+resultatb

    if resultat is None:
        return None, None

    for s in resultat:
        if not s:
            continue

        last = s[-1]

        # Couloir A à E + N
        if ('A' <= last <= 'E') or last == 'N':
            chemins3.append(layers_3[s])
            

        # Couloir F à M
        elif 'F' <= last <= 'M':
            chemins2.append(layers_2[s])

        elif 'O' <= last <= 'R':
            chemins1.append(layers_1[s])

        elif 'S' <= last <= 'X':
            chemins_cdi.append(layers_cdi[s])

        elif 'Y' <= last <= 'Z' or s.endswith(("A1","B1","C1","D1","E1")):
            chemins1B.append(layers_1B[s])

        # Si c'est un chiffre
        elif last.isdigit():
            layer2 = layers_2.get(s)
            layer3 = layers_3.get(s)
            layer1 = layers_1.get(s)
            layer_cdi = layers_cdi.get(s)
            layer_1B = layers_1B.get(s)

            if layer2:
                chemins2.append(layer2)
            if layer3:
                chemins3.append(layer3)
            if layer1:
                chemins1.append(layer1)
            if layer_cdi:
                chemins_cdi.append(layer_cdi)
            if layer_1B:
                chemins1B.append(layer_1B)
    
    # Rendre salle de départ et d'arrivée visibles
    if depart in layers_3:
        chemins3.append(layers_3[depart])
    elif depart in layers_2:
        chemins2.append(layers_2[depart])
    elif depart in layers_1:
        chemins1.append(layers_1[depart])
    elif depart in layers_cdi:
        chemins_cdi.append(layers_cdi[depart])
    elif depart in layers_1B:
        chemins1B.append(layers_1B[depart])
    
    if arrivee in layers_3:
        chemins3.append(layers_3[arrivee])
    elif arrivee in layers_2:
        chemins2.append(layers_2[arrivee])
    elif arrivee in layers_1:
        chemins1.append(layers_1[arrivee])
    elif arrivee in layers_cdi:
        chemins_cdi.append(layers_cdi[arrivee])
    elif arrivee in layers_1B:
        chemins1B.append(layers_1B[arrivee])
    
    chemins_cdi.append(tmx_data_c.layers[9])
    chemins1.append(tmx_data_d.layers[8])
    chemins2.append(tmx_data_b.layers[17])
    chemins3.append(tmx_data.layers[12])
    chemins1B.append(tmx_data_e.layers[10])
    chemins = [chemins_cdi,chemins1,chemins1B, chemins2, chemins3]
    liste_etage.clear()
    for element in resultat:
        for layer in layers:
            if element in layer.keys():
                for cle, v in dico_etage.items():
                    if v == layer:
                         if cle not in liste_etage:
                            liste_etage.append(cle)
    return resultat, chemins


# =========================
# FONCTIONNALITÉS BONUS
# =========================

def fonctionnalitees(depart, arrivee):
    """Retourne un dictionnaire de calories et temps pour l'itinéraire trouvé."""

    _, distance = algo.dijkstra(depart, arrivee)

    return {
        "calories": str(distance * 0.9),
        "temps": str(distance * 9 // 60) + " min " + str(distance * 9 % 60)
    }


def enlever_accents(texte):
    """Supprime les accents d'une chaîne pour normaliser les clés de cours."""
    return ''.join(c for c in unicodedata.normalize('NFD', texte) if unicodedata.category(c) != 'Mn')

def get_ennui(cours):
    """Retourne un niveau d'ennui pour une matière.

    Si la matière n'est pas enregistrée, valeur par défaut 50.
    """
    cours_nettoye = enlever_accents(cours).lower()
    resultat = ennui_par_cours.get(cours_nettoye, 50)
    return resultat

def message_ennui(taux):
    """Retourne un message court en fonction du taux d'ennui."""
    if taux > 75:
        return "Bonne chance"
    elif taux >= 40:
        return "Tranquille"
    else:
        return "Ba incroyable"

def get_message(cours):
    """Retourne un message d'encouragement selon le cours."""
    cours_nettoyee = enlever_accents(cours).lower()
    message_trouve = messages_par_cours.get(cours_nettoyee, "Bonne route !")
    return message_trouve

def infos_cours(cours):
    """Retourne un dictionnaire d'informations sur le cours.

    Clé:
    - ennui: score de 0 à 100.
    - message_ennui: commentaire court.
    - message: message détaillé.
    """
    taux = get_ennui(cours)
    msg_ennui = message_ennui(taux)
    message = get_message(cours)
    return {'ennui': taux, 'message_ennui': msg_ennui, 'message': message}

def trouver_etages(resultat):
    """Retourne la liste des étages traversés d'après le résultat du chemin."""
    pass
                          

    


def suggestion(depart, arrivee, tmx_data, tmx_data_b, tmx_data_d, tmx_data_c, tmx_data_e, layers_2, layers_3, layers_1, layers_cdi, layers_1B):
    """(À compléter) Suggestion d'itinéraire selon les étages et la distance."""
    # fait la liste dans l'ordre des étages empruntés.
    pass
