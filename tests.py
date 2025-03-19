import unittest

from bmi_calculator import (
    calculate_bmi,
    get_kg_from_pounds,
    get_meters_from_inches,
    split_height_string,
    return_bmi_category
)

class TestBMICalculator(unittest.TestCase):

    # Verify correct BMI calculation
    def test_calculate_bmi(self):
        self.assertAlmostEqual(calculate_bmi(1.75, 70), 22.86, places=2)
        self.assertAlmostEqual(calculate_bmi(1.6, 50), 19.53, places=2)
        self.assertAlmostEqual(calculate_bmi(1.8, 90), 27.78, places=2)

    # Verify correct conversion from pounds to kg
    def test_get_kg_from_pounds(self):
        self.assertAlmostEqual(get_kg_from_pounds(150), 68.04, places=2)
        self.assertAlmostEqual(get_kg_from_pounds(100), 45.36, places=2)
        self.assertAlmostEqual(get_kg_from_pounds(200), 90.72, places=2)

    # # Verify correct conversion from inches to meters
    def test_get_meters_from_inches(self):
        self.assertAlmostEqual(get_meters_from_inches(70), 1.78, places=2)
        self.assertAlmostEqual(get_meters_from_inches(60), 1.52, places=2)
        self.assertAlmostEqual(get_meters_from_inches(72), 1.83, places=2)
    
    # Verify correct splitting of height string
    def test_split_height_string(self):
        self.assertEqual(split_height_string("5'10\""), (5, 10))
        self.assertEqual(split_height_string("6'2\""), (6, 2))
        self.assertEqual(split_height_string("5'0\""), (5, 0))
        self.assertEqual(split_height_string("411"), (None))

    def test_return_bmi_category(self):
        # Near upper bound underweight
        self.assertEqual(return_bmi_category(18.4), "Underweight")
        # Lower bound normal weight
        self.assertEqual(return_bmi_category(18.5), "Normal weight")
        # Near upper bound normal weight
        self.assertEqual(return_bmi_category(24.9), "Normal weight")
        # Lower bound overweight
        self.assertEqual(return_bmi_category(25), "Overweight")
        # Near upper bound overweight
        self.assertEqual(return_bmi_category(29.9), "Overweight")
        # Lower bound obese
        self.assertEqual(return_bmi_category(30), "Obese")
        

if __name__ == "__main__":
    unittest.main()