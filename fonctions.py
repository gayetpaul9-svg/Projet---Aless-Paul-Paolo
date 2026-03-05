import algo
import algo_long
from algo import graphe

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


def selectionner_etape_lointaine(depart, arrivee):
    """
    Sélectionne l'étape intermédiaire la plus loin possible de la salle d'arrivée.
    
    Paramètres:
        depart: Salle de départ
        arrivee: Salle d'arrivée
    
    Retourne:
        (etape_lointaine, distance_a_l_arrivee) ou (None, 0) si pas de chemin valide
    """
    # Vérifier que les salles existent
    if depart not in graphe or arrivee not in graphe:
        print("Salle invalide.")
        return None, 0
    
    # Récupérer le chemin optimal du départ à l'arrivée
    chemin, _ = algo.dijkstra(depart, arrivee)
    
    if chemin is None or len(chemin) == 0:
        print("Aucun chemin trouvé.")
        return None, 0
    
    # Calculer les distances de toutes les salles à l'arrivée
    distances = dijkstra_inverse(arrivee)
    
    # Trouver l'étape intermédiaire la plus loin de l'arrivée sur le chemin
    etape_lointaine = None
    distance_max = -1
    
    for etape in chemin:
        distance = distances.get(etape, float("inf"))
        if distance != float("inf") and distance > distance_max:
            distance_max = distance
            etape_lointaine = etape
    
    if etape_lointaine is None:
        print("Aucune étape intermédiaire trouvée.")
        return None, 0
    print(f"Étape intermédiaire la plus lointaine de l'arrivée : {etape_lointaine} (distance à l'arrivée : {distance_max})")
    return etape_lointaine

# =========================
# FONCTION GPS
# =========================

def gps(depart, arrivee, tmx_data, tmx_data_b, tmx_data_d, tmx_data_c, layers_2, layers_3, layers_1, layers_cdi,long):

    chemins1 = []
    chemins_cdi = []
    chemins2 = []
    chemins3 = []


    if not depart or not arrivee:
        print("Départ ou arrivée non défini.")
        chemins1.append(tmx_data_d.layers[8])
        chemins_cdi.append(tmx_data_c.layers[9])
        chemins3.append(tmx_data.layers[12])
        chemins2.append(tmx_data_b.layers[17])
        chemins = [chemins_cdi, chemins1, chemins2, chemins3]
        print("chemins :", chemins)
        return None, chemins
    if long == False:
        resultat, _ = algo.dijkstra(depart, arrivee)
    else:
        resultat, _ = algo_long.chemin_aleatoire_unique(graphe,depart,arrivee,selectionner_etape_lointaine(depart, arrivee))
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

        # Si c'est un chiffre
        elif last.isdigit():
            layer2 = layers_2.get(s)
            layer3 = layers_3.get(s)
            layer1 = layers_1.get(s)
            layer_cdi = layers_cdi.get(s)

            if layer2:
                chemins2.append(layer2)
            if layer3:
                chemins3.append(layer3)
            if layer1:
                chemins1.append(layer1)
            if layer_cdi:
                chemins_cdi.append(layer_cdi)
    
    # Rendre salle de départ et d'arrivée visibles
    if depart in layers_3:
        chemins3.append(layers_3[depart])
    elif depart in layers_2:
        chemins2.append(layers_2[depart])
    elif depart in layers_1:
        chemins1.append(layers_1[depart])
    elif depart in layers_cdi:
        chemins_cdi.append(layers_cdi[depart])
    
    if arrivee in layers_3:
        chemins3.append(layers_3[arrivee])
    elif arrivee in layers_2:
        chemins2.append(layers_2[arrivee])
    elif arrivee in layers_1:
        chemins1.append(layers_1[arrivee])
    elif arrivee in layers_cdi:
        chemins_cdi.append(layers_cdi[arrivee])
    
    chemins_cdi.append(tmx_data_c.layers[9])
    chemins1.append(tmx_data_d.layers[8])
    chemins2.append(tmx_data_b.layers[17])
    chemins3.append(tmx_data.layers[12])
    chemins = [chemins_cdi,chemins1, chemins2, chemins3]
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
