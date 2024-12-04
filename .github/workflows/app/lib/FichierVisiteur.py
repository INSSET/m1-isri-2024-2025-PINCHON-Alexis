import json

class FichierVisiteur:
    def __init__(self, chemin_fichier: str):
        self.chemin_fichier = chemin_fichier

    def ajout(self, visiteur: dict):
        visiteurs = self.tout_lire()
        visiteurs.append(visiteur)
        with open(self.chemin_fichier, 'w') as fichier:
            json.dump(visiteurs, fichier)

    def tout_lire(self):
        try:
            with open(self.chemin_fichier, 'r') as fichier:
                return json.load(fichier)
        except FileNotFoundError:
            return []