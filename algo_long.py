import algo #type: ignore

graphe = algo.graphe

def plus_long_chemin(depart, arrivee):
    
    if depart not in graphe or arrivee not in graphe:
        return None, 0

    meilleur_chemin = []
    meilleur_distance = 0
    salles_visitees = [depart]

    # Fonction qui explore le graphe récursivement
    def explorer(salle_actuelle, chemin_actuel, distance_actuelle):
        
        # On a accès aux variables du dessus grâce à "nonlocal"
        nonlocal meilleur_chemin, meilleur_distance

        if salle_actuelle == arrivee:
            if distance_actuelle > meilleur_distance:
                meilleur_distance = distance_actuelle
                meilleur_chemin = chemin_actuel.copy()
            return

        #salles voisines accessibles depuis la salle actuelle
        for voisin, poids in graphe[salle_actuelle].items():
            if voisin not in salles_visitees:
                salles_visitees.append(voisin)
                chemin_actuel.append(voisin)

                # On continue d'explorer depuis ce voisin
                explorer(voisin, chemin_actuel, distance_actuelle + poids)

                # On revient en arrière : on retre le voisin du chemin et des visitées
                # pour pouvoir explorer d'autres chemins
                chemin_actuel.pop()
                salles_visitees.remove(voisin)

    # on lanc l'exploration depuis le depart
    explorer(depart, [depart], 0)

    if meilleur_chemin == []:
        return None, 0

    # on retire le depart et l'arrivée du chemin (comme dans algo.py)
    chemin_intermediaire = meilleur_chemin[1:-1] if len(meilleur_chemin) > 2 else []

    return chemin_intermediaire, meilleur_distance


def gps_long(depart, arrivee, tmx_data, tmx_data_b, tmx_data_d, tmx_data_c, layers_2, layers_3, layers_1, layers_cdi):

    chemins1 = []
    chemins_cdi = []
    chemins2 = []
    chemins3 = []


    if not depart or not arrivee:
        print("Départ ou arrivée non défini.")
        chemins1.append(tmx_data_d.layers[8])
        chemins_cdi.append(tmx_data_c.layers[9])
        chemins3.append(tmx_data.layers[12])
        chemins2.append(tmx_data_b.layers[15])
        chemins = [chemins_cdi, chemins1, chemins2, chemins3]
        print("chemins :", chemins)
        return None, chemins

    resultat, _ = plus_long_chemin(depart, arrivee)

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
    chemins_cdi.append(tmx_data_c.layers[9])
    chemins1.append(tmx_data_d.layers[8])
    chemins2.append(tmx_data_b.layers[16])
    chemins3.append(tmx_data.layers[12])
    chemins = [chemins_cdi,chemins1, chemins2, chemins3]
    print(chemins)
    return resultat, chemins

def fonctionnalitees_long(depart, arrivee):

    _, distance = plus_long_chemin(depart, arrivee)

    return {
        "calories": str(distance * 0.9),
        "temps": str(distance * 9 // 60) + " : " + str(distance * 9 % 60)
    }