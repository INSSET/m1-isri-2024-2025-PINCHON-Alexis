import pytest
from app.lib.Validateur import Validateur

class TestValidateur:
    @pytest.mark.parametrize("valeur, attendu", [
        ("Jean-Marie", True),
        ("Marie Anne", True),
        ("J", False),
        (" Jean", False),
        ("Marie-", False),
        ("a" * 61, False),
        ("Jean---Marie", True),
        ("Marie  Anne", True),
        ("Marie-Anne@", False)
    ])
    def test_valider_nom_prenom(self, valeur, attendu):
        assert Validateur.valider_nom_prenom(valeur) == attendu
