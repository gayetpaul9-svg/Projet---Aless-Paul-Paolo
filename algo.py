"""
Représente le lycée. Chaque sommet correspond à une salle, un couloir ou un escalier.
Les arêtes représentent les déplacements possibles avec un poids correspondant au temps.
"""
graphe = {

    "A106": {"COULOIR_O": 1},
    "A107": {"COULOIR_O": 1},
    "A108": {"COULOIR_O": 1},

    "A105": {"COULOIR_R": 1},
    "A104": {"COULOIR_R": 1},
    "A103": {"COULOIR_R": 1},
    "A102": {"COULOIR_R": 1},

    "A014": {"COULOIR_X": 1},
    "A013": {"COULOIR_X": 1},
    "A012": {"COULOIR_X": 1},
    "A011": {"COULOIR_X": 1},
    "A010": {"COULOIR_X": 1},

    "A006": {"COULOIR_V": 1},
    "A007": {"COULOIR_V": 1},
    "A008": {"COULOIR_V": 1},
    "A009": {"COULOIR_V": 1},

    "A005": {"COULOIR_T": 1},
    "A003": {"COULOIR_T": 1},
    "A002": {"COULOIR_T": 1},

    "A001": {"COULOIR_U": 1},
    
    "A301": {"COULOIR_A": 1},
    "A302": {"COULOIR_A": 1},
    "A303": {"COULOIR_A": 1},
    
    "A304": {"COULOIR_B": 1},
    "A305": {"COULOIR_B": 1},
    "A306": {"COULOIR_B": 1},
    "A307": {"COULOIR_B": 1},
    "A308": {"COULOIR_B": 1},
    "A309": {"COULOIR_B": 1},
    "A310": {"COULOIR_B": 1},
    "B311": {"COULOIR_N": 1},
    
    "B312": {"COULOIR_C": 1},
    "B313": {"COULOIR_C": 1},
    "B314": {"COULOIR_C": 1},
    
    "B315": {"COULOIR_D": 1},
    "B316": {"COULOIR_D": 1},
    "B317": {"COULOIR_D": 1},
    "B318": {"COULOIR_D": 1},

    "B319": {"COULOIR_E": 1},
    "B320": {"COULOIR_E": 1},
    "B321": {"COULOIR_E": 1},
    "B322": {"COULOIR_E": 1},
    "B323": {"COULOIR_E": 1},
    "B324": {"COULOIR_E": 1},
    "B325": {"COULOIR_E": 1},

    "A201": {"COULOIR_F": 1},
    "A202": {"COULOIR_F": 1},
    "A203": {"COULOIR_F": 1},
    "A204": {"COULOIR_F": 1},

    "A205": {"COULOIR_G": 1},
    "A206": {"COULOIR_G": 1},
    "A207": {"COULOIR_G": 1},

    "A208": {"COULOIR_H": 1},
    "A209": {"COULOIR_H": 1},
    "A210": {"COULOIR_H": 1},
    "A211": {"COULOIR_H": 1},
    "A212": {"COULOIR_H": 1},

    # Salles B200
    "B214": {"COULOIR_J": 1},
    "B215": {"COULOIR_I": 1},
    "B216": {"COULOIR_I": 1},

    "B217": {"COULOIR_I": 1},
    "B218": {"COULOIR_I": 1},
    "B219": {"COULOIR_K": 1},
    "B220": {"COULOIR_K": 1},
    "B221": {"COULOIR_K": 1},

    "B222": {"COULOIR_L": 1},
    "B223": {"COULOIR_L": 1},

    "COULOIR_A": {
        "A301": 1,
        "A302": 1,
        "A303": 1,
        "COULOIR_B": 2,
    },

    "COULOIR_B": {
        "A304": 1,
        "A305": 1,
        "A306": 1,
        "A307": 1,
        "A308": 1,
        "A309": 1,
        "A310": 1,
        "COULOIR_A": 2,
        "COULOIR_N": 2,
        "ESCALIER_1": 3,
        "ESCALIER_2": 3,
    },

    "COULOIR_N": {
        "B311": 1,
        "COULOIR_B": 2,
        "COULOIR_C": 2,
        "ESCALIER_2": 3,
    },

    "COULOIR_C": {
        "B312": 1,
        "B313": 1,
        "B314": 1,
        "COULOIR_D": 2,
        "COULOIR_B": 2,
        "ESCALIER_3": 3,
    },
    "COULOIR_D": {
        "B315": 1,
        "B316": 1,
        "B317": 1,
        "B318": 1,
        "COULOIR_E": 2,
        "COULOIR_C": 2,
        "ESCALIER_4": 3,
        "ESCALIER_5": 3,
    },

    "COULOIR_E": {
        "B319": 1,
        "B320": 1,
        "B321": 1,
        "B322": 1,
        "B323": 1,
        "B324": 1,
        "B325": 1,
        "COULOIR_D": 2,
    },

    "ESCALIER_1": {
        "COULOIR_B": 3,
        "COULOIR_F": 3,
    },

    "ESCALIER_2": {
        "COULOIR_N": 3,
        "COULOIR_H": 3,
    } ,# type: ignore

    "ESCALIER_3": {
        "COULOIR_C": 3,
        "COULOIR_I": 3,

    },# type: ignore

    "ESCALIER_4": {
        "COULOIR_D": 3,
        "COULOIR_K": 3,
    },# type: ignore

    "ESCALIER_5": {
        "COULOIR_D": 3,
        "COULOIR_L": 3,
    },# type: ignore

    "ESCALIER_6": {
        "COULOIR_F": 3,
        "COULOIR_O": 3,
        "COULOIR_T": 3,
    },# type: ignore

    "ESCALIER_7": {
        "COULOIR_R": 3,
    },# type: ignore

    "ESCALIER_9": {
        "COULOIR_Q": 3,
        "COULOIR_U": 3,
    },# type: ignore

    # Salles A200
    

    # Couloirs renommés
    "COULOIR_F": {
        "A201": 1, 
        "A202": 1, 
        "A203": 1, 
        "A204": 1,
        "COULOIR_G": 2,
        "COULOIR_H": 2,
        "ESCALIER_1": 3,
        "ESCALIER_6": 3,
    },

    "COULOIR_G": {
        "A205": 1, 
        "A206": 1, 
        "A207": 1,
        "COULOIR_F": 2,
        "ESCALIER_6": 3,
    },

    "COULOIR_H": {
        "A208": 1, 
        "A209": 1, 
        "A210": 1, 
        "A211": 1,
        "A212": 1,
        "COULOIR_F": 2,
        "ESCALIER_2": 3,
    },

    "COULOIR_I": {
        "B215": 1, 
        "B216": 1,
        "B217": 1,
        "B218": 1,
        "COULOIR_J": 2,
        "ESCALIER_3": 3,
    },

    "COULOIR_J": {
        "B214": 1,
        "COULOIR_I": 2,
        "COULOIR_K": 2,
    },

    "COULOIR_K": {
        "B219": 1, 
        "B220": 1, 
        "B221": 1,
        "COULOIR_J": 2,
        "COULOIR_L": 2,
        "ESCALIER_4": 3,
    },

    "COULOIR_L": {
        "B222": 1, 
        "B223": 1,
        "COULOIR_K": 2,
        "COULOIR_M": 2,
        "ESCALIER_5": 3,
    },

    "COULOIR_M": {
        "COULOIR_L": 2,
        "COULOIR_I": 2,
    },

    "COULOIR_O": {
        "COULOIR_P": 2,
        "ESCALIER_6": 3,
        "A106": 1, 
        "A107": 1,
        "A108": 1,
    },

    "COULOIR_P": {
        "COULOIR_O": 2,
        "COULOIR_Q": 2,
    },

    "COULOIR_Q": {
        "COULOIR_P": 2,
        "COULOIR_R": 2,
        "ESCALIER_9": 3,
    },

    "COULOIR_R": {
        "COULOIR_Q": 2,
        "ESCALIER_7": 3,
        "A105": 1, 
        "A104": 1,
        "A103": 1,
        "A102": 1,
    },

    "COULOIR_S": {
        "COULOIR_T": 2,
        "COULOIR_V": 2,
    },

    "COULOIR_T": {
        "COULOIR_S": 2,
        "COULOIR_U": 2,
        "ESCALIER_6": 3,
        "A005": 1, 
        "A003": 1,
        "A002": 1,
    },

    "COULOIR_U": {
        "COULOIR_T": 2,
        "ESCALIER_9": 3,
        "A001": 1,
    },

    "COULOIR_V": {
        "COULOIR_S": 2,
        "COULOIR_W": 2,
        "A006": 1,
        "A007": 1,
        "A008": 1,
        "A009": 1,
    },

    "COULOIR_W": {
        "COULOIR_V": 2,
        "COULOIR_X": 2,
    },

    "COULOIR_X": {
        "COULOIR_W": 2,
        "A014": 1,
        "A013": 1,
        "A012": 1,
        "A011": 1,
        "A010": 1,
    },
}

def dijkstra(depart, arrivee):
    """
    Algorithme de Dijkstra.
    Calcule le plus court chemin entre le sommet de départ et le sommet d'arrivée.
    """
    # Validate inputs
    if depart not in graphe or arrivee not in graphe:
        return None

    print(f"Départ: {depart}, Arrivée: {arrivee}")

    distances = {}
    precedent = {}
    non_visites = []

    # Initialisation
    for sommet in graphe:
        distances[sommet] = float("inf")
        precedent[sommet] = None
        non_visites.append(sommet)
    distances[depart] = 0

    # Boucle principale
    while len(non_visites) > 0:
        # Trouvé le sommet non visitée avec la plus petite distance
        min_distance = float("inf")
        sommet_courant = None
        for sommet in non_visites:
            if distances[sommet] < min_distance:
                min_distance = distances[sommet]
                sommet_courant = sommet

        # if no reachable unvisited node remains, stop
        if sommet_courant is None or min_distance == float("inf"):
            break

        if sommet_courant not in non_visites:
            break

        non_visites.remove(sommet_courant)

        if sommet_courant == arrivee:
            break

        voisins = graphe[sommet_courant]
        for voisin in voisins:
            distance_temporaire = distances[sommet_courant] + voisins[voisin]
            if distance_temporaire < distances[voisin]:
                distances[voisin] = distance_temporaire
                precedent[voisin] = sommet_courant

    # Reconstruction du chemin
    chemin = []
    sommet = arrivee
    while sommet != None:
        chemin.insert(0, sommet)
        sommet = precedent[sommet]

    '''if distances[arrivee] == float("inf"):
        return None'''

    # Retourner le chemin sans le départ et l'arrivée
    chemin_intermediaire = chemin[1:-1] if len(chemin) > 2 else []
    return chemin_intermediaire, distances[arrivee]
   

"""salle_depart = input("Salle de départ : ")
salle_arrivee = input("Salle d'arrivée : ")

if salle_depart not in graphe or salle_arrivee not in graphe:
    print("Salle invalide.")
else:
    resultat = dijkstra( salle_depart, salle_arrivee)
    if resultat == None:
        print("Aucun chemin trouvé.")
    else:
        chemin, distance = resultat
        print("Chemin le plus court :")
        print(" → ".join(chemin))
        print("Distance totale :", distance)
307"""
