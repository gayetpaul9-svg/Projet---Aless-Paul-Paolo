# Projet GPS CIV NSI
## Notre projet est de faire une map du CIV en 2D pour par la suite faire un gps en entrant la salle où l'on veut aller et montrer le chemins le plus court d'une classe à l'autre.
![Image CIV](https://www.blog.asso-api.org/wp-content/uploads/2023/07/bandeauCIV.jpg)
![Image CIV](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQV7ByOkW2OdXD0OkoAmRCXzYGkG0j5I808lg&s) 
![Image CIV](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRuND2-FKN7CX-FM7TQSv8vf00hZX9XHOuaig&s)

# Projet GPS CIV NSI

## Description du projet
Notre projet consiste à créer une carte en 2D du CIV, permettant aux utilisateurs de se diriger facilement d’une salle à l’autre en utilisant un GPS interactif. Le chemin sera calculé à l’aide de l’algorithme de Dijkstra. Ce projet sera développé en utilisant la bibliothèque **Pygame**, avec une possibilité d'extension en 3D avec **Ursina**.

---

# Cahier des charges

### 1. Plan du lycée en 2D
- **Cartographie du bâtiment** : Représenter le plan du lycée avec plusieurs étages, principalement le bâtiment A (et potentiellement le bâtiment B).
  - Affichage de chaque étage de manière claire.
  
- **Affichage des salles** : Chaque salle sera représentée sur le plan avec des labels (ex : "Salle 101", "Salle 202", etc.).

---

### 2. Interface utilisateur (UI)
- **Choix des salles** : L’utilisateur pourra sélectionner dans un menu déroulant la salle de départ et la salle d’arrivée à partir d’une liste de salles disponibles/en sélectionnant sur la carte/en écrivant le nom de la salle.
  
- **Affichage du chemin** : Une fois le chemin calculé, le trajet à suivre sera tracé sur la carte en 2D.

- **Instructions textuelles** : Des messages (affichés dans un bandeau lattéral) afficheront les étapes du trajet à suivre, comme "Tourner à gauche" ou "Monter au 2ème étage".

---

### 3. Calcul du chemin le plus court avec Dijkstra
- **Algorithme de Dijkstra** : Le plan sera modélisé sous forme de graphe, chaque salle étant un noeud et chaque couloir une arête. L’algorithme de Dijkstra sera utilisé pour déterminer le chemin le plus court.
  
- **Estimation du temps de trajet** : Le temps de trajet estimé sera calculé en fonction de la distance et de la vitesse de marche.

---

### 4. Fonctionnalités supplémentaires
- **Types de trajets** :
  - **Plus court** : Le chemin le plus rapide en termes de distance.
  - **Plus long** : Permet de choisir un itinéraire plus long.
  - **Énergie minimum** : Privilégier des trajets avec moins de montée d'escaliers ou autres efforts physiques.

- **Calcul des calories** : Estimation des calories brûlées en fonction de la distance et de l'effort physique (par exemple, monter un étage).
  
- **Enregistrement des trajets favoris** : Permettre à l’utilisateur d’enregistrer et nommer des trajets pour une utilisation future.

- **Trajet vers les toilettes les plus proches** : Ajouter une fonctionnalité permettant de trouver et de guider l’utilisateur vers les toilettes les plus proches.

- **Calcul du taux d'ennui en fonction de la salle et du cours** : Permettre à l'utilisateur de savoir en avance à quoi s'attendre

---

### 5. Aspect graphique et ergonomie
- **Graphisme** : Design simple, épuré et moderne. Utilisation de couleurs claires et d'icônes visibles pour une bonne lisibilité.

- **Personnalisation de l'interface** : Permettre à l'utilisateur de personnaliser la couleur principale de l'interface (par exemple, thème clair ou sombre).
  
- **Navigation au clavier et à la souris** : Le programme sera navigable à l’aide du clavier et de la souris.

---

### 6. Technologies utilisées
- **Pygame** : Utilisation de la bibliothèque Pygame pour créer l’interface graphique 2D et gérer l'interaction avec l’utilisateur.
  
---

# Liste des tâches:
##### Nous utiliserons la bibliothèque pygame et (ursina(3d)peut etre) ainsi que l'algorithme dijkstra
- - [ ] Une interface avec un plan du lycée (batiments A(étage par étage) sûr et peut etre batiment B)
    - [ ] étages 
- - [ ] Une interface utilisateur qui permet de choisir la salle de départ et celle d'arrivée
- - [ ] Une ligne indiquant le chemin à suivre
- - [ ] des messages qui indiquent chaque action (tourner a droite/gauche, monter d'un étage,avancer etc)
- - [ ] calcul du temps de trajet estimée
- - [ ] messages personnalisés en fonction des cours et des salles ainsi qu'un calcul du taux d'ennuie en fonction du cours.
- - [ ] Des choix de types de trajet
    - [ ] Plus court ou plus long
    - [ ] Energie minimum
    - [ ] calcul des calories
    - [ ] on peut enregistrer et nommer des trajets dans les favoris pour les réutiliser
    - [ ] trajet ver les toilettes les plus prochees
- - [ ] Aspect graphique
    - [ ] Graphisme simple, épuré et moderne
    - [ ] Utilisable avec le clavier
    - [ ] Couleur principale de l'interface personnalisable
    - [ ] format pc
    - [ ] clavié et souris
    
