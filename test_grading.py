import unittest
from grading import calculate_grade, process_student_records

class TestGradingBoundaries(unittest.TestCase):

    def test_boundary_values(self):
        # Boundary tests for grade rules:
        # 0 <= m < 40  -> F
        # 40 <= m < 60 -> C  (so 40 and 59, 60 are C)
        # 60 < m < 80  -> B  (so 61 and 79 are B)
        # 80 <= m <= 100 -> A (so 80 and 100 are A)
        self.assertEqual(calculate_grade(39), 'F')
        self.assertEqual(calculate_grade(40), 'C')
        self.assertEqual(calculate_grade(59), 'C')
        self.assertEqual(calculate_grade(60), 'C')   # 60 is C because 60 < m < 80 for B!
        self.assertEqual(calculate_grade(61), 'B')   # > 60 gets B
        self.assertEqual(calculate_grade(79), 'B')
        self.assertEqual(calculate_grade(80), 'A')
        self.assertEqual(calculate_grade(100), 'A')

    def test_invalid_marks(self):
        # Out-of-bounds inputs
        with self.assertRaises(ValueError):
            calculate_grade(-1)
        with self.assertRaises(ValueError):
            calculate_grade(101)

    def test_malformed_inputs(self):
        # Non-numeric string input
        with self.assertRaises(ValueError):
            calculate_grade("abc")

if __name__ == '__main__':
    unittest.main()