import unittest
from unittest import TestCase
class Generated0Test(unittest.TestCase):

    def test_has_close_elements_positive_case(self):
        numbers = [1.0, 2.0, 3.0]
        threshold = 0.5
        self.assertTrue(has_close_elements(numbers, threshold))

    def test_has_close_elements_negative_case(self):
        numbers = [1.0, 2.0, 3.0]
        threshold = 0.1
        self.assertFalse(has_close_elements(numbers, threshold))

class Generated1Test(unittest.TestCase):

    def test_separate_paren_groups_empty_input(self):
        self.assertEqual(separate_paren_groups(''), [])

    def test_separate_paren_groups_single_group(self):
        self.assertEqual(separate_paren_groups('(abc)'), ['(abc)'])

    def test_separate_paren_groups_nested_groups(self):
        self.assertEqual(separate_paren_groups('(ab(cd)e(f(g)h))'), ['(ab(cd)e(f(g)h))'])

    def test_separate_paren_groups_multiple_groups(self):
        self.assertEqual(separate_paren_groups('(abc)(def)'), ['(abc)', '(def)'])

    def test_separate_paren_groups_no_parentheses(self):
        self.assertEqual(separate_paren_groups('abc'), [])
  



class Generated2Test(unittest.TestCase):
    def test_truncate_number(self):
        self.assertAlmostEqual(truncate_number(5.678), 0.678)
        self.assertAlmostEqual(truncate_number(10.0), 0.0)
        self.assertAlmostEqual(truncate_number(-3.14159), -0.14159)

class Generated3Test(unittest.TestCase):

    def test_below_zero_empty_list(self):
        self.assertFalse(below_zero([]))

    def test_below_zero_all_positive(self):
        self.assertFalse(below_zero([1, 2, 3]))

    def test_below_zero_all_negative(self):
        self.assertTrue(below_zero([-1, -2, -3]))

    def test_below_zero_mixed(self):
        self.assertTrue(below_zero([1, -2, 3, -4]))
class Generated4Test(unittest.TestCase):
    
    def test_mean_absolute_deviation_empty_list(self):
        self.assertEqual(mean_absolute_deviation([]), 0.0)
    
    def test_mean_absolute_deviation_single_element(self):
        self.assertEqual(mean_absolute_deviation([5]), 0.0)

    def test_mean_absolute_deviation_positive_numbers(self):
        self.assertEqual(mean_absolute_deviation([1, 2, 3, 4, 5]), 1.2)
    
    def test_mean_absolute_deviation_mixed_positive_negative_numbers(self):
        self.assertEqual(mean_absolute_deviation([-2, 0, 2]), 1.3333333333333333)
unittest
class Generated5Test(unittest.TestCase):

    def test_intersperse_empty_list(self):
        self.assertEqual(intersperse([], 5), [])
        
    def test_intersperse_single_element_list(self):
        self.assertEqual(intersperse([1], 5), [1])
        
    def test_intersperse_multiple_elements_list(self):
        self.assertEqual(intersperse([1, 2, 3, 4], 5), [1, 5, 2, 5, 3, 5, 4])

    def test_intersperse_negative_delimeter(self):
        self.assertEqual(intersperse([10, 20, 30], -1), [10, -1, 20, -1, 30])

    def test_intersperse_delimeter_as_zero(self):
        self.assertEqual(intersperse([4, 5, 6], 0), [4, 0, 5, 0, 6])
  



class Generated6Test(unittest.TestCase):

    def test_empty_input(self):
        self.assertEqual(parse_nested_parens(''), [])

    def test_single_paren_group(self):
        self.assertEqual(parse_nested_parens('(())'), [2])

    def test_multiple_paren_groups(self):
        self.assertEqual(parse_nested_parens('(()) () ((()))'), [2, 1, 3])

    def test_nested_paren_groups(self):
        self.assertEqual(parse_nested_parens('(()) (()) ((()))'), [2, 2, 3])

class Generated7Test(unittest.TestCase):

    def test_filter_by_substring_empty_list(self):
        self.assertEqual(filter_by_substring([], "test"), [])

    def test_filter_by_substring_no_matching_substring(self):
        self.assertEqual(filter_by_substring(["hello", "world"], "test"), [])

    def test_filter_by_substring_single_matching_substring(self):
        self.assertEqual(filter_by_substring(["hello", "test", "world"], "test"), ["test"])

    def test_filter_by_substring_multiple_matching_substrings(self):
        self.assertEqual(filter_by_substring(["hello", "test", "world", "testing"], "test"), ["test", "testing"])



class Generated8Test(unittest.TestCase):

    def test_sum_product(self):
        self.assertEqual(sum_product([1, 2, 3]), (6, 6))
        self.assertEqual(sum_product([-1, 2, -3]), (-2, 6))
        self.assertEqual(sum_product([0, 0, 0]), (0, 0))

class Generated9Test(unittest.TestCase):
    
    def test_rolling_max_running_max_is_none(self):
        self.assertEqual(rolling_max([3, 1, 4, 6, 2]), [3, 3, 4, 6, 6])

    def test_rolling_max_running_max_is_not_none(self):
        self.assertEqual(rolling_max([5, 2, 7, 4, 8]), [5, 5, 7, 7, 8])

    def test_rolling_max_empty_list(self):
        self.assertEqual(rolling_max([]), [])
