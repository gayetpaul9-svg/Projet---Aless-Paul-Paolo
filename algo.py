"""
Représente le lycée. Chaque sommet correspond à une salle, un couloir ou un escalier.
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

    if distances[arrivee] == float("inf"):
        return None

    return chemin, distances[arrivee]

salle_depart = input("Salle de départ : ")
salle_arrivee = input("Salle d'arrivée : ")

if salle_depart not in graphe or salle_arrivee not in graphe:
    print("Salle invalide.")
else:
    resultat = dijkstra(graphe, salle_depart, salle_arrivee)
    if resultat == None:
        print("Aucun chemin trouvé.")
    else:
        chemin, distance = resultat
        print("Chemin le plus court :")
        print(" → ".join(chemin))
        print("Distance totale :", distance)
