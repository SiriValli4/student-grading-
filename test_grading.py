import unittest
from grading import calculate_grade

class TestGrading(unittest.TestCase):

    def test_valid_grades(self):
        self.assertEqual(calculate_grade(85), 'A')
        self.assertEqual(calculate_grade(70), 'B')
        self.assertEqual(calculate_grade(50), 'C')
        self.assertEqual(calculate_grade(20), 'F')

    def test_out_of_range_marks(self):
        with self.assertRaises(ValueError):
            calculate_grade(-5)
        with self.assertRaises(ValueError):
            calculate_grade(105)

if __name__ == '__main__':
    unittest.main()