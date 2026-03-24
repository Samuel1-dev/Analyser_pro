import os

def creer_fichiers_test():
    os.makedirs("logs_test", exist_ok=True)
    logs = [
        "2026-03-24 08:00:00 INFO Demarrage du service\n",
        "2026-03-24 08:05:00 ERROR Connexion echouee\n",
        "2026-03-24 08:10:00 WARN Memoire faible\n",
        "2026-03-24 08:15:00 ERROR Connexion echouee\n", # Doublon pour le Top 5
        "2026-03-24 08:20:00 ERROR Base de donnees hors ligne\n"
    ]
    
    for i in range(1, 4):
        with open(f"logs_test/app{i}.log", "w", encoding="utf-8") as f:
            f.writelines(logs * 5) # On répète pour avoir 25 lignes par fichier
    print("✅ Dossier 'logs_test' créé avec 3 fichiers .log")

if __name__ == "__main__":
    creer_fichiers_test()