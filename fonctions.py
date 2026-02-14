import algo

# =========================
# FONCTION GPS
# =========================

def gps(depart, arrivee, tmx_data, tmx_data_b, tmx_data_d, tmx_data_c, layers_2, layers_3, layers_1, layers_cdi):

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
        chemins = [chemins1, chemins_cdi, chemins2, chemins3]
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
            chemins3.append(tmx_data.layers[12])
            

        # Couloir F à M
        elif 'F' <= last <= 'M':
            chemins2.append(layers_2[s])
            chemins2.append(tmx_data_b.layers[15])

        elif 'o' <= last <= 'r':
            chemins1.append(tmx_data_d.layers[15])
            chemins1.append(layers_1[s])

        elif 's' <= last <= 'z':
            chemins1.append(tmx_data_c.layers[15])
            chemins1.append(layers_cdi[s])

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
                chemins1.append(layer_cdi)
    
    chemins = [chemins1, chemins_cdi, chemins2, chemins3]
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
