import unittest
from health_utils import calculate_bmi, calculate_bmr

class TestHealthUtils(unittest.TestCase):

    def test_calculate_bmi(self):
        """Teste le calcul de l'IMC avec des entrées valides."""
        self.assertAlmostEqual(calculate_bmi(1.75, 70), 22.8571, places=4)
        self.assertAlmostEqual(calculate_bmi(1.60, 50), 19.5312, places=4)

    def test_calculate_bmr_male(self):
        """Teste le calcul du BMR pour les hommes avec des entrées valides."""
        self.assertAlmostEqual(calculate_bmr(180, 80, 30, 'male'), 1853.632, places=3)

    def test_calculate_bmr_female(self):
        """Teste le calcul du BMR pour les femmes avec des entrées valides."""
        self.assertAlmostEqual(calculate_bmr(165, 60, 30, 'female'), 1383.683, places=3)

    def test_calculate_bmr_invalid_gender(self):
        """Teste le calcul du BMR avec un genre invalide."""
        with self.assertRaises(ValueError):
            calculate_bmr(175, 70, 25, 'other')

if __name__ == '__main__':
    unittest.main()
