
"""
Représente le lycée.
Chaque sommet correspond à une salle, un couloir ou un escalier.
Les arêtes représentent les déplacements possibles avec un poids correspondant au temps.
"""
graphe = {
    "A301": {"COULOIR_A": 1},
    "A302": {"COULOIR_A": 1},
    "A303": {"COULOIR_A": 1},
    "A304": {"COULOIR_A": 1},
    "A305": {"COULOIR_A": 1},
    "A306": {"COULOIR_A": 1},
    "A307": {"COULOIR_A": 1},
    "A308": {"COULOIR_A": 1},

    "B311": {"COULOIR_B": 1},
    "B312": {"COULOIR_B": 1},
    "B313": {"COULOIR_B": 1},
    "B314": {"COULOIR_B": 1},
    "B315": {"COULOIR_B": 1},
    "B316": {"COULOIR_B": 1},
    "B317": {"COULOIR_B": 1},
    "B318": {"COULOIR_B": 1},

    "COULOIR_A": {
        "A301": 1,
        "A302": 1,
        "A303": 1,
        "A304": 1,
        "A305": 1,
        "A306": 1,
        "A307": 1,
        "A308": 1,
        "COULOIR_B": 2,
        "ESCALIER": 3
    },

    "COULOIR_B": {
        "B311": 1,
        "B312": 1,
        "B313": 1,
        "B314": 1,
        "B315": 1,
        "B316": 1,
        "B317": 1,
        "B318": 1,
        "COULOIR_A": 2,
        "ESCALIER": 3
    },

    "ESCALIER": {
        "COULOIR_A": 3,
        "COULOIR_B": 3
    }
}



def dijkstra(graphe, depart, arrivee):
    """
    Algorithme de Dijkstra.
    Calcule le plus court chemin entre le sommet de départ et le sommet d'arrivée.
    """

    """
    distance: distance minimale connue depuis le départ
    precedent : permet de reconstruire le chemin
    non_visites : sommets pas encore vu
    """
    distances = {}
    precedent = {}
    non_visites = []

    """
    Tous les sommets sont initialisés avec une distance infinie
    sauf le sommet de départ où sa distance est nul.
    """
    for sommet in graphe:
        distances[sommet] = float("inf")
        precedent[sommet] = None
        non_visites.append(sommet)

    distances[depart] = 0

    """
    A chaque étape, on sélectionne le sommet non visité
    ayant la plus petite distance.
    """
    while non_visites:
        sommet_courant = min(non_visites, key=lambda s: distances[s])
        non_visites.remove(sommet_courant)

        if sommet_courant == arrivee:
            break
