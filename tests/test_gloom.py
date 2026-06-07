import unittest
from logic.london_gloom import evaluate_vibe


class TestLondonGloom(unittest.TestCase):

    def test_maximum_edgy_depression(self):
        """Testuje absolutny kryzys: deszcz i brak herbaty."""
        wynik = evaluate_vibe(weather="heavy rain", tea_status="none", pocket_money_pounds=10.0)
        self.assertIn("Mroczna otchłań", wynik)
        self.assertIn("The Smiths", wynik)

    def test_tesco_financial_ruin(self):
        """Testuje brak funduszy na chipsy z Tesco."""
        wynik = evaluate_vibe(weather="grey", tea_status="jest", pocket_money_pounds=0.50)
        self.assertIn("Tesco", wynik)
        self.assertIn("shambles", wynik)

    def test_ruined_by_sunlight(self):
        """Testuje, czy słońce niszczy edgy klimat."""
        wynik = evaluate_vibe(weather="sunny days", tea_status="jest", pocket_money_pounds=5.0)
        self.assertIn("Obrzydliwe", wynik)


if __name__ == "__main__":
    unittest.main()
