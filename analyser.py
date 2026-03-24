import os
import glob
import platform
from collections import Counter

def extraire_stats(source_dir, niveau_filtre="ALL"):
    """Analyse les fichiers .log et retourne les statistiques."""
    fichiers = glob.glob(os.path.join(source_dir, "*.log"))
    stats = {"total_lignes": 0, "par_niveau": {"ERROR": 0, "WARN": 0, "INFO": 0}, "erreurs": []}
    fichiers_lus = []

    for fichier in fichiers:
        try:
            with open(fichier, 'r', encoding='utf-8') as f:
                fichiers_lus.append(os.path.abspath(fichier))
                for ligne in f:
                    stats["total_lignes"] += 1
                    parts = ligne.split(' ', 3)
                    if len(parts) < 4: continue
                    
                    lvl = parts[2]
                    msg = parts[3].strip()

                    if lvl in stats["par_niveau"]:
                        stats["par_niveau"][lvl] += 1
                    
                    if lvl == "ERROR":
                        stats["erreurs"].append(msg)
        except Exception as e:
            print(f"Erreur lors de la lecture de {fichier}: {e}")

    # Top 5 erreurs
    top5 = [msg for msg, count in Counter(stats["erreurs"]).most_common(5)]
    
    metadata = {
        "utilisateur": os.environ.get('USER') or os.environ.get('USERNAME'),
        "os": platform.system(),
        "source": os.path.abspath(source_dir)
    }
    
    return metadata, stats, fichiers_lus