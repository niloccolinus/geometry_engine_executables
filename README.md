# ⚙️ geometry_engine_executables

Ce répertoire contient les scripts exécutables et les interfaces de démonstration du moteur de géométrie.

## Description

`geometry_engine_executables` propose des exemples concrets d'utilisation de la bibliothèque `geometry_engine_librairie`. Ces scripts permettent de résoudre et de visualiser des exercices géométriques. À ce jour, plusieurs scripts sont disponibles, chacun ayant un objectif spécifique. 

### Comment lancer les scripts

1. **Avec Sublime Text (si vous utilisez ce programme)** :
   - Ouvrez le projet dans Sublime Text.
   - Appuyez sur `Ctrl` + `Maj` + `B` (Windows/Linux) ou `Cmd` + `Maj` + `B` (Mac) pour ouvrir les commandes de compilation.
   - Sélectionnez la commande correspondant au script que vous souhaitez exécuter.

2. **Sans Sublime Text (en utilisant le terminal)** :
    Vous pouvez également exécuter chaque script directement dans votre terminal. Pour chaque script, utilisez la commande suivante :
    
        python chemin_vers_le_script

    Exemple :

        python geometry_engine_executables/tp_0_ins.py

### Liste des scripts

1. **tp_0_ins.py** - Affiche un message "Hello World"

    Ce script est un simple exemple pour tester si l'environnement est correctement configuré. Il affiche "Hello World" dans le terminal.


2. **julia_viewer.py** - Visualisation de l'ensemble de Julia

    Ce script permet de visualiser l'ensemble de Julia, une structure fractale complexe. L'ensemble de Julia est généré en fonction d'un nombre complexe donné, et chaque pixel de l'écran est colorié en fonction de la divergence ou non de la suite complexe associée à ce pixel.


3. **tp_2_exos.py** - Résout et visualise plusieurs exercices géométriques

    Ce script résout et visualise un exercice de géométrie. 


## Dépendances

Ce projet utilise la bibliothèque pygame pour afficher les visualisations. Assurez-vous que cette bibliothèque est installée avant d'exécuter les scripts. Vous pouvez l'installer avec pip :

    pip install pygame
