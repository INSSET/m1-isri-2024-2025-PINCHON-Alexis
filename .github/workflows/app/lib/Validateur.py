import re

class Validateur:
    @staticmethod
    def valider_nom_prenom(valeur: str) -> bool:

        if not (2 <= len(valeur) <= 60):
            return False
        if valeur.startswith(("-", " ")) or valeur.endswith(("-", " ")):
            return False
        if valeur.count('-') > 5 or valeur.count(' ') > 5:
            return False
        if not re.match(r'^[a-zA-Z\s\-]+$', valeur):
            return False
        return True