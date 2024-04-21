
import unittest

class ZeroTest(unittest.TestCase):

    def test_has_close_elements_empty_list(self):
        self.assertFalse(has_close_elements([], 1.0))

    def test_has_close_elements_no_close_elements(self):
        self.assertFalse(has_close_elements([1.0, 2.0, 3.0], 0.5))

    def test_has_close_elements_close_elements(self):
        self.assertTrue(has_close_elements([1.0, 2.0, 2.5, 3.0], 0.6))

    def test_has_close_elements_identical_elements(self):
        self.assertFalse(has_close_elements([1.0, 1.0, 1.0], 0.1))


    
  
class OneTest:

    def test_separate_paren_groups(self):
        self.assertEqual(separate_paren_groups("()"), ["()"])
        self.assertEqual(separate_paren_groups("(())"), ["(())"])
        self.assertEqual(separate_paren_groups("()()"), ["()", "()"])
        self.assertEqual(separate_paren_groups("((()))"), ["((()))"])
        self.assertEqual(separate_paren_groups("(())()"), ["(())", "()"])
        self.assertEqual(separate_paren_groups("((()()))()"), ["((()()))","()"])
 
import unittest

class TwoTest(unittest.TestCase):
    def test_truncate_number_positive_integer(self):
        self.assertEqual(truncate_number(5), 0.0)

    def test_truncate_number_positive_float(self):
        self.assertEqual(truncate_number(3.14), 0.14000000000000012)

    def test_truncate_number_negative_integer(self):
        self.assertEqual(truncate_number(-7), 0.0)

    def test_truncate_number_negative_float(self):
        self.assertEqual(truncate_number(-2.71828), 0.2817199999999998)


    
  
class ThreeTest(unittest.TestCase):

    def test_below_zero_empty_list(self):
        self.assertFalse(below_zero([]))

    def test_below_zero_positive_numbers(self):
        self.assertFalse(below_zero([1, 2, 3]))

    def test_below_zero_negative_numbers(self):
        self.assertTrue(below_zero([-1, -2, -3]))

    def test_below_zero_mixed_numbers(self):
        self.assertTrue(below_zero([1, -2, 3, -4]))

    def test_below_zero_zero_balance(self):
        self.assertFalse(below_zero([5, -5]))

    def test_below_zero_single_negative(self):
        self.assertTrue(below_zero([-10]))

class FourTest(unittest.TestCase):

    def test_mean_absolute_deviation_empty_list(self):
        self.assertEqual(mean_absolute_deviation([]), 0.0)

    def test_mean_absolute_deviation_single_element(self):
        self.assertEqual(mean_absolute_deviation([5.0]), 0.0)

    def test_mean_absolute_deviation_positive_numbers(self):
        self.assertEqual(mean_absolute_deviation([1.5, 2.5, 3.5, 4.5]), 1.0)

    def test_mean_absolute_deviation_mixed_numbers(self):
        self.assertEqual(mean_absolute_deviation([-1, 0, 1]), 0.6666666666666666)

