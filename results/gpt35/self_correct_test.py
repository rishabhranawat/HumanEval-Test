import unittest
from unittest import TestCase
class Generated0Test(unittest.TestCase):
    def test_has_close_elements_true(self):
        self.assertTrue(has_close_elements([1.0, 2.0, 3.0], 1.5))

    def test_has_close_elements_false(self):
        self.assertFalse(has_close_elements([1.0, 2.0, 3.0], 0.5))

    def test_has_close_elements_empty_list(self):
        self.assertFalse(has_close_elements([], 1.0))
class Generated1Test(unittest.TestCase):
    
    def test_separate_paren_groups_empty(self):
        paren_string = ""
        self.assertEqual(separate_paren_groups(paren_string), [])
        
    def test_separate_paren_groups_single_group(self):
        paren_string = "(abc)"
        self.assertEqual(separate_paren_groups(paren_string), ["(abc)"])
        
    def test_separate_paren_groups_nested_groups(self):
        paren_string = "(abc(def)ghi(jkl))"
        self.assertEqual(separate_paren_groups(paren_string), ["(abc(def)ghi(jkl))"])
        
    def test_separate_paren_groups_multiple_groups(self):
        paren_string = "(abc)(def)(ghi)"
        self.assertEqual(separate_paren_groups(paren_string), ["(abc)", "(def)", "(ghi)"])
class Generated2Test(unittest.TestCase):
    def test_truncate_number(self):
        self.assertAlmostEqual(truncate_number(3.14), 0.14000000000000012)
        self.assertAlmostEqual(truncate_number(10.5), 0.5)
        self.assertAlmostEqual(truncate_number(7.0), 0.0)
class Generated3Test(unittest.TestCase):

    def test_below_zero_balance_less_than_zero(self):
        self.assertTrue(below_zero([-1, -2, 3, -4]))

    def test_below_zero_balance_greater_than_zero(self):
        self.assertFalse(below_zero([2, 3, 1, -5]))

    def test_below_zero_empty_operations(self):
        self.assertFalse(below_zero([]))

    def test_below_zero_single_operation_balance_zero(self):
        self.assertFalse(below_zero([0]))

    def test_below_zero_single_operation_balance_negative(self):
        self.assertTrue(below_zero([-3]))




class Generated4Test(unittest.TestCase):

    def test_mean_absolute_deviation_empty_list(self):
        self.assertEqual(mean_absolute_deviation([]), 0.0)

    def test_mean_absolute_deviation_single_element(self):
        self.assertEqual(mean_absolute_deviation([5.0]), 0.0)

    def test_mean_absolute_deviation_positive_numbers(self):
        self.assertEqual(mean_absolute_deviation([1.0, 2.0, 3.0, 4.0, 5.0]), 1.0)

    def test_mean_absolute_deviation_negative_numbers(self):
        self.assertEqual(mean_absolute_deviation([-1.0, -2.0, -3.0, -4.0, -5.0]), 1.0)

    def test_mean_absolute_deviation_mixed_numbers(self):
        self.assertEqual(mean_absolute_deviation([-1.0, 2.0, -3.0, 4.0, -5.0]), 2.4)

    def test_mean_absolute_deviation_float_numbers(self):
        self.assertAlmostEqual(mean_absolute_deviation([1.1, 2.2, 3.3, 4.4, 5.5]), 1.46, places=2)

  
unittest
class Generated5Test(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(intersperse([], 5), [])

    def test_single_element_list(self):
        self.assertEqual(intersperse([1], 5), [1])

    def test_multiple_elements_list(self):
        self.assertEqual(intersperse([1, 2, 3, 4], 5), [1, 5, 2, 5, 3, 5, 4])

    def test_delerimeter_included_at_end(self):
        self.assertEqual(intersperse([1, 2, 3], 5), [1, 5, 2, 5, 3])






class Generated6Test(unittest.TestCase):

    def test_parse_nested_parens(self):
        self.assertEqual(parse_nested_parens('() ((()) ())'), [1, 2, 1])

    def test_empty_string(self):
        self.assertEqual(parse_nested_parens(''), [])

    def test_no_parentheses(self):
        self.assertEqual(parse_nested_parens('abc def ghi'), [])

    def test_single_close_parenthesis(self):
        self.assertEqual(parse_nested_parens(') ( ) ) ( ( ( ) ) )'), [1, 1, 0, 2])

    def test_deep_nesting(self):
        self.assertEqual(parse_nested_parens('( ( ( ( ( ( ) ) ) ) ) ) ( ( ( ) ) )'), [6, 2])

    def test_mixed_characters(self):
        self.assertEqual(parse_nested_parens('a ( b ( c d ) e f ) g'), [1, 2])
  

class Generated7Test(unittest.TestCase):
    
    def test_filter_by_substring(self):
        strings = ['apple', 'banana', 'cherry', 'orange']
        self.assertEqual(filter_by_substring(strings, 'a'), ['apple', 'banana', 'orange'])
        
        strings = ['cat', 'dog', 'elephant', 'horse']
        self.assertEqual(filter_by_substring(strings, 'o'), ['dog', 'horse'])

        strings = ['red', 'green', 'blue', 'yellow']
        self.assertEqual(filter_by_substring(strings, 'l'), ['yellow'])

class Generated8Test(unittest.TestCase):
    def test_sum_product_positive_numbers(self):
        self.assertEqual(sum_product([1, 2, 3, 4]), (10, 24))
    
    def test_sum_product_negative_numbers(self):
        self.assertEqual(sum_product([-1, -2, -3]), (-6, -6))
    
    def test_sum_product_mixed_numbers(self):
        self.assertEqual(sum_product([2, -3, 4, -5]), (-2, 120))
    
    def test_sum_product_empty_list(self):
        self.assertEqual(sum_product([]), (0, 1))
class Generated9Test(unittest.TestCase):

    def test_rolling_max(self):
        self.assertEqual(rolling_max([1, 2, 3, 4]), [1, 2, 3, 4])
        self.assertEqual(rolling_max([4, 3, 2, 1]), [4, 4, 4, 4])
        self.assertEqual(rolling_max([50, 20, 70, 45, 30]), [50, 50, 70, 70, 70])
        self.assertEqual(rolling_max([10, 5, 8, 12, 15]), [10, 10, 10, 12, 15])
        self.assertEqual(rolling_max([67]), [67])
class Generated10Test(unittest.TestCase):
    def test_is_palindrome(self):
        self.assertTrue(is_palindrome("level"))
        self.assertTrue(is_palindrome("radar"))
        self.assertTrue(is_palindrome("Able was I ere I saw Elba"))
        self.assertTrue(is_palindrome(""))

    def test_make_palindrome(self):
        self.assertEqual(make_palindrome("radar"), "radar")
        self.assertEqual(make_palindrome("race"), "racecar")
        self.assertEqual(make_palindrome(""), "")
        self.assertEqual(make_palindrome("ab"), "aba")
class Generated11Test(unittest.TestCase):
    def test_string_xor_equal_length(self):
        self.assertEqual(string_xor('1101', '1010'), '0111')
    
    def test_string_xor_different_length(self):
        self.assertEqual(string_xor('1101', '10'), '011')
    
    def test_string_xor_empty_string(self):
        self.assertEqual(string_xor('', ''), '')
class Generated12Test(unittest.TestCase):
    
    def test_empty_list(self):
        self.assertIsNone(longest([]))

    def test_single_string(self):
        self.assertEqual(longest(['abc']), 'abc')

    def test_multiple_strings(self):
        self.assertEqual(longest(['a', 'abc', 'abcd', 'ab']), 'abcd')

    def test_equal_length_strings(self):
        self.assertEqual(longest(['apple', 'banana', 'cherry']), 'banana')



class Generated13Test(unittest.TestCase):

    def test_greatest_common_divisor_positive_numbers(self):
        self.assertEqual(greatest_common_divisor(12, 8), 4)

    def test_greatest_common_divisor_negative_numbers(self):
        self.assertEqual(greatest_common_divisor(-5, -10), 5)
    
    def test_greatest_common_divisor_zero(self):
        self.assertEqual(greatest_common_divisor(0, 5), 5)

    def test_greatest_common_divisor_same_number(self):
        self.assertEqual(greatest_common_divisor(75, 75), 75)
  

class Generated14Test(unittest.TestCase):

    def test_all_prefixes_empty_string(self):
        self.assertEqual(all_prefixes(""), [])

    def test_all_prefixes_single_character_string(self):
        self.assertEqual(all_prefixes("a"), ["a"])

    def test_all_prefixes_multiple_character_string(self):
        self.assertEqual(all_prefixes("hello"), ["h", "he", "hel", "hell", "hello"])

class Generated15Test(unittest.TestCase):
    def test_string_sequence(self):
        self.assertEqual(string_sequence(0), "0")
        self.assertEqual(string_sequence(5), "0 1 2 3 4 5")



class Generated16Test(unittest.TestCase):

    def test_count_distinct_characters_empty_string(self):
        self.assertEqual(count_distinct_characters(""), 0)

    def test_count_distinct_characters_all_same_characters(self):
        self.assertEqual(count_distinct_characters("aaaaa"), 1)

    def test_count_distinct_characters_mixed_characters(self):
        self.assertEqual(count_distinct_characters("helLoWorLD"), 8)

    def test_count_distinct_characters_special_characters(self):
        self.assertEqual(count_distinct_characters("!@#$%^&*()"), 9)

class Generated17Test(unittest.TestCase):
    def test_parse_music(self):
        self.assertEqual(parse_music("o o| o .|"), [4, 2, 4, 1])
        self.assertEqual(parse_music(""), [])
        self.assertEqual(parse_music("o"), [4])
class Generated18Test(unittest.TestCase):
    
    def test_how_many_times_when_substring_occurs_multiple_times(self):
        self.assertEqual(how_many_times("hello hello hello", "hello"), 3)
    
    def test_how_many_times_when_substring_not_present(self):
        self.assertEqual(how_many_times("hello world", "apple"), 0)
    
    def test_how_many_times_when_substring_is_empty_string(self):
        self.assertEqual(how_many_times("test", ""), 5)
class Generated19Test(unittest.TestCase):

    def test_sort_numbers(self):
        self.assertEqual(sort_numbers('one six four two'), 'one two four six')

    def test_sort_numbers_empty_string(self):
        self.assertEqual(sort_numbers(''), '')

    def test_sort_numbers_already_sorted(self):
        self.assertEqual(sort_numbers('zero one two three'), 'zero one two three')

    def test_sort_numbers_reverse_sorted(self):
        self.assertEqual(sort_numbers('three two one zero'), 'zero one two three')

    def test_sort_numbers_duplicate_numbers(self):
        self.assertEqual(sort_numbers('one one two two three three'), 'one one two two three three')
