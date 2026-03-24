import argparse
import sys
import os
from analyser import extraire_stats
from rapport import generer_json
from archiver import archiver_logs, nettoyer_anciens_rapports, verifier_espace

def main():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    
    parser = argparse.ArgumentParser(description="LogAnalyzer Pro CLI")
    parser.add_argument("--source", required=True, help="Dossier des logs")
    parser.add_argument("--niveau", default="ALL", choices=["INFO", "WARN", "ERROR", "ALL"])
    parser.add_argument("--retention", type=int, default=30)
    args = parser.parse_args()

    try:
        print(f"--- Analyse des logs dans {args.source} ---")
        meta, stats, fichiers = extraire_stats(args.source, args.niveau)
        
        if not fichiers:
            print("Aucun fichier .log trouvé.")
            sys.exit(0)

        print("--- Génération du rapport ---")
        rep_dir = os.path.join(BASE_DIR, "rapports")
        chemin_rep = generer_json(meta, stats, fichiers, rep_dir)
        print(f"Rapport généré : {chemin_rep}")

        print("--- Archivage ---")
        back_dir = os.path.join(BASE_DIR, "backups")
        print(f"Espace disponible :\n{verifier_espace(BASE_DIR)}")
        arch_path = archiver_logs(fichiers, back_dir)
        print(f"Archive créée : {arch_path}")

        print("--- Nettoyage ---")
        nettoyer_anciens_rapports(rep_dir, args.retention)
        print("Opération terminée avec succès.")

    except Exception as e:
        print(f"ERREUR FATALE : {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()