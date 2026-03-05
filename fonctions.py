import algo

# =========================
# FONCTION GPS
# =========================

def gps(depart, arrivee, tmx_data, tmx_data_b, tmx_data_d, tmx_data_c,tmx_data_e, layers_2, layers_3, layers_1, layers_cdi, layers_1B):

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

    resultat, _ = algo.dijkstra(depart, arrivee)

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
