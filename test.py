import unittest
from health_utils import calculate_bmi, calculate_bmr

class TestHealthUtils(unittest.TestCase):

    def test_calculate_bmi(self):
        """Test the BMI calculation with valid inputs."""
        self.assertAlmostEqual(calculate_bmi(1.75, 70), 22.8571, places=4)
        self.assertAlmostEqual(calculate_bmi(1.60, 50), 19.5312, places=4)

    def test_calculate_bmr_male(self):
        """Test the BMR calculation for males with valid inputs."""
        self.assertAlmostEqual(calculate_bmr(180, 80, 30, 'male'), 1853.632, places=3)

    def test_calculate_bmr_female(self):
        """Test the BMR calculation for females with valid inputs."""
        self.assertAlmostEqual(calculate_bmr(165, 60, 30, 'female'), 1383.683, places=3)

    def test_calculate_bmr_invalid_gender(self):
        """Test the BMR calculation with an invalid gender."""
        with self.assertRaises(ValueError):
            calculate_bmr(175, 70, 25, 'other')

if __name__ == '__main__':
    unittest.main()
