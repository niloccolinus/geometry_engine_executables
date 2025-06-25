# ⚙️ geometry_engine_executables

Ce répertoire contient les scripts exécutables et les interfaces de démonstration du moteur de géométrie.

## Description

`geometry_engine_executables` propose des exemples concrets d'utilisation de la bibliothèque `geometry_engine_librairie`. Ces scripts permettent de résoudre et de visualiser des exercices géométriques. À ce jour, plusieurs scripts sont disponibles, chacun ayant un objectif spécifique. 


### Liste des scripts

1. **tp_0_ins.py** - Affiche un message "Hello World"

    Ce script est un simple exemple pour tester si l'environnement est correctement configuré. Il affiche "Hello World" dans le terminal.


2. **tp_1_julia.py** - Visualisation de l'ensemble de Julia

    Ce script permet de visualiser l'ensemble de Julia, une structure fractale complexe. L'ensemble de Julia est généré en fonction d'un nombre complexe donné, et chaque pixel de l'écran est colorié en fonction de la divergence ou non de la suite complexe associée à ce pixel.


3. **tp_2_exos.py** - Résout et visualise un exercice géométrique

    Ce script résout et visualise un exercice de géométrie. 

4. **tp_2_delaunay.py** - Calcule et visualise une triangulation de Delaunay

    Ce script calcule la triangulation de Delaunay d'un ensemble de points aléatoires dans un plan. Il utilise l'algorithme de Bowyer-Watson pour construire la triangulation.

5. **tp_3_exo1.py** - Implémentation et visualisation des transformations homogènes

    Ce script illustre l’utilisation des classes de transformation homogène (translation, rotation, homothétie) en combinant ces transformations sur un personnage et son épée. Il applique ces transformations et affiche les résultats dans la console.

6. **tp_3_exo3.py** - Visualisation de cercles en orbite

    Ce script illustre l’utilisation des classes de similitudes (translation, rotation) en coordonnées homogènes, en simulant la trajectoire de 2 cercles en orbite autour d'un troisième cercle, lui même en rotation autour de l'origine du repère. Ces trajectoires sont visualisables grâce à la classe renderer.py et la bibliothèque pygame.

7. **tp_4_rendercube.py** - Implémentation d'une pipeline de rendu simplifiée.

   Ce script utilise des notions de géométrie spatiale pour afficher un cube en 3D.

8. **tp_5_airplane.py** - Affichage d'un avion en 3D.

   Ce script reprend le pipeline réalisé précédemment pour afficher un modèle d'avion.

   **tp_6_two-airplanes.py** - Affichage de deux avions en 3D.

   Ce script reprend le pipeline réalisé précédemment pour afficher deux modèles d'avion avec une rotation : l'une utilisant les angles d'Euler, et l'autre uilisant les quaternions.

### Comment lancer les scripts

1. **Avec Sublime Text (si vous utilisez ce programme)** :
   - Ouvrez le projet dans Sublime Text.
   - Appuyez sur `Ctrl` + `Maj` + `B` (Windows/Linux) ou `Cmd` + `Maj` + `B` (Mac) pour ouvrir les commandes de compilation.
   - Sélectionnez l'une des commandes suivantes selon le script à exécuter :

        `tp_0_ins` : exécute tp_0_ins.py

        `tp_1_julia` : exécute tp_1_julia.py

        `tp_2_exos` : exécute tp_2_exos.py

        `tp_2_delaunay` : exécute tp_2_delaunay.py

        `tp_3_exo1` : exécute tp_3_exo1.py

        `tp_4_rendercube` : exécute tp_4_rendercube.py

        `tp_5_airplane` : exécute tp_5_airplane.py

        `tp_6_two-airplanes` : exécute tp_6_two-airplanes.py

2. **Sans Sublime Text (en utilisant le terminal)** :
    Vous pouvez également exécuter chaque script directement dans votre terminal. Pour chaque script, utilisez la commande suivante :
    
        python chemin_vers_le_script

    Exemple :

        python geometry_engine_executables/tp_0_ins.py


## Remarques

Ce projet utilise la bibliothèque `pygame` pour l'affichage. Assurez-vous d’avoir suivi les instructions d’installation à la racine du projet ([README.md](https://github.com/niloccolinus/geometry_engine/blob/main/README.md)) pour que toutes les dépendances soient disponibles.
