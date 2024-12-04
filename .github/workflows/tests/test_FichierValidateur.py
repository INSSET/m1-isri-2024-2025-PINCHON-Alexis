import pytest
import os
from app.lib.FichierVisiteur import FichierVisiteur

class TestFichierVisiteur:
    @pytest.fixture
    def fichier_temporaire(self, tmp_path):
        chemin = tmp_path / "visiteurs.json"
        return FichierVisiteur(str(chemin))

    def test_ajout_et_tout_lire(self, fichier_temporaire):
        visiteur = {"nom": "Jean", "prenom": "Marie"}
        fichier_temporaire.ajout(visiteur)
        contenu = fichier_temporaire.tout_lire()
        assert len(contenu) == 1
        assert contenu[0] == visiteur

    def test_tout_lire_fichier_vide(self, fichier_temporaire):
        assert fichier_temporaire.tout_lire() == []