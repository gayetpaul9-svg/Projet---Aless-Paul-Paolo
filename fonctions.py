import algo

# =========================
# FONCTION GPS
# =========================

def gps(depart, arrivee, tmx_data, tmx_data_b, layers_2, layers_3):

    chemins1 = []
    chemins2 = []
    chemins3 = []

    if not depart or not arrivee:
        print("Départ ou arrivée non défini.")
        chemins3.append(tmx_data.layers[12])
        chemins2.append(tmx_data_b.layers[15])
        chemins = [chemins1, chemins2, chemins3]
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

        # Si c'est un chiffre
        elif last.isdigit():
            chemins2.append(layers_2[s])
            chemins3.append(layers_3[s])
    
    chemins = [chemins1, chemins2, chemins3]
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
