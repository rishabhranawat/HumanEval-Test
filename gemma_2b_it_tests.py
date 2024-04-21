import unittest

class ZeroTest(unittest.TestCase):

    def test_has_close_elements(self):
        self.assertEqual(has_close_elements([1.0, 2.0, 3.0], 0.5), False)
        self.assertEqual(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3), True)
        self.assertEqual(has_close_elements([1.0, 2.0, 3.0], 1.0), False)
        self.assertEqual(has_close_elements([1.0, 2.0, 3.0], 0.0), False)

# Path: gemma_2b_it_tests.py