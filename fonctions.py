import algo
import algo_long
from algo import graphe
from layers import *
import random

# =========================
# SELECTION ETAPE INTERMEDIAIRE LOINTAINE
# =========================

def dijkstra_inverse(arrivee):
    """
    Calcule les distances de TOUTES les salles vers l'arrivée.
    Utilise Dijkstra en inversant la direction d graphe.
    Retourne un dictionnaire {salle: distance_vers_arrivee}
    """
    distances = {}
    precedent = {}
    non_visites = []

    # Initialisation
    for sommet in graphe:
        distances[sommet] = float("inf")
        precedent[sommet] = None
        non_visites.append(sommet)
    distances[arrivee] = 0

    # Boucle principale
    while len(non_visites) > 0:
        # Trouvé le sommet non visité avec la plus petite distance
        min_distance = float("inf")
        sommet_courant = None
        for sommet in non_visites:
            if distances[sommet] < min_distance:
                min_distance = distances[sommet]
                sommet_courant = sommet

        if sommet_courant is None or min_distance == float("inf"):
            break

        non_visites.remove(sommet_courant)

        # Explorer les voisins
        voisins = graphe[sommet_courant]
        for voisin in voisins:
            distance_temporaire = distances[sommet_courant] + voisins[voisin]
            if distance_temporaire < distances[voisin]:
                distances[voisin] = distance_temporaire
                precedent[voisin] = sommet_courant

    return distances


def trouver_nombre_eloigne(debut, fin):
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

def gps(depart, arrivee, tmx_data, tmx_data_b, tmx_data_d, tmx_data_c,tmx_data_e, layers_2, layers_3, layers_1, layers_cdi, layers_1B,long=False):

    chemins1 = []
    chemins_cdi = []
    chemins2 = []
    chemins3 = []
    chemins1B = []


    if not depart or not arrivee:
        print("Départ ou arrivée non défini.")
        chemins1.append(tmx_data_d.layers[8])
        chemins_cdi.append(tmx_data_c.layers[9])
        chemins3.append(tmx_data.layers[12])
        chemins2.append(tmx_data_b.layers[17])
        chemins1B.append(tmx_data_e.layers[10])
        chemins = [chemins_cdi,chemins1B, chemins1, chemins2, chemins3]        
        print("chemins :", chemins)
        return None, chemins
    if long == False:
        resultat, _ = algo.dijkstra(depart, arrivee)
    else:
        #recherche etage depart
        for layer_etage in layers:
            for cle, val in layer_etage.items():
                if val == arrivee:
                    b=cle
        for layer_etage in layers:
            for cle, val in layer_etage.items():
                if val == depart:
                    a=cle
        c=dico_etage[trouver_nombre_eloigne(a,b)]
        d=c[random.randint(0,len(cle)-1)]
        resultata, _ = algo.dijkstra(depart, d)
        print("etape intermediare = ",d)
        resultatb, _ = algo.dijkstra(d, arrivee)
        resultat=resultata+resultatb
        print("mode long")

    print("Chemin trouvé :", resultat)

    if resultat is None:
        print("Aucun chemin trouvé par l'algorithme.")
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
            print("Chemin ajouté à chemins2 :", layers_2[s])

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
    chemins = [chemins_cdi,chemins1B,chemins1, chemins2, chemins3]
    print(chemins)
    return resultat, chemins


# =========================
# FONCTIONNALITÉS BONUS
# =========================

def fonctionnalitees(depart, arrivee):

    _, distance = algo.dijkstra(depart, arrivee)

    return {
        "calories": str(distance * 0.9),
        "temps": str(distance * 9 // 60) + " : " + str(distance * 9 % 60)
    }
