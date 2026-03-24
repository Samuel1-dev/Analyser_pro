import os
import tarfile
import shutil
import time
import subprocess

def verifier_espace(chemin):
    """Vérifie l'espace disque via subprocess (df)."""
    res = subprocess.run(['df', '-h', chemin], capture_output=True, text=True)
    return res.stdout

def archiver_logs(fichiers, dest_backups):
    """Archive les fichiers .log en .tar.gz."""
    os.makedirs(dest_backups, exist_ok=True)
    date_str = time.strftime("%Y-%m-%d")
    nom_archive = os.path.join(dest_backups, f"backup_{date_str}.tar.gz")
    
    with tarfile.open(nom_archive, "w:gz") as tar:
        for f in fichiers:
            tar.add(f, arcname=os.path.basename(f))
    return nom_archive

def nettoyer_anciens_rapports(dossier_rapports, jours_retention):
    """Supprime les fichiers JSON trop vieux."""
    seuil = time.time() - (jours_retention * 86400)
    for f in os.listdir(dossier_rapports):
        chemin = os.path.join(dossier_rapports, f)
        if os.path.isfile(chemin) and os.path.getmtime(chemin) < seuil:
            os.remove(chemin)