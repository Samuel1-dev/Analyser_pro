1. Description du projet et objectif

LogAnalyzer Pro est un outil en ligne de commande (CLI) conçu pour automatiser la gestion des fichiers de logs applicatifs. Dans un contexte DevOps, cet outil permet de surveiller la santé des services en filtrant les erreurs, en générant des rapports statistiques structurés au format JSON, et en assurant la maintenance du stockage via l'archivage compressé et le nettoyage automatique des anciens rapports.

Objectifs principaux :

    Extraire des statistiques pertinentes des fichiers .log.

    Centraliser les métadonnées système (OS, Utilisateur) et les erreurs critiques.

    Optimiser l'espace disque par la compression .tar.gz.

    Automatiser la rétention des données pour éviter la saturation du serveur.

2. Prérequis et installation

    Version Python : Python 3.8 

    Dépendances : Aucune. Ce projet utilise exclusivement la bibliothèque standard de Python (zéro installation pip requise).

Installation :

    Clonez le dossier du projet.

    Donnez les droits d'exécution au script principal :
    Bash

    chmod +x main.py

3. Utilisation

Le script se lance via le terminal avec différents arguments pour personnaliser le traitement.
Syntaxe de base :
Bash

python main.py --source /chemin/vers/logs [OPTIONS]

Exemples de commandes :

    Analyse complète avec rétention par défaut (30 jours) : 
    python main.py --source ./logs_test --niveau ALL


    Filtrage uniquement sur les erreurs avec une rétention de 7 jours :
    python main.py --source ./logs_test --niveau ERROR --retention 7

Arguments disponibles :

Argument	Description	Obligatoire	Défaut
--source	Chemin vers le dossier contenant les fichiers .log	obligatoire
--niveau	Niveau de filtrage (INFO, WARN, ERROR, ALL)	Non obligatoire ALL par defaut
--retention	Nombre de jours avant suppression des anciens rapports	Non obligatoire	30 par defaut

4. Description des modules

Le projet est découpé en 4 modules spécialisés pour garantir une maintenance facile :

    analyser.py (Module 1) : Responsable du scan des fichiers via glob. Il parse les lignes de log, filtre selon le niveau choisi et calcule les statistiques (Top 5 erreurs, comptage).

    rapport.py (Module 2) : Transforme les données analysées en un fichier JSON horodaté. Il récupère les métadonnées système (platform, os.environ) et assure la structure stricte du rapport.

    archiver.py (Module 3) : Gère les opérations système lourdes. Il vérifie l'espace disque disponible (subprocess), compresse les logs traités (tarfile) et nettoie les fichiers JSON obsolètes.

    main.py (Module 4) : Point d'entrée du programme. Il gère les arguments CLI (argparse), orchestre l'exécution des modules et intercepte les erreurs pour garantir la robustesse de l'outil.

5. Planification Hebdomadaire (Cron)

Pour exécuter l'outil automatiquement tous les dimanches à 03h00, ajoutez la ligne suivante à votre configuration cron (crontab -e) :
Bash

0 3 * * 0 /usr/bin/python3 /home/USER/loganalyzer/main.py --source /home/USER/logs --dest /home/USER/backups

Explication de la ligne :

    0 3 : Déclenchement à la minute 0 de la 3ème heure (03:00 du matin).

    * * : Tous les jours du mois et tous les mois.

    0 : Uniquement le dimanche (Sunday).

    Chemins absolus : L'utilisation de chemins complets est impérative car Cron s'exécute dans un environnement restreint.
