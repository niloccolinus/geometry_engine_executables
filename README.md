# ⚙️ geometry_engine_executables

Ce répertoire contient les scripts exécutables et les interfaces de démonstration du moteur de géométrie.

## Description

`geometry_engine_executables` propose des exemples concrets d'utilisation de la bibliothèque `geometry_engine_librairie`. Ces scripts permettent de résoudre et de visualiser des exercices géométriques. À ce jour, plusieurs scripts sont disponibles, chacun ayant un objectif spécifique. 


### Liste des scripts

1. **tp_0_ins.py** - Affiche un message "Hello World"

    Ce script est un simple exemple pour tester si l'environnement est correctement configuré. Il affiche "Hello World" dans le terminal.


2. **julia_viewer.py** - Visualisation de l'ensemble de Julia

    Ce script permet de visualiser l'ensemble de Julia, une structure fractale complexe. L'ensemble de Julia est généré en fonction d'un nombre complexe donné, et chaque pixel de l'écran est colorié en fonction de la divergence ou non de la suite complexe associée à ce pixel.


3. **tp_2_exos.py** - Résout et visualise plusieurs exercices géométriques

    Ce script résout et visualise un exercice de géométrie. 

4. **tp_2_3_delaunay.py** - Calcule et visualise une triangulation de Delaunay

    Ce script calcule la triangulation de Delaunay d'un ensemble de points aléatoires dans un plan. Il utilise l'algorithme de Bowyer-Watson pour construire la triangulation.

### Comment lancer les scripts

1. **Avec Sublime Text (si vous utilisez ce programme)** :
   - Ouvrez le projet dans Sublime Text.
   - Appuyez sur `Ctrl` + `Maj` + `B` (Windows/Linux) ou `Cmd` + `Maj` + `B` (Mac) pour ouvrir les commandes de compilation.
   - Sélectionnez l'une des commandes suivantes selon le script à exécuter :

        `hello_world_build` : exécute tp_0_ins.py

        `run_julia_viewer` : exécute julia_viewer.py

        `solve_exercises` : exécute tp_2_exos.py

        `delaunay_triangulation` : exécute tp_2_3_delaunay.py

2. **Sans Sublime Text (en utilisant le terminal)** :
    Vous pouvez également exécuter chaque script directement dans votre terminal. Pour chaque script, utilisez la commande suivante :
    
        python chemin_vers_le_script

    Exemple :

        python geometry_engine_executables/tp_0_ins.py


## Remarques

Ce projet utilise la bibliothèque `pygame` pour l'affichage. Assurez-vous d’avoir suivi les instructions d’installation à la racine du projet ([README.md](../README.md)) pour que toutes les dépendances soient disponibles.
