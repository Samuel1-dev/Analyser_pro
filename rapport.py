import json
import os
from datetime import datetime
from collections import Counter

def generer_json(metadata, stats, fichiers, dest_dir):
    """Crée le fichier JSON structuré."""
    os.makedirs(dest_dir, exist_ok=True)
    date_str = datetime.now().strftime("%Y-%m-%d")
    nom_fichier = f"rapport_{date_str}.json"
    chemin_complet = os.path.join(dest_dir, nom_fichier)

    data = {
        "metadata": {
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "utilisateur": metadata["utilisateur"],
            "os": metadata["os"],
            "source": metadata["source"]
        },
        "statistiques": {
            "total_lignes": stats["total_lignes"],
            "par_niveau": stats["par_niveau"],
            "top5_erreurs": [msg for msg, _ in Counter(stats["erreurs"]).most_common(5)] if "erreurs" in stats else []
        },
        "fichiers_traites": fichiers
    }

    with open(chemin_complet, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    
    return chemin_complet