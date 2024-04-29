import unittest

class ZeroTest(unittest.TestCase):

    def test_has_close_elements_empty_list(self):
        self.assertFalse(has_close_elements([], 0.5))

    def test_has_close_elements_no_close_elements(self):
        self.assertFalse(has_close_elements([1.0, 2.0, 3.0, 4.0], 0.5))

    def test_has_close_elements_close_elements(self):
        self.assertTrue(has_close_elements([1.0, 1.5, 3.0, 4.0], 0.5))

    def test_has_close_elements_same_element(self):
        self.assertTrue(has_close_elements([1.0, 1.0, 3.0, 4.0], 0.5))

    def test_has_close_elements_negative_threshold(self):
        self.assertFalse(has_close_elements([1.0, 2.0, 3.0, 4.0], -1.0))

    def test_has_close_elements_threshold_zero(self):
        self.assertFalse(has_close_elements([1.0, 2.0, 3.0, 4.0], 0.0))
class OneTest(unittest.TestCase):

    def test_separate_paren_groups_empty_string(self):
        self.assertEqual(separate_paren_groups(''), [])

    def test_separate_paren_groups_no_parentheses(self):
        self.assertEqual(separate_paren_groups('abc'), [])

    def test_separate_paren_groups_single_group(self):
        self.assertEqual(separate_paren_groups('(abc)'), ['(abc)'])

    def test_separate_paren_groups_multiple_groups(self):
        self.assertEqual(separate_paren_groups('(abc)def(ghi)'), ['(abc)', '(ghi)'])

    def test_separate_paren_groups_nested_groups(self):
        self.assertEqual(separate_paren_groups('(a(b)c(d(e)f)g)h'), ['(a(b)c(d(e)f)g)'])

    def test_separate_paren_groups_no_closing_paren(self):
        self.assertEqual(separate_paren_groups('(abc'), [])

    def test_separate_paren_groups_no_opening_paren(self):
        self.assertEqual(separate_paren_groups('abc)'), [])
class TwoTest(unittest.TestCase):

    def test_truncate_number_integer(self):
        self.assertEqual(truncate_number(5), 0.0)

    def test_truncate_number_float(self):
        self.assertEqual(truncate_number(3.14), 0.14000000000000012)

    def test_truncate_number_negative(self):
        self.assertEqual(truncate_number(-7.5), 0.5)

    def test_truncate_number_large(self):
        self.assertEqual(truncate_number(123456789.987654321), 0.987654321)



class ThreeTest(unittest.TestCase):

    def test_below_zero_empty_list(self):
        self.assertFalse(below_zero([]))

    def test_below_zero_positive_operations(self):
        self.assertFalse(below_zero([1, 2, 3]))

    def test_below_zero_negative_operation(self):
        self.assertTrue(below_zero([-1, -2, -3, 4, 5]))

    def test_below_zero_mixed_operations(self):
        self.assertTrue(below_zero([1, -2, 3, -4, 5]))


    




class FourTest(unittest.TestCase):

    def test_mean_absolute_deviation_empty_list(self):
        self.assertEqual(mean_absolute_deviation([]), 0.0)

    def test_mean_absolute_deviation_single_element_list(self):
        self.assertEqual(mean_absolute_deviation([5.0]), 0.0)

    def test_mean_absolute_deviation_list_with_positive_numbers(self):
        self.assertAlmostEqual(mean_absolute_deviation([1.0, 2.0, 3.0, 4.0, 5.0]), 1.2)

    def test_mean_absolute_deviation_list_with_negative_numbers(self):
        self.assertAlmostEqual(mean_absolute_deviation([-1.0, -2.0, -3.0, -4.0, -5.0]), 1.2)

    def test_mean_absolute_deviation_mixed_list(self):
        self.assertAlmostEqual(mean_absolute_deviation([-1.0, 2.0, -3.0, 4.0, -5.0]), 2.4)


    
  
class FiveTest(unittest.TestCase):

    def test_intersperse_empty_list(self):
        self.assertEqual(intersperse([], 5), [])

    def test_intersperse_single_element(self):
        self.assertEqual(intersperse([1], 5), [1])

    def test_intersperse_multiple_elements(self):
        self.assertEqual(intersperse([1, 2, 3], 5), [1, 5, 2, 5, 3])
unittest
class SixTest(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(parse_nested_parens(''), [])

    def test_single_group(self):
        self.assertEqual(parse_nested_parens('(())'), [2])

    def test_multiple_groups(self):
        self.assertEqual(parse_nested_parens('(()) ()(((())) ())(())'), [2, 1, 3, 2])

    def test_no_groups(self):
        self.assertEqual(parse_nested_parens('word'), [])

    def test_mixed_input(self):
        self.assertEqual(parse_nested_parens('(()) word ()(((()))  () ())(())'), [2, 3, 1, 2])





class SevenTest(unittest.TestCase):

    def test_filter_by_substring_empty_input(self):
        self.assertEqual(filter_by_substring([], "test"), [])
        
    def test_filter_by_substring_no_matching_substring(self):
        self.assertEqual(filter_by_substring(["hello", "world", "python"], "test"), [])
        
    def test_filter_by_substring_single_matching_substring(self):
        self.assertEqual(filter_by_substring(["apple", "banana", "orange"], "apple"), ["apple"])
        
    def test_filter_by_substring_multiple_matching_substrings(self):
        self.assertEqual(filter_by_substring(["cat", "dog", "cow", "bat"], "at"), ["cat", "bat"])
        
    def test_filter_by_substring_all_matching_substrings(self):
        self.assertEqual(filter_by_substring(["apple", "banana", "orange"], "a"), ["apple", "banana", "orange"])
  
class EightTest(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(sum_product([]), (0, 1))

    def test_single_element_list(self):
        self.assertEqual(sum_product([8]), (8, 8))

    def test_positive_numbers_list(self):
        self.assertEqual(sum_product([1, 2, 3, 4]), (10, 24))

    def test_negative_numbers_list(self):
        self.assertEqual(sum_product([-1, -2, -3, -4]), (-10, -24))

    def test_mixed_numbers_list(self):
        self.assertEqual(sum_product([-1, 2, -3, 4]), (2, 24))

                         
class NineTest(unittest.TestCase):

    def test_rolling_max_empty_list(self):
        self.assertEqual(rolling_max([]), [])

    def test_rolling_max_single_element(self):
        self.assertEqual(rolling_max([5]), [5])

    def test_rolling_max_general_case(self):
        self.assertEqual(rolling_max([1, 3, 5, 2, 7, 4]), [1, 3, 5, 5, 7, 7])

    def test_rolling_max_negative_numbers(self):
        self.assertEqual(rolling_max([-2, 5, -3, 8, -1]), [-2, 5, 5, 8, 8])

    def test_rolling_max_duplicates(self):
        self.assertEqual(rolling_max([2, 2, 2, 2, 2]), [2, 2, 2, 2, 2])

    def test_rolling_max_all_equal(self):
        self.assertEqual(rolling_max([1, 1, 1, 1, 1]), [1, 1, 1, 1, 1])





class TenTest(unittest.TestCase):

    def test_is_palindrome(self):
        self.assertTrue(is_palindrome('racecar'))
        self.assertTrue(is_palindrome('level'))
        self.assertTrue(is_palindrome('deified'))
        self.assertTrue(is_palindrome('radar'))
        self.assertFalse(is_palindrome('hello'))
        self.assertFalse(is_palindrome('python'))
        self.assertFalse(is_palindrome('world'))

    def test_make_palindrome(self):
        self.assertEqual(make_palindrome('race'), 'racecar')
        self.assertEqual(make_palindrome('level'), 'level')
        self.assertEqual(make_palindrome('hello'), 'helloolleh')
        self.assertEqual(make_palindrome('python'), 'pythonohtyp')
        self.assertEqual(make_palindrome('test'), 'testset')


    

class ElevenTest(unittest.TestCase):

    def test_string_xor_equal_strings(self):
        self.assertEqual(string_xor('1111', '1111'), '0000')

    def test_string_xor_different_strings(self):
        self.assertEqual(string_xor('1010', '1100'), '0110')

    def test_string_xor_empty_strings(self):
        self.assertEqual(string_xor('', ''), '')

    def test_string_xor_unequal_length_strings(self):
        self.assertEqual(string_xor('1010', '110'), '')

    def test_string_xor_longer_first_string(self):
        self.assertEqual(string_xor('1010101', '111'), '0101010')

    def test_string_xor_longer_second_string(self):
        self.assertEqual(string_xor('11', '1010101'), '1000101')


from typing import List, Optional


def longest(strings: List[str]) -> Optional[str]:

    if not strings:
        return None

    maxlen = max(len(x) for x in strings)
    for s in strings:
        if len(s) == maxlen:
            return s


class TwelveTest(unittest.TestCase):

    def test_empty_list(self):
        self.assertIsNone(longest([]))

    def test_single_item(self):
        self.assertEqual(longest(['apple']), 'apple')

    def test_longest_first(self):
        self.assertEqual(longest(['banana', 'apple']), 'banana')

    def test_longest_last(self):
        self.assertEqual(longest(['apple', 'banana']), 'banana')

    def test_multiple_longest(self):
        self.assertEqual(longest(['ant', 'banana', 'apple', 'dog']), 'banana')



    
  
class ThirteenTest(unittest.TestCase):

    def test_greatest_common_divisor(self):
        self.assertEqual(greatest_common_divisor(10, 25), 5)
        self.assertEqual(greatest_common_divisor(14, 28), 14)
        self.assertEqual(greatest_common_divisor(21, 49), 7)
        self.assertEqual(greatest_common_divisor(81, 153), 9)
class FourteenTest(unittest.TestCase):

    def test_all_prefixes_empty_string(self):
        self.assertEqual(all_prefixes(''), [])

    def test_all_prefixes_single_char_string(self):
        self.assertEqual(all_prefixes('A'), ['A'])

    def test_all_prefixes_multiple_char_string(self):
        self.assertEqual(all_prefixes('Hello'), ['H', 'He', 'Hel', 'Hell', 'Hello'])

    def test_all_prefixes_long_string(self):
        self.assertEqual(all_prefixes('Python'), ['P', 'Py', 'Pyt', 'Pyth', 'Pytho', 'Python'])

    def test_all_prefixes_special_chars_string(self):
        self.assertEqual(all_prefixes('@#$%'), ['@', '@#', '@#$', '@#$%'])
                      
class FifteenTest(unittest.TestCase):

    def test_string_sequence(self):
        self.assertEqual(string_sequence(0), "0")
        self.assertEqual(string_sequence(1), "0 1")
        self.assertEqual(string_sequence(5), "0 1 2 3 4 5")
        self.assertEqual(string_sequence(10), "0 1 2 3 4 5 6 7 8 9 10")




class SixteenTest(unittest.TestCase):

    def test_count_distinct_characters_empty_string(self):
        self.assertEqual(count_distinct_characters(""), 0)

    def test_count_distinct_characters_all_same_characters(self):
        self.assertEqual(count_distinct_characters("aaAAaa"), 1)

    def test_count_distinct_characters_mixed_characters(self):
        self.assertEqual(count_distinct_characters("AbCDefg"), 7)

    def test_count_distinct_characters_special_characters(self):
        self.assertEqual(count_distinct_characters("!@#$%"), 5)

    def test_count_distinct_characters_whitespace(self):
        self.assertEqual(count_distinct_characters("  a b  c  "), 3)


    




class SeventeenTest(unittest.TestCase):

    def test_parse_music_empty_string(self):
        self.assertEqual(parse_music(''), [])

    def test_parse_music_single_note(self):
        self.assertEqual(parse_music('o'), [4])

    def test_parse_music_multiple_notes(self):
        self.assertEqual(parse_music('o o .| o|'), [4, 4, 1, 2])


    
  
class EighteenTest(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(how_many_times("", "test"), 0)

    def test_no_occurrences(self):
        self.assertEqual(how_many_times("abcdefgh", "xyz"), 0)

    def test_single_occurrence(self):
        self.assertEqual(how_many_times("abctesttestgh", "test"), 1)

    def test_multiple_occurrences(self):
        self.assertEqual(how_many_times("testtesttest", "test"), 3)
class NineteenTest(unittest.TestCase):
    
    def test_sort_numbers(self):
        self.assertEqual(sort_numbers('five one seven three two'), 'one two three five seven')
  
    def test_sort_numbers_duplicates(self):
        self.assertEqual(sort_numbers('eight eight eight one one'), 'one one eight eight eight')
  
    def test_sort_numbers_empty(self):
        self.assertEqual(sort_numbers(''), '')
class TwentyTest(unittest.TestCase):
    def test_find_closest_elements(self):
        self.assertEqual(find_closest_elements([1.0, 2.0, 3.0]), (1.0, 2.0))
        self.assertEqual(find_closest_elements([5.0, 8.0, 2.0]), (5.0, 8.0))
        self.assertEqual(find_closest_elements([10.5, 10.2, 10.8, 10.3]), (10.2, 10.3))
from unittest import TestCase

class Twenty_oneTest(unittest.TestCase):

    def test_rescale_to_unit_all_positive_numbers(self):
        numbers = [2, 5, 8, 11]
        expected_result = [0.0, 0.3333333333333333, 0.6666666666666666, 1.0]
        self.assertEqual(rescale_to_unit(numbers), expected_result)

    def test_rescale_to_unit_positive_and_negative_numbers(self):
        numbers = [-3, 0, 5, 10]
        expected_result = [0.0, 0.3, 0.6, 1.0]
        self.assertEqual(rescale_to_unit(numbers), expected_result)

    def test_rescale_to_unit_repeated_numbers(self):
        numbers = [3, 3, 3, 3]
        expected_result = [0.0, 0.0, 0.0, 0.0]
        self.assertEqual(rescale_to_unit(numbers), expected_result)

    def test_rescale_to_unit_empty_list(self):
        numbers = []
        expected_result = []
        self.assertEqual(rescale_to_unit(numbers), expected_result)

  
class TwentyTwoTest(unittest.TestCase):

    def test_filter_integers_with_integers_only(self):
        values = [1, 2, 3]
        self.assertEqual(filter_integers(values), [1, 2, 3])

    def test_filter_integers_with_mixed_values(self):
        values = [1, 'a', 3.14, True, 5]
        self.assertEqual(filter_integers(values), [1, 5])

    def test_filter_integers_with_empty_list(self):
        values = []
        self.assertEqual(filter_integers(values), [])

    def test_filter_integers_with_no_integers(self):
        values = ['a', 'b', 'c']
        self.assertEqual(filter_integers(values), [])
class TwentythreeTest(unittest.TestCase):

    def test_strlen_empty_string(self):
        self.assertEqual(strlen(''), 0)

    def test_strlen_single_character_string(self):
        self.assertEqual(strlen('a'), 1)

    def test_strlen_longer_string(self):
        self.assertEqual(strlen('unittest'), 8)

    def test_strlen_string_with_spaces(self):
        self.assertEqual(strlen('hello world'), 11)
class Twenty_fourTest(unittest.TestCase):

    def test_largest_divisor(self):
        self.assertEqual(largest_divisor(24), 12)
        self.assertEqual(largest_divisor(36), 18)
        self.assertEqual(largest_divisor(17), 1)



class Twenty_fiveTest(unittest.TestCase):

    def test_factorize_case1(self):
        self.assertEqual(factorize(12), [2, 2, 3])

    def test_factorize_case2(self):
        self.assertEqual(factorize(30), [2, 3, 5])

    def test_factorize_case3(self):
        self.assertEqual(factorize(50), [2, 5, 5])

    def test_factorize_case4(self):
        self.assertEqual(factorize(144), [2, 2, 2, 2, 3, 3])


    




class TwentySixTest(unittest.TestCase):

    def test_remove_duplicates_no_duplicates(self):
        numbers = [1, 2, 3, 4, 5]
        self.assertEqual(remove_duplicates(numbers), [1, 2, 3, 4, 5])

    def test_remove_duplicates_with_duplicates(self):
        numbers = [1, 2, 2, 3, 3, 4, 5]
        self.assertEqual(remove_duplicates(numbers), [1, 4, 5])

    def test_remove_duplicates_empty_list(self):
        numbers = []
        self.assertEqual(remove_duplicates(numbers), [])

    def test_remove_duplicates_all_duplicates(self):
        numbers = [1, 1, 1, 1, 1, 1]
        self.assertEqual(remove_duplicates(numbers), [])


    
  



class Twenty_sevenTest(unittest.TestCase):

    def test_flip_case_all_uppercase(self):
        self.assertEqual(flip_case("HELLO"), "hello")

    def test_flip_case_all_lowercase(self):
        self.assertEqual(flip_case("hello"), "HELLO")

    def test_flip_case_mixed_case(self):
        self.assertEqual(flip_case("HeLlO"), "hElLo")

    def test_flip_case_special_characters(self):
        self.assertEqual(flip_case("123@#%$^&"), "123@#%$^&")


    
  
class Twenty_eightTest(unittest.TestCase):
    
    def test_concatenate_empty_list(self):
        self.assertEqual(concatenate([]), '')
        
    def test_concatenate_single_string(self):
        self.assertEqual(concatenate(['Hello']), 'Hello')
        
    def test_concatenate_multiple_strings(self):
        self.assertEqual(concatenate(['Hello', 'World']), 'HelloWorld')
        
    def test_concatenate_strings_with_space(self):
        self.assertEqual(concatenate(['Hello', ' ', 'World']), 'Hello World')
class TwentynineTest(unittest.TestCase):

    def test_filter_by_prefix_empty_list(self):
        strings = []
        prefix = "abc"
        self.assertEqual(filter_by_prefix(strings, prefix), [])

    def test_filter_by_prefix_no_matching_prefix(self):
        strings = ["hello", "world", "python"]
        prefix = "abc"
        self.assertEqual(filter_by_prefix(strings, prefix), [])

    def test_filter_by_prefix_one_matching_prefix(self):
        strings = ["abcde", "xyz", "abcdef"]
        prefix = "abc"
        self.assertEqual(filter_by_prefix(strings, prefix), ["abcde", "abcdef"])

    def test_filter_by_prefix_multiple_matching_prefix(self):
        strings = ["apple", "banana", "abcd", "tomato", "abc-123"]
        prefix = "abc"
        self.assertEqual(filter_by_prefix(strings, prefix), ["abcd", "abc-123"])



class ThirtyTest(unittest.TestCase):

    def test_get_positive_with_positive_numbers(self):
        self.assertEqual(get_positive([1, 2, 3, -4, -5, 6]), [1, 2, 3, 6])

    def test_get_positive_with_only_negative_numbers(self):
        self.assertEqual(get_positive([-1, -2, -3, -4, -5]), [])

    def test_get_positive_with_mixed_numbers(self):
        self.assertEqual(get_positive([-1, 2, 0, 3, -4, 5]), [2, 3, 5])

    def test_get_positive_with_empty_list(self):
        self.assertEqual(get_positive([]), [])


    
  
class ThirtyoneTest(unittest.TestCase):
    
    def test_is_prime_negative_number(self):
        self.assertFalse(is_prime(-5))
    
    def test_is_prime_zero(self):
        self.assertFalse(is_prime(0))
    
    def test_is_prime_one(self):
        self.assertFalse(is_prime(1))
    
    def test_is_prime_primes(self):
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(3))
        self.assertTrue(is_prime(5))
        self.assertTrue(is_prime(7))
    
    def test_is_prime_non_primes(self):
        self.assertFalse(is_prime(4))
        self.assertFalse(is_prime(6))
        self.assertFalse(is_prime(8))
        self.assertFalse(is_prime(9))

class Thirty_twoTest(unittest.TestCase):

    def test_poly(self):
        self.assertEqual(poly([1, 2, 3], 2), 17.0)
        self.assertEqual(poly([1, 0, -1, 2], 3), 14.0)
        self.assertEqual(poly([5, 2, 1], 0), 5.0)

    def test_find_zero(self):
        self.assertAlmostEqual(find_zero([1, 0, -1]), 1.0)
        self.assertAlmostEqual(find_zero([1, 1, -1]), 0.801937735950533)
        self.assertAlmostEqual(find_zero([1, -1, -1]), -0.6180339889570474)

class Thirty_threeTest(unittest.TestCase):

    def test_sort_third_empty_list(self):
        self.assertEqual(sort_third([]), [])

    def test_sort_third_list_with_three_elements(self):
        self.assertEqual(sort_third([3, 2, 1]), [1, 2, 3])

    def test_sort_third_list_with_six_elements(self):
        self.assertEqual(sort_third([5, 4, 3, 2, 1, 0]), [0, 4, 1, 3, 5, 2])

    def test_sort_third_list_with_multiple_elements(self):
        self.assertEqual(sort_third([9, 8, 7, 6, 5, 4, 3, 2, 1, 0]), [0, 8, 1, 6, 4, 3, 9, 2, 7, 5])
class ThirtyfourTest(unittest.TestCase):

    def test_unique_empty_list(self):
        self.assertEqual(unique([]), [])

    def test_unique_all_unique_elements(self):
        self.assertEqual(unique([1, 2, 3, 4]), [1, 2, 3, 4])

    def test_unique_has_duplicates(self):
        self.assertEqual(unique([1, 2, 2, 3, 3, 4]), [1, 2, 3, 4])

    def test_unique_mixed_data_types(self):
        self.assertEqual(unique([1, 'a', 2, 'b', 2, 3]), [1, 2, 3, 'a', 'b'])

    def test_unique_nested_list(self):
        self.assertEqual(unique([[1, 2], [3, 4], [1, 2]]), [[1, 2], [3, 4]])



class Thirty_fiveTest(unittest.TestCase):

    def test_max_element_empty_list(self):
        self.assertEqual(max_element([]), None)

    def test_max_element_single_element_list(self):
        self.assertEqual(max_element([5]), 5)

    def test_max_element_multiple_element_list(self):
        self.assertEqual(max_element([1, 8, 3, 12, 5, 2]), 12)

    def test_max_element_negative_elements(self):
        self.assertEqual(max_element([-10, -5, -3, -7]), -3)


    
  



class Thirty_sixTest(unittest.TestCase):

    def test_fizz_buzz(self):
        self.assertEqual(fizz_buzz(30), 4)
        self.assertEqual(fizz_buzz(50), 6)
        self.assertEqual(fizz_buzz(70), 8)


    

class ThirtysevenTest(unittest.TestCase):

    def test_sort_even_empty_list(self):
        self.assertEqual(sort_even([]), [])

    def test_sort_even_single_element_list(self):
        self.assertEqual(sort_even([5]), [5])

    def test_sort_even_even_number_of_elements(self):
        self.assertEqual(sort_even([4, 2, 6, 1, 3, 5]), [2, 1, 4, 3, 6, 5])

    def test_sort_even_odd_number_of_elements(self):
        self.assertEqual(sort_even([4, 2, 6, 1, 3]), [2, 1, 4, 3, 6])

    def test_sort_even_repeated_elements(self):
        self.assertEqual(sort_even([2, 3, 2, 1, 4, 3]), [2, 1, 2, 3, 4, 3])

class ThirtyEightTest(unittest.TestCase):

    def test_encode_cyclic(self):
        self.assertEqual(encode_cyclic("hello"), "elloh")
        self.assertEqual(encode_cyclic("world"), "rldwo")
        self.assertEqual(encode_cyclic("foo"), "oof")

    def test_decode_cyclic(self):
        self.assertEqual(decode_cyclic("elloh"), "hello")
        self.assertEqual(decode_cyclic("rldwo"), "world")
        self.assertEqual(decode_cyclic("oof"), "foo")


    


class Thirty_nineTest(unittest.TestCase):
    def test_prime_fib(self):
        self.assertEqual(prime_fib(1), 2)
        self.assertEqual(prime_fib(2), 3)
        self.assertEqual(prime_fib(3), 13)
        self.assertEqual(prime_fib(4), 89)
  
class FortyTest(unittest.TestCase):

    def test_triples_sum_to_zero(self):
        self.assertTrue(triples_sum_to_zero([1, -2, 3, 0]))
        self.assertTrue(triples_sum_to_zero([0, 0, 0]))
        self.assertFalse(triples_sum_to_zero([1, 2, 3]))
        self.assertFalse(triples_sum_to_zero([-1, -2, -3]))
        self.assertFalse(triples_sum_to_zero([1, 2, -3, 1]))
class FortyoneTest(unittest.TestCase):

    def test_car_race_collision_positive(self):
        self.assertEqual(car_race_collision(4), 16)

    def test_car_race_collision_negative(self):
        self.assertEqual(car_race_collision(-3), 9)

    def test_car_race_collision_zero(self):
        self.assertEqual(car_race_collision(0), 0)
 


class Forty_twoTest(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(incr_list([]), [])

    def test_positive_numbers(self):
        self.assertEqual(incr_list([1, 2, 3]), [2, 3, 4])

    def test_negative_numbers(self):
        self.assertEqual(incr_list([-1, -2, -3]), [0, -1, -2])

    def test_mixed_numbers(self):
        self.assertEqual(incr_list([0, -3, 5]), [1, -2, 6])



    
  
class FortythreeTest(unittest.TestCase):

    def test_pairs_sum_to_zero_empty_list(self):
        self.assertFalse(pairs_sum_to_zero([]))

    def test_pairs_sum_to_zero_no_pairs(self):
        self.assertFalse(pairs_sum_to_zero([1, 2, 3, 4, 5]))

    def test_pairs_sum_to_zero_pairs_exist(self):
        self.assertTrue(pairs_sum_to_zero([1, 2, -2, 3, 4, -3]))

    def test_pairs_sum_to_zero_single_pair(self):
        self.assertTrue(pairs_sum_to_zero([1, -1]))

    def test_pairs_sum_to_zero_multiple_zero_pairs(self):
        self.assertTrue(pairs_sum_to_zero([0, 1, 2, 0]))

    def test_pairs_sum_to_zero_all_zeros(self):
        self.assertTrue(pairs_sum_to_zero([0, 0, 0, 0]))    

class FortyfourTest(unittest.TestCase):

    def test_change_base_base_10(self):
        self.assertEqual(change_base(44, 10), "44")

    def test_change_base_base_2(self):
        self.assertEqual(change_base(44, 2), "101100")

    def test_change_base_base_16(self):
        self.assertEqual(change_base(44, 16), "2C")

    def test_change_base_large_num(self):
        self.assertEqual(change_base(12345, 8), "30071")

    def test_change_base_zero_input(self):
        self.assertEqual(change_base(0, 7), "0")
class FortyFiveTest(unittest.TestCase):

    def test_triangle_area(self):
        self.assertEqual(triangle_area(3, 6), 9.0)
        self.assertEqual(triangle_area(5, 4), 10.0)
        self.assertEqual(triangle_area(8, 10), 40.0)



class Forty_sixTest(unittest.TestCase):

    def test_example_1(self):
        self.assertEqual(fib4(0), 0)

    def test_example_2(self):
        self.assertEqual(fib4(1), 0)

    def test_example_3(self):
        self.assertEqual(fib4(2), 2)

    def test_example_4(self):
        self.assertEqual(fib4(3), 0)

    def test_example_5(self):
        self.assertEqual(fib4(4), 2)

    def test_example_6(self):
        self.assertEqual(fib4(5), 4)

    def test_example_7(self):
        self.assertEqual(fib4(10), 90)

    def test_example_8(self):
        self.assertEqual(fib4(15), 1456)

    def test_example_9(self):
        self.assertEqual(fib4(20), 13138)


    
  

class Forty_sevenTest(unittest.TestCase):

    def test_odd_list(self):
        self.assertEqual(median([3, 2, 5, 1, 4]), 3)

    def test_even_list(self):
        self.assertEqual(median([7, 10, 5, 3]), 6.0)

    def test_empty_list(self):
        self.assertEqual(median([]), None)


    
  
class Forty_eightTest(unittest.TestCase):

    def test_palindrome_even_length(self):
        self.assertTrue(is_palindrome("racecar"))

    def test_palindrome_odd_length(self):
        self.assertTrue(is_palindrome("level"))

    def test_not_palindrome(self):
        self.assertFalse(is_palindrome("python"))

    def test_single_char_palindrome(self):
        self.assertTrue(is_palindrome("x"))

    def test_empty_string(self):
        self.assertTrue(is_palindrome(""))

class Forty_nineTest(unittest.TestCase):

    def test_modp_small_numbers(self):
        self.assertEqual(modp(0, 1), 1)
        self.assertEqual(modp(1, 1), 0)
        self.assertEqual(modp(2, 5), 2)
    
    def test_modp_large_numbers(self):
        self.assertEqual(modp(10, 1000), 24)
        self.assertEqual(modp(5, 3), 2)





class FiftyTest(unittest.TestCase):
    
    def test_encode_shift(self):
        self.assertEqual(encode_shift("abc"), "fgh")
        self.assertEqual(encode_shift("xyz"), "cde")
        self.assertEqual(encode_shift("Hello, World!"), "Mjqqt, Btwqi!")
    
    def test_decode_shift(self):
        self.assertEqual(decode_shift("fgh"), "abc")
        self.assertEqual(decode_shift("cde"), "xyz")
        self.assertEqual(decode_shift("Mjqqt, Btwqi!"), "Hello, World!")


    


class FiftyoneTest(unittest.TestCase):

    def test_remove_vowels_empty_string(self):
        self.assertEqual(remove_vowels(""), "")

    def test_remove_vowels_no_vowels(self):
        self.assertEqual(remove_vowels("Python"), "Python")

    def test_remove_vowels_all_vowels(self):
        self.assertEqual(remove_vowels("aeiou"), "")

    def test_remove_vowels_mixed_case_vowels(self):
        self.assertEqual(remove_vowels("HeLLo tHerE"), "HLL THR")

    def test_remove_vowels_special_characters(self):
        self.assertEqual(remove_vowels("##$@aeiOu"), "##$@")

  
class Fifty_twoTest:

    def test_below_threshold(self):
        self.assertTrue(below_threshold([1, 2, 3], 5))
        self.assertFalse(below_threshold([10, 20, 30], 15))
        self.assertTrue(below_threshold([], 100))
        self.assertFalse(below_threshold([50, 60, 70], 55))



class Fifty_threeTest(unittest.TestCase):

    def test_add_positive_numbers(self):
        self.assertEqual(add(3, 5), 8)

    def test_add_negative_numbers(self):
        self.assertEqual(add(-3, -5), -8)

    def test_add_mixed_numbers(self):
        self.assertEqual(add(4, -2), 2)

    def test_add_zero_to_number(self):
        self.assertEqual(add(0, 7), 7)

    def test_add_zero_to_zero(self):
        self.assertEqual(add(0, 0), 0)


    
 
class FiftyfourTest(unittest.TestCase):

    def test_same_chars_same_length(self):
        self.assertTrue(same_chars('abc', 'cab'))

    def test_same_chars_different_length(self):
        self.assertFalse(same_chars('abc', 'ab'))

    def test_same_chars_duplicate_characters(self):
        self.assertTrue(same_chars('hello', 'helol'))

    def test_same_chars_empty_strings(self):
        self.assertTrue(same_chars('', ''))
 


class Fifty_fiveTest(unittest.TestCase):

    def test_fib_zero(self):
        self.assertEqual(fib(0), 0)

    def test_fib_one(self):
        self.assertEqual(fib(1), 1)

    def test_fib_positive(self):
        self.assertEqual(fib(5), 5)

    def test_fib_negative(self):
        self.assertEqual(fib(-1), None)




class FiftysixTest(unittest.TestCase):
    
    def test_correct_bracketing_valid(self):
        self.assertTrue(correct_bracketing("<><>"))
        self.assertTrue(correct_bracketing("<<>>"))
        self.assertTrue(correct_bracketing("<><>>><<"))
    
    def test_correct_bracketing_invalid(self):
        self.assertFalse(correct_bracketing("<>><"))
        self.assertFalse(correct_bracketing("<<>><"))
        self.assertFalse(correct_bracketing(">>>><<<<"))
    
    def test_correct_bracketing_edge_cases(self):
        self.assertTrue(correct_bracketing(""))
        self.assertTrue(correct_bracketing("><"))
        self.assertFalse(correct_bracketing("<<<"))
        self.assertFalse(correct_bracketing(">>>"))


    
  
class FiftysevenTest(unittest.TestCase):

    def test_monotonic_sorted_list_asc(self):
        self.assertTrue(monotonic([1, 2, 3, 4, 5]))

    def test_monotonic_sorted_list_desc(self):
        self.assertTrue(monotonic([5, 4, 3, 2, 1]))

    def test_monotonic_unsorted_list(self):
        self.assertFalse(monotonic([3, 1, 2, 5, 4]))

    def test_monotonic_empty_list(self):
        self.assertTrue(monotonic([]))

    def test_monotonic_single_element_list(self):
        self.assertTrue(monotonic([42]))

class Fifty_eightTest(unittest.TestCase):

    def test_common_empty_lists(self):
        self.assertEqual(common([], []), [])

    def test_common_no_common_elements(self):
        self.assertEqual(common([1, 2, 3], [4, 5, 6]), [])

    def test_common_one_common_element(self):
        self.assertEqual(common([1, 2, 3], [3, 4, 5]), [3])

    def test_common_multiple_common_elements(self):
        self.assertEqual(common([1, 2, 3, 4, 5], [3, 4, 5, 6, 7]), [3, 4, 5])

    def test_common_duplicate_elements(self):
        self.assertEqual(common([1, 2, 3, 3, 4], [3, 4, 4, 5]), [3, 4])

    def test_common_mixed_types(self):
        self.assertEqual(common([1, 'a', 3.14, True], [True, 3.14, 'b', 5]), [True, 3.14])
  

class FiftyNineTest(unittest.TestCase):

    def test_is_prime(self):
        self.assertFalse(is_prime(0))
        self.assertFalse(is_prime(1))
        self.assertFalse(is_prime(4))
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(3))
        self.assertTrue(is_prime(7))

    def test_largest_prime_factor(self):
        self.assertEqual(largest_prime_factor(10), 5)
        self.assertEqual(largest_prime_factor(15), 5)
        self.assertEqual(largest_prime_factor(30), 5)
        self.assertEqual(largest_prime_factor(13195), 29)


    

unittest
class SixtyTest(unittest.TestCase):

    def test_sum_to_n_with_positive_integer(self):
        self.assertEqual(sum_to_n(5), 15)

    def test_sum_to_n_with_zero(self):
        self.assertEqual(sum_to_n(0), 0)

    def test_sum_to_n_with_negative_integer(self):
        self.assertEqual(sum_to_n(-3), 0)

                                                                               


class SixtyoneTest(unittest.TestCase):

    def test_correct_bracketing_single_open_close(self):
        self.assertTrue(correct_bracketing("()"))

    def test_correct_bracketing_multiple_pairs(self):
        self.assertTrue(correct_bracketing("()()"))

    def test_correct_bracketing_nested(self):
        self.assertTrue(correct_bracketing("(())"))

    def test_correct_bracketing_imbalanced(self):
        self.assertFalse(correct_bracketing("())"))

    def test_correct_bracketing_extra_closing(self):
        self.assertFalse(correct_bracketing("()("))

    def test_correct_bracketing_extra_opening(self):
        self.assertFalse(correct_bracketing("())"))
  
class SixtytwoTest(unittest.TestCase):

    def test_derivative_empty_list(self):
        self.assertEqual(derivative([]), [])

    def test_derivative_single_element(self):
        self.assertEqual(derivative([5]), [])

    def test_derivative_positive_values(self):
        self.assertEqual(derivative([2, 3, 4, 5]), [3, 8, 15])

    def test_derivative_negative_values(self):
        self.assertEqual(derivative([-2, -3, -4, -5]), [-3, -8, -15])

    def test_derivative_mixed_values(self):
        self.assertEqual(derivative([2, -3, 4, -5]), [-3, 8, -15])
  


class SixtythreeTest(unittest.TestCase):

    def test_fibfib_zero(self):
        self.assertEqual(fibfib(0), 0)

    def test_fibfib_one(self):
        self.assertEqual(fibfib(1), 0)

    def test_fibfib_two(self):
        self.assertEqual(fibfib(2), 1)

    def test_fibfib_other_values(self):
        self.assertEqual(fibfib(3), 1)
        self.assertEqual(fibfib(4), 2)
        self.assertEqual(fibfib(5), 4)
        self.assertEqual(fibfib(6), 7)
        self.assertEqual(fibfib(7), 13)


    
  
class SixtyFourTest(unittest.TestCase):

    def test_vowels_count_no_vowels(self):
        self.assertEqual(vowels_count("xyz"), 0)

    def test_vowels_count_lowercase_vowels(self):
        self.assertEqual(vowels_count("hello"), 2)

    def test_vowels_count_uppercase_vowels(self):
        self.assertEqual(vowels_count("WOrld"), 1)

    def test_vowels_count_mixed_vowels(self):
        self.assertEqual(vowels_count("hEllo"), 2)

    def test_vowels_count_ends_with_y(self):
        self.assertEqual(vowels_count("happy"), 2)

    def test_vowels_count_ends_with_capital_Y(self):
        self.assertEqual(vowels_count("babY"), 2)

    def test_vowels_count_only_vowels(self):
        self.assertEqual(vowels_count("aeiouAEIOU"), 10)

    def test_vowels_count_empty_string(self):
        self.assertEqual(vowels_count(""), 0)

    def test_vowels_count_whitespace_only_string(self):
        self.assertEqual(vowels_count("   "), 0)

    def test_vowels_count_special_characters(self):
        self.assertEqual(vowels_count("!@#$%"), 0)
    


class SixtyFiveTest(unittest.TestCase):

    def test_circular_shift_with_shift_greater_than_length(self):
        self.assertEqual(circular_shift(12345, 7), '54321')

    def test_circular_shift_with_shift_equal_to_length(self):
        self.assertEqual(circular_shift(6789, 4), '6789')

    def test_circular_shift_with_shift_less_than_length(self):
        self.assertEqual(circular_shift(987654, 3), '654987')


    




class Sixty_sixTest(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(digitSum(""), 0)

    def test_all_uppercase_letters(self):
        self.assertEqual(digitSum("ABC"), 195)

    def test_mixed_characters(self):
        self.assertEqual(digitSum("aBcD"), 195)


    


class SixtysevenTest(unittest.TestCase):

    def test_fruit_distribution_empty_string(self):
        self.assertEqual(fruit_distribution('', 10), 10)

    def test_fruit_distribution_no_numbers(self):
        self.assertEqual(fruit_distribution('apple banana', 20), 20)

    def test_fruit_distribution_only_numbers(self):
        self.assertEqual(fruit_distribution('5 10 15', 30), 0)

    def test_fruit_distribution_mixed_input(self):
        self.assertEqual(fruit_distribution('apple 10 banana 5', 25), 10)

    def test_fruit_distribution_negative_numbers(self):
        self.assertEqual(fruit_distribution('-5 10 -15', 30), 40)

    def test_fruit_distribution_decimal_numbers(self):
        self.assertEqual(fruit_distribution('5.5 10.2 15.8', 30), 3)

class SixtyEightTest(unittest.TestCase):

    def test_empty_array(self):
        self.assertEqual(pluck([]), [])

    def test_no_even_numbers(self):
        self.assertEqual(pluck([1, 3, 5]), [])

    def test_even_numbers(self):
        self.assertEqual(pluck([2, 4, 6, 3, 8]), [2, 0])

    def test_multiple_even_numbers(self):
        self.assertEqual(pluck([10, 2, 8, 4, 6]), [2, 1])

    def test_negative_numbers(self):
        self.assertEqual(pluck([-2, -4, -6, 3, 8]), [-6, 2])
 


class SixtynineTest(unittest.TestCase):

    def test_search_empty_list(self):
        self.assertEqual(search([]), -1)

    def test_search_single_element(self):
        self.assertEqual(search([5]), -1)

    def test_search_non_ascending_order(self):
        self.assertEqual(search([1, 2, 3, 4, 5]), 3)

    def test_search_all_same_elements(self):
        self.assertEqual(search([1, 1, 1, 1, 1]), 1)

    def test_search_duplicate_elements(self):
        self.assertEqual(search([1, 2, 3, 4, 2, 5, 4]), 2)


    
  
class SeventyTest(unittest.TestCase):

    def test_strange_sort_list_with_empty_list(self):
        self.assertEqual(strange_sort_list([]), [])

    def test_strange_sort_list_with_single_element(self):
        self.assertEqual(strange_sort_list([5]), [5])

    def test_strange_sort_list_with_ordered_elements(self):
        self.assertEqual(strange_sort_list([1, 2, 3, 4, 5]), [1, 5, 2, 4, 3])

    def test_strange_sort_list_with_repeated_elements(self):
        self.assertEqual(strange_sort_list([1, 1, 2, 2, 3, 3]), [1, 3, 2, 2, 1, 3])

    def test_strange_sort_list_with_negative_elements(self):
        self.assertEqual(strange_sort_list([-3, -1, -2, 0, -4]), [-4, 0, -3, -1, -2])
class SeventyoneTest(unittest.TestCase):

    def test_triangle_area_valid(self):
        self.assertEqual(triangle_area(3, 4, 5), 6.0)
        self.assertEqual(triangle_area(5, 12, 13), 30.0)
        self.assertEqual(triangle_area(8, 15, 17), 60.0)

    def test_triangle_area_invalid(self):
        self.assertEqual(triangle_area(1, 1, 3), -1)
        self.assertEqual(triangle_area(0, 0, 0), -1)
class SeventyTwoTest(unittest.TestCase):

    def test_will_it_fly_sum_greater_than_w(self):
        self.assertFalse(will_it_fly([1, 2, 3], 5))

    def test_will_it_fly_not_palindrome(self):
        self.assertFalse(will_it_fly([1, 2, 3, 4], 6))

    def test_will_it_fly_palindrome(self):
        self.assertTrue(will_it_fly([1, 2, 2, 1], 6))



class SeventythreeTest(unittest.TestCase):

    def test_smallest_change_odd_length(self):
        self.assertEqual(smallest_change([1, 2, 3, 4, 5]), 2)

    def test_smallest_change_even_length(self):
        self.assertEqual(smallest_change([1, 2, 2, 1]), 0)

    def test_smallest_change_empty_array(self):
        self.assertEqual(smallest_change([]), 0)

    def test_smallest_change_single_element(self):
        self.assertEqual(smallest_change([1]), 0)


    
  
class SeventyfourTest(unittest.TestCase):

    def test_total_match_lst1_shorter(self):
        self.assertEqual(total_match(['abc', 'def'], ['ghi', 'jkl']), ['abc', 'def'])

    def test_total_match_lst2_shorter(self):
        self.assertEqual(total_match(['abc', 'def', 'ghi'], ['jkl']), ['jkl'])

    def test_total_match_equal_lengths(self):
        self.assertEqual(total_match(['abc', 'def'], ['ghi', 'jkl']), ['abc', 'def'])
class SeventyFiveTest(unittest.TestCase):

    def test_is_multiply_prime(self):
        self.assertTrue(is_multiply_prime(2))
        self.assertFalse(is_multiply_prime(1))
        self.assertTrue(is_multiply_prime(30))
        self.assertFalse(is_multiply_prime(7))
        self.assertTrue(is_multiply_prime(5))
        self.assertFalse(is_multiply_prime(3))
 
class SeventysixTest(unittest.TestCase):

    def test_power_of_one(self):
        self.assertTrue(is_simple_power(1, 1))

    def test_power_of_two(self):
        self.assertTrue(is_simple_power(2, 2))

    def test_power_of_three(self):
        self.assertTrue(is_simple_power(9, 3))

    def test_not_power(self):
        self.assertFalse(is_simple_power(15, 3))

    def test_large_number(self):
        self.assertTrue(is_simple_power(1000000, 10))


    



class SeventysevenTest(unittest.TestCase):
    
    def test_positive_cube(self):
        self.assertTrue(iscube(125))

    def test_negative_cube(self):
        self.assertFalse(iscube(-125))

    def test_non_cube(self):
        self.assertFalse(iscube(30))

    def test_zero_cube(self):
        self.assertTrue(iscube(0))

    def test_large_number(self):
        self.assertTrue(iscube(39304))


    




class SeventyEightTest(unittest.TestCase):

    def test_hex_key_valid_input(self):
        self.assertEqual(hex_key('357B'), 4)
        self.assertEqual(hex_key('2357BD'), 6)
        self.assertEqual(hex_key('77777'), 0)
    
    def test_hex_key_empty_input(self):
        self.assertEqual(hex_key(''), 0)
    
    def test_hex_key_invalid_input(self):
        self.assertEqual(hex_key('ABCDEF'), 0)
        self.assertEqual(hex_key('999999'), 0)


    

class SeventynineTest(unittest.TestCase):

    def test_decimal_to_binary(self):
        self.assertEqual(decimal_to_binary(0), "db0db")
        self.assertEqual(decimal_to_binary(5), "db101db")
        self.assertEqual(decimal_to_binary(10), "db1010db")
        self.assertEqual(decimal_to_binary(15), "db1111db")
class EightyTest(unittest.TestCase):

    def test_is_happy_short_string(self):
        self.assertFalse(is_happy("HA"))

    def test_is_happy_not_happy(self):
        self.assertFalse(is_happy("HAPPY"))

    def test_is_happy_happy(self):
        self.assertTrue(is_happy("HELLO"))

    def test_is_happy_empty_string(self):
        self.assertFalse(is_happy(""))

    def test_is_happy_single_character(self):
        self.assertFalse(is_happy("A"))

class EightyoneTest(unittest.TestCase):

    def test_numerical_letter_grade_all_Aplus(self):
        grades = [4.0, 4.0, 4.0]
        self.assertEqual(numerical_letter_grade(grades), ["A+", "A+", "A+"])

    def test_numerical_letter_grade_mixed_grades(self):
        grades = [3.8, 2.7, 1.5]
        self.assertEqual(numerical_letter_grade(grades), ["A", "B", "D"])


class Eighty_twoTest(unittest.TestCase):

    def test_prime_length_empty_string(self):
        self.assertFalse(prime_length(''))

    def test_prime_length_single_character_string(self):
        self.assertFalse(prime_length('a'))

    def test_prime_length_prime_length_input(self):
        self.assertTrue(prime_length('hello'))

    def test_prime_length_non_prime_length_input(self):
        self.assertFalse(prime_length('world'))

    def test_prime_length_longer_prime_length_input(self):
        self.assertTrue(prime_length('engineering'))

    def test_prime_length_longer_non_prime_length_input(self):
        self.assertFalse(prime_length('software'))


    



class EightythreeTest(unittest.TestCase):
    
    def test_starts_one_ends_one(self):
        self.assertEqual(starts_one_ends(1), 1)
        
    def test_starts_one_ends_two(self):
        self.assertEqual(starts_one_ends(2), 18)
        
    def test_starts_one_ends_three(self):
        self.assertEqual(starts_one_ends(3), 180)
    
    def test_starts_one_ends_large(self):
        self.assertEqual(starts_one_ends(7), 18000000)


    
  
class Eighty_fourTest(unittest.TestCase):

    def test1(self):
        self.assertEqual(solve(84), '101010')

    def test2(self):
        self.assertEqual(solve(123), '100010')
        
    def test3(self):
        self.assertEqual(solve(9876), '101110')

    def test4(self):
        self.assertEqual(solve(0), '0')
class EightyfiveTest(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add([1, 2, 3, 4, 5, 6]), 6)
        self.assertEqual(add([2, 4, 6, 8, 10]), 18)
        self.assertEqual(add([1, 3, 5, 7, 9]), 0)
class EightySixTest(unittest.TestCase):

    def test_anti_shuffle_empty_string(self):
        self.assertEqual(anti_shuffle(''), '')

    def test_anti_shuffle_single_word(self):
        self.assertEqual(anti_shuffle('hello'), 'ehllo')

    def test_anti_shuffle_multiple_words(self):
        self.assertEqual(anti_shuffle('hello world'), 'ehllo dlorw')

    def test_anti_shuffle_special_characters(self):
        self.assertEqual(anti_shuffle('abc! @def'), '!abc @def')

    def test_anti_shuffle_repeating_characters(self):
        self.assertEqual(anti_shuffle('banana'), 'aaabnn')

    def test_anti_shuffle_large_input(self):
        input_str = 'lorem ipsum dolor sit amet consectetur adipiscing elit'
        expected_output = 'elmor ipsmu dloor ist aemt cceennorsstu acdegiipsg eilrt'
        self.assertEqual(anti_shuffle(input_str), expected_output)
class Eighty_sevenTest(unittest.TestCase):

    def test_get_row(self):
        self.assertEqual(get_row([[2, 3, 4], [5, 6, 7], [8, 7, 6]], 7), [(1, 2), (2, 1)])
        self.assertEqual(get_row([[1, 1, 1], [2, 2, 2], [3, 3, 3]], 1), [(0, 2), (1, 2), (2, 2)])
class Eighty_eightTest(unittest.TestCase):
    def test_sort_array_empty(self):
        self.assertEqual(sort_array([]), [])

    def test_sort_array_odd_sum(self):
        self.assertEqual(sort_array([1, 2, 3, 4, 5]), [5, 4, 3, 2, 1])

    def test_sort_array_even_sum(self):
        self.assertEqual(sort_array([2, 3, 7, 9, 12]), [2, 3, 7, 9, 12])
 


class EightyNineTest(unittest.TestCase):

    def test_encrypt_basic(self):
        self.assertEqual(encrypt('hello'), 'jgnnq')

    def test_encrypt_special_characters(self):
        self.assertEqual(encrypt('how are you?'), 'jqa ctg aqw?')

    def test_encrypt_empty_string(self):
        self.assertEqual(encrypt(''), '')


    




class NinetyTest(unittest.TestCase):

    def test_empty_list(self):
        self.assertIsNone(next_smallest([]))

    def test_single_element_list(self):
        self.assertIsNone(next_smallest([1]))

    def test_all_equal_elements(self):
        self.assertIsNone(next_smallest([5, 5, 5, 5]))

    def test_sorted_list(self):
        self.assertEqual(next_smallest([1, 2, 3, 4]), 2)

    def test_unsorted_list(self):
        self.assertEqual(next_smallest([9, 3, 5, 1, 8, 5]), 3)

    def test_negative_numbers(self):
        self.assertEqual(next_smallest([-10, -5, -15, -1]), -10)


    
  
class NinetyOneTest(unittest.TestCase):

    def test_is_bored_empty_string(self):
        self.assertEqual(is_bored(''), 0)

    def test_is_bored_single_sentence(self):
        self.assertEqual(is_bored('I am bored. I need excitement!'), 2)

    def test_is_bored_multiple_sentences(self):
        self.assertEqual(is_bored('I am bored. I need excitement! I need fun.'), 3)
class NinetyTwoTest(unittest.TestCase):
    
    def test_all_integers(self):
        self.assertTrue(any_int(1, 2, 3))
        self.assertTrue(any_int(3, 2, 1))
        self.assertTrue(any_int(2, 3, 1))
        
    def test_two_integers(self):
        self.assertFalse(any_int(1, 2, '3'))
        self.assertFalse(any_int(1, '2', 3))
        self.assertFalse(any_int('1', 2, 3))
        
    def test_sum_relationships(self):
        self.assertTrue(any_int(5, 6, 11))
        self.assertTrue(any_int(10, 1, 9))
        self.assertTrue(any_int(7, 3, 10))
        
    def test_negative_integers(self):
        self.assertTrue(any_int(-1, -2, -3))
        self.assertTrue(any_int(-3, -2, -1))
        self.assertFalse(any_int(1, -2, 3))
        
    def test_mixed_types(self):
        self.assertFalse(any_int(1, '2', 3))
        self.assertFalse(any_int('1', '2', 3))
        self.assertFalse(any_int('1', 2, '3'))


class NinetyThreeTest(unittest.TestCase):

    def test_encode_no_vowels(self):
        self.assertEqual(encode("Hello, World!"), "Jemmo, Wurld!")

    def test_encode_all_vowels(self):
        self.assertEqual(encode("a e i o u A E I O U"), "c g k q w C G K Q W")

    def test_encode_mixed_case_vowels(self):
        self.assertEqual(encode("AppLE"), "CrrNG")
  
class Ninety_fourTest(unittest.TestCase):
    def test_skjkasdkd(self):
        self.assertEqual(skjkasdkd([3, 5, 7, 9, 11, 15]), 2)
        self.assertEqual(skjkasdkd([2, 4, 6, 8, 10, 12]), 2)
        self.assertEqual(skjkasdkd([13, 17, 19, 23, 29]), 7)

class Ninety_fiveTest(unittest.TestCase):
    
    def test_empty_dict(self):
        self.assertFalse(check_dict_case({}))
    
    def test_all_uppercase(self):
        self.assertTrue(check_dict_case({"HELLO": "value"}))
    
    def test_mixed_case(self):
        self.assertFalse(check_dict_case({"Hello": "value", "WORLD": "value"}))
    
    def test_all_lowercase(self):
        self.assertTrue(check_dict_case({"hello": "value"}))
    
    def test_mixed_case_with_non_string_key(self):
        self.assertFalse(check_dict_case({123: "value", "WORLD": "value"}))
    
    def test_single_element_dict(self):
        self.assertTrue(check_dict_case({"Hello": "value"}))
  
class NinetySixTest(unittest.TestCase):

    def test_count_up_to_with_n_equal_to_1(self):
        self.assertEqual(count_up_to(1), [])

    def test_count_up_to_with_n_equal_to_10(self):
        self.assertEqual(count_up_to(10), [2, 3, 5, 7])

    def test_count_up_to_with_n_equal_to_20(self):
        self.assertEqual(count_up_to(20), [2, 3, 5, 7, 11, 13, 17, 19])

    def test_count_up_to_with_n_equal_to_2(self):
        self.assertEqual(count_up_to(2), [])

    def test_count_up_to_with_n_equal_to_3(self):
        self.assertEqual(count_up_to(3), [2])

    def test_count_up_to_with_n_equal_to_30(self):
        self.assertEqual(count_up_to(30), [2, 3, 5, 7, 11, 13, 17, 19, 23, 29])
class Ninety_sevenTest(unittest.TestCase):

    def test_multiply_positive_numbers(self):
        self.assertEqual(multiply(5, 7), 5)

    def test_multiply_negative_numbers(self):
        self.assertEqual(multiply(-3, -4), 2)

    def test_multiply_mixed_numbers(self):
        self.assertEqual(multiply(9, -2), 8)

    def test_multiply_zero(self):
        self.assertEqual(multiply(0, 7), 0)

class NinetyeightTest(unittest.TestCase):
    def test_count_upper_empty_string(self):
        self.assertEqual(count_upper(''), 0)

    def test_count_upper_no_uppercase(self):
        self.assertEqual(count_upper('abcdef'), 0)

    def test_count_upper_only_vowels(self):
        self.assertEqual(count_upper('AEIOU'), 5)

    def test_count_upper_mixed_case(self):
        self.assertEqual(count_upper('aAbBcCdDeEfF'), 3)

    def test_count_upper_alternating_vowels_and_consonants(self):
        self.assertEqual(count_upper('AbCdEfG'), 2)
  

class Ninety_nineTest(unittest.TestCase):
    def test_closest_integer_with_half_value(self):
        self.assertEqual(closest_integer('3.5'), 4)
        self.assertEqual(closest_integer('5.5'), 6)
        self.assertEqual(closest_integer('-2.5'), -2)
    
    def test_closest_integer_without_half_value(self):
        self.assertEqual(closest_integer('8.00'), 8)
        self.assertEqual(closest_integer('10.0'), 10)
    
    def test_closest_integer_with_empty_value(self):
        self.assertEqual(closest_integer(''), 0)
        self.assertEqual(closest_integer('.5'), 0)


    
  
class One_hundredTest(unittest.TestCase):

    def test_make_a_pile(self):
        self.assertEqual(make_a_pile(0), [])
        self.assertEqual(make_a_pile(1), [1])
        self.assertEqual(make_a_pile(5), [5, 7, 9, 11, 13])
        self.assertEqual(make_a_pile(10), [10, 12, 14, 16, 18, 20, 22, 24, 26, 28])

    def test_make_a_pile_negative(self):
        self.assertEqual(make_a_pile(-1), [])

class OneHundredAndOneTest(unittest.TestCase):

    def test_words_string_empty_string(self):
        self.assertEqual(words_string(''), [])

    def test_words_string_no_commas(self):
        self.assertEqual(words_string('hello world'), ['hello', 'world'])

    def test_words_string_with_commas(self):
        self.assertEqual(words_string('hello,world'), ['hello', 'world'])

    def test_words_string_multiple_commas(self):
        self.assertEqual(words_string('hello,my,name,is,john'), ['hello', 'my', 'name', 'is', 'john'])
  
class OnetwoTest(unittest.TestCase):

    def test_choose_num_x_greater_than_y(self):
        self.assertEqual(choose_num(5, 3), -1)
    
    def test_choose_num_y_even(self):
        self.assertEqual(choose_num(2, 4), 4)

    def test_choose_num_x_equal_to_y(self):
        self.assertEqual(choose_num(2, 2), -1)

    def test_choose_num_default(self):
        self.assertEqual(choose_num(4, 7), 6)



class OneHundredAndThreeTest(unittest.TestCase):

    def test_rounded_avg_positive(self):
        result = rounded_avg(1, 5)
        self.assertEqual(result, '0b11')

    def test_rounded_avg_negative(self):
        result = rounded_avg(5, 1)
        self.assertEqual(result, -1)


    

class OnefourTest(unittest.TestCase):

    def test_unique_digits_empty_list(self):
        self.assertEqual(unique_digits([]), [])

    def test_unique_digits_no_odd_digits(self):
        self.assertEqual(unique_digits([22, 444, 666]), [])

    def test_unique_digits_all_odd_digits(self):
        self.assertEqual(unique_digits([135, 3579, 19]), [19, 135, 3579])

    def test_unique_digits_mixed_digits(self):
        self.assertEqual(unique_digits([123, 456, 789]), [123, 789])

    def test_unique_digits_only_single_digit(self):
        self.assertEqual(unique_digits([1, 3, 5]), [1, 3, 5])
 
class OnefiveTest(unittest.TestCase):

    def test_by_length(self):
        arr = [1, 2, 3, 4, 5]
        self.assertEqual(by_length(arr), ["One", "Two", "Three", "Four", "Five"])

    def test_by_length_empty(self):
        arr = []
        self.assertEqual(by_length(arr), [])

    def test_by_length_duplicates(self):
        arr = [2, 2, 4, 4, 1, 1]
        self.assertEqual(by_length(arr), ["One", "Two", "Four"])

    def test_by_length_non_integer(self):
        arr = [5, 'a', 3, 2]
        self.assertEqual(by_length(arr), ["Two", "Three", "Five"])

    def test_by_length_negative_values(self):
        arr = [-1, 5, 3, -4]
        self.assertEqual(by_length(arr), ["Five", "Three"])



class OnesixTest(unittest.TestCase):

    def test_even_numbers(self):
        self.assertEqual(f(2), [1, 3])

    def test_odd_numbers(self):
        self.assertEqual(f(3), [1, 3, 6])

    def test_negative_input(self):
        self.assertEqual(f(-4), [])

    def test_large_input(self):
        self.assertEqual(f(5), [1, 3, 6, 10, 15])

class OneHundredAndsevenTest(unittest.TestCase):

    def test_even_odd_palindrome(self):
        self.assertEqual(even_odd_palindrome(10), (4, 3))
        self.assertEqual(even_odd_palindrome(20), (9, 6))
        self.assertEqual(even_odd_palindrome(5), (1, 1))
        self.assertEqual(even_odd_palindrome(0), (0, 0))
 
class OneHundredAndeightTest(unittest.TestCase):

    def test_count_nums_empty_array(self):
        self.assertEqual(count_nums([]), 0)

    def test_count_nums_positive_numbers_only(self):
        self.assertEqual(count_nums([123, 456, 789]), 3)

    def test_count_nums_negative_numbers_only(self):
        self.assertEqual(count_nums([-123, -456, -789]), 0)

    def test_count_nums_mixed_numbers(self):
        self.assertEqual(count_nums([-123, 456, -789]), 1)

    def test_count_nums_zeros(self):
        self.assertEqual(count_nums([0, 0, 0]), 0)

    def test_count_nums_mixed_numbers_with_zeros(self):
        self.assertEqual(count_nums([123, 0, -456, 0, 789]), 2)
  

class OneHundredAndnineTest(unittest.TestCase):
    
    def test_move_one_ball_empty(self):
        self.assertTrue(move_one_ball([]))
    
    def test_move_one_ball_already_sorted(self):
        self.assertTrue(move_one_ball([1, 2, 3, 4, 5]))
    
    def test_move_one_ball_single_element(self):
        self.assertTrue(move_one_ball([9]))
    
    def test_move_one_ball_sorted_single_swap(self):
        self.assertTrue(move_one_ball([2, 1, 3]))
    
    def test_move_one_ball_sorted_multiple_swaps(self):
        self.assertTrue(move_one_ball([3, 5, 4, 2, 1]))
    
    def test_move_one_ball_unsorted(self):
        self.assertFalse(move_one_ball([5, 2, 6, 1, 4]))
    
    def test_move_one_ball_duplicate_elements(self):
        self.assertTrue(move_one_ball([3, 3, 4, 4, 5, 5]))
  
class OneHundredAndtenTest(unittest.TestCase):

    def test_exchange_even_greater_than_odd(self):
        lst1 = [1, 3, 5]
        lst2 = [2, 4, 6]
        self.assertEqual(exchange(lst1, lst2), "YES")

    def test_exchange_even_equal_to_odd(self):
        lst1 = [1, 2, 3]
        lst2 = [4, 5, 6]
        self.assertEqual(exchange(lst1, lst2), "YES")

    def test_exchange_odd_greater_than_even(self):
        lst1 = [1, 3, 5]
        lst2 = [1, 4, 6]
        self.assertEqual(exchange(lst1, lst2), "NO")


class OneHundredAndelevenTest(unittest.TestCase):

    def test_histogram_with_one_most_frequent_word(self):
        result = histogram("hello world hello")
        self.assertEqual(result, {'hello': 2})
    
    def test_histogram_with_multiple_most_frequent_words(self):
        result = histogram("apple banana banana apple orange")
        self.assertEqual(result, {'apple': 2, 'banana': 2})
    
    def test_histogram_with_empty_string(self):
        result = histogram("")
        self.assertEqual(result, {})
    
    def test_histogram_with_all_unique_words(self):
        result = histogram("one two three")
        self.assertEqual(result, {'one': 1, 'two': 1, 'three': 1})

    def test_histogram_with_same_frequency_for_all_words(self):
        result = histogram("a b c d e")
        self.assertEqual(result, {'a': 1, 'b': 1, 'c': 1, 'd': 1, 'e': 1})

    def test_histogram_with_special_characters(self):
        result = histogram("apple@# banana apple orange")
        self.assertEqual(result, {'apple@#': 1, 'banana': 1, 'orange': 1})


    

class OneHundredAndtwelveTest(unittest.TestCase):

    def test_reverse_delete_matching_characters(self):
        result = reverse_delete("hello", "el")
        self.assertEqual(result, ('ho', False))

    def test_reverse_delete_no_matching_characters(self):
        result = reverse_delete("hello", "z")
        self.assertEqual(result, ('hello', True))

    def test_reverse_delete_empty_string(self):
        result = reverse_delete("", "abc")
        self.assertEqual(result, ('', True))
  
class OneHundredAndthirteenTest(unittest.TestCase):

    def test_odd_count(self):
        self.assertEqual(odd_count(['123', '456']), ['the number of odd elements 2 in the string 2 of the input.', 'the number of odd elements 0 in the string 0 of the input.'])
        self.assertEqual(odd_count(['2468', '13579']), ['the number of odd elements 0 in the string 0 of the input.', 'the number of odd elements 5 in the string 5 of the input.'])
        self.assertEqual(odd_count(['987654321', ''], ['the number of odd elements 5 in the string 5 of the input.', 'the number of odd elements 0 in the string 0 of the input.']))
 
class OneHundredAndfourteenTest(unittest.TestCase):

    def test_minSubArraySum_emptyList(self):
        self.assertEqual(minSubArraySum([]), 0)
    
    def test_minSubArraySum_singleElement(self):
        self.assertEqual(minSubArraySum([5]), -5)
    
    def test_minSubArraySum_basicCase(self):
        self.assertEqual(minSubArraySum([1, -2, 3, -4, 5]), -6)
    
    def test_minSubArraySum_allPositiveNumbers(self):
        self.assertEqual(minSubArraySum([1, 2, 3]), 0)
    
    def test_minSubArraySum_allNegativeNumbers(self):
        self.assertEqual(minSubArraySum([-1, -2, -3]), 1)




class OneHundredAndFifteenTest(unittest.TestCase):

    def test_max_fill_empty_grid(self):
        grid = []
        capacity = 10
        self.assertEqual(max_fill(grid, capacity), 0)

    def test_max_fill_single_row_within_capacity(self):
        grid = [[3, 4, 5]]
        capacity = 10
        self.assertEqual(max_fill(grid, capacity), 1)

    def test_max_fill_single_row_exceeds_capacity(self):
        grid = [[7, 8, 9]]
        capacity = 10
        self.assertEqual(max_fill(grid, capacity), 3)

    def test_max_fill_multiple_rows(self):
        grid = [[3, 4, 5], [6, 7]]
        capacity = 10
        self.assertEqual(max_fill(grid, capacity), 1)

    def test_max_fill_multiple_rows_exceed_capacity(self):
        grid = [[12, 4, 5], [6, 7]]
        capacity = 10
        self.assertEqual(max_fill(grid, capacity), 2)

class One_hundred_and_sixteenTest(unittest.TestCase):

    def test_sort_array_empty(self):
        arr = []
        self.assertEqual(sort_array(arr), [])

    def test_sort_array_single_element(self):
        arr = [5]
        self.assertEqual(sort_array(arr), [5])

    def test_sort_array_multiple_elements(self):
        arr = [5, 3, 7, 2, 8]
        self.assertEqual(sort_array(arr), [3, 5, 2, 7, 8])

    def test_sort_array_duplicate_elements(self):
        arr = [5, 3, 7, 3, 8]
        self.assertEqual(sort_array(arr), [3, 3, 5, 7, 8])

    def test_sort_array_negative_elements(self):
        arr = [-5, 3, -7, 2, 8]
        self.assertEqual(sort_array(arr), [3, -5, 2, -7, 8])


    

 
class OneHundredAndSeventeenTest(unittest.TestCase):

    def test_select_words_no_consonants(self):
        self.assertEqual(select_words("hello there", 0), ["hello"])

    def test_select_words_one_consonant(self):
        self.assertEqual(select_words("apple banana cherry", 1), ["banana", "cherry"])

    def test_select_words_multiple_consonants(self):
        self.assertEqual(select_words("python programming is fun", 3), ["programming"])

class OneHundredAndeighteenTest(unittest.TestCase):

    def test_single_vowel(self):
        self.assertEqual(get_closest_vowel("hello"), "e")

    def test_multiple_consonants_between_vowels(self):
        self.assertEqual(get_closest_vowel("testing"), "e")

    def test_no_vowels(self):
        self.assertEqual(get_closest_vowel("xyz"), "")

    def test_empty_string(self):
        self.assertEqual(get_closest_vowel(""), "")

    def test_short_word(self):
        self.assertEqual(get_closest_vowel("a"), "")

    def test_case_insensitive(self):
        self.assertEqual(get_closest_vowel("HELLO"), "E")

    def test_same_vowel_twice(self):
        self.assertEqual(get_closest_vowel("banana"), "a")
class OneHundredAndnineteenTest(unittest.TestCase):
    def test_match_parens(self):
        self.assertEqual(match_parens(['(', ')']), 'Yes')
        self.assertEqual(match_parens(['(', '(', ')']), 'Yes')
        self.assertEqual(match_parens([')', '(', ')']), 'Yes')
        self.assertEqual(match_parens([')', ')']), 'No')
        self.assertEqual(match_parens(['(', '(']), 'No')
        self.assertEqual(match_parens(['(', ')', ')']), 'Yes')
class One_hundred_and_twentyTest(unittest.TestCase):

    def test_maximum_empty_array(self):
        self.assertEqual(maximum([], 3), [])
    
    def test_maximum_k_equals_zero(self):
        self.assertEqual(maximum([4, 2, 7, 1], 0), [])
    
    def test_maximum_sorted_array(self):
        self.assertEqual(maximum([1, 2, 3, 4, 5], 2), [4, 5])
    
    def test_maximum_unsorted_array(self):
        self.assertEqual(maximum([9, 2, 7, 3, 1, 6], 3), [6, 7, 9])




class OneHundredAndTwentyOneTest(unittest.TestCase):

    def test_solution_with_odd_indices_and_odd_values(self):
        self.assertEqual(solution([1, 2, 3, 4, 5]), 9)

    def test_solution_with_no_odd_indices_and_odd_values(self):
        self.assertEqual(solution([2, 4, 6, 8]), 0)

    def test_solution_with_odd_indices_and_no_odd_values(self):
        self.assertEqual(solution([2, 1, 4, 3]), 1)

    def test_solution_with_no_odd_indices_and_no_odd_values(self):
        self.assertEqual(solution([2, 4, 6, 8, 10]), 0)


    

class OneHundredAndtwentyTwoTest(unittest.TestCase):

    def test_add_elements(self):
        self.assertEqual(add_elements([10, 100, 5, 500, 1000], 3), 115)
        self.assertEqual(add_elements([15, 25, 30, 150, 200], 4), 220)
        self.assertEqual(add_elements([1, 20, 300, 4000, 50000], 2), 21)

class OneHundredAndTwentyThreeTest(unittest.TestCase):

    def test_odd_collatz_odd_input(self):
        self.assertEqual(get_odd_collatz(3), [3, 10, 5, 16, 8, 4, 2, 1])

    def test_odd_collatz_even_input(self):
        self.assertEqual(get_odd_collatz(12), [])
  

class One_hundred_and_twenty_fourTest(unittest.TestCase):

    def test_valid_date_valid_input(self):
        self.assertTrue(valid_date('12-25-2021'))

    def test_valid_date_invalid_month(self):
        self.assertFalse(valid_date('13-25-2021'))

    def test_valid_date_invalid_day(self):
        self.assertFalse(valid_date('02-30-2021'))

    def test_valid_date_invalid_format(self):
        self.assertFalse(valid_date('02/15-2021'))

    def test_valid_date_invalid_input(self):
        self.assertFalse(valid_date('invalid_date'))

    def test_valid_date_empty_input(self):
        self.assertFalse(valid_date(''))

    def test_valid_date_missing_parts(self):
        self.assertFalse(valid_date('12-2021'))
  
 


class One_hundred_and_twenty_fiveTest(unittest.TestCase):
    
    def test_space_split(self):
        self.assertEqual(split_words("hello world"), ["hello", "world"])

    def test_comma_split(self):
        self.assertEqual(split_words("apple,banana,cherry"), ["apple", "banana", "cherry"])

    def test_single_word_lowercase_even_ord(self):
        self.assertEqual(split_words("hello"), 3)

    def test_single_word_all_upper(self):
        self.assertEqual(split_words("HELLO"), 0)

    def test_empty_string(self):
        self.assertEqual(split_words(""), 0)


    




class OneHundredAndtwentySixTest(unittest.TestCase):

    def test_is_sorted_empty(self):
        self.assertTrue(is_sorted([]))

    def test_is_sorted_single_element(self):
        self.assertTrue(is_sorted([5]))

    def test_is_sorted_sorted_list(self):
        self.assertTrue(is_sorted([1, 2, 3, 4, 5]))

    def test_is_sorted_unsorted_list(self):
        self.assertFalse(is_sorted([5, 3, 1, 4, 2]))

    def test_is_sorted_duplicates(self):
        self.assertFalse(is_sorted([1, 2, 2, 3, 4]))

    def test_is_sorted_no_duplicates(self):
        self.assertTrue(is_sorted([1, 2, 3, 4]))

    def test_is_sorted_edge_case(self):
        self.assertFalse(is_sorted([3, 3, 3]))
  

class One_hundred_and_twenty_sevenTest(unittest.TestCase):

    def test_intersection_prime_length(self):
        interval1 = (3, 7)
        interval2 = (5, 9)
        self.assertEqual(intersection(interval1, interval2), "YES")

    def test_intersection_non_prime_length(self):
        interval1 = (2, 5)
        interval2 = (6, 9)
        self.assertEqual(intersection(interval1, interval2), "NO")

    def test_intersection_negative_intervals(self):
        interval1 = (-10, 0)
        interval2 = (-5, 5)
        self.assertEqual(intersection(interval1, interval2), "YES")

    def test_intersection_overlapping_intervals(self):
        interval1 = (1, 10)
        interval2 = (5, 15)
        self.assertEqual(intersection(interval1, interval2), "NO")
  
class OneHundredAndtwentyEightTest(unittest.TestCase):

    def test_empty_input(self):
        self.assertIsNone(prod_signs([]))

    def test_positive_numbers_only(self):
        self.assertEqual(prod_signs([1, 2, 3]), sum([1, 2, 3]))

    def test_negative_numbers_only(self):
        self.assertEqual(prod_signs([-1, -2, -3]), -6)

    def test_mixed_numbers(self):
        self.assertEqual(prod_signs([1, -2, 3, -4]), -10)

class OneHundredAndtwentyNineTest(unittest.TestCase):

    def test_minPath(self):
        grid = [[1, 0], [0, 1]]
        k = 5
        self.assertEqual(minPath(grid, k), [1, 1, 1, 1, 1])

        grid = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
        k = 6
        self.assertEqual(minPath(grid, k), [1, 1, 1, 1, 1, 1])

        grid = [[1, 1], [0, 1]]
        k = 3
        self.assertEqual(minPath(grid, k), [1, 1, 1])
  
class OneHundredAndthirtyTest(unittest.TestCase):

    def test_tri_with_zero(self):
        self.assertEqual(tri(0), [1])

    def test_tri_with_positive_number(self):
        self.assertEqual(tri(5), [1, 3, 4.0, 7.0, 12.0, 21.0])
class OneHundredAndthirtyOneTest(unittest.TestCase):

    def test_all_even_digits(self):
        self.assertEqual(digits(2468), 0)

    def test_one_odd_digit(self):
        self.assertEqual(digits(2469), 9)

    def test_multiple_odd_digits(self):
        self.assertEqual(digits(13579), 105)

    def test_large_odd_digit(self):
        self.assertEqual(digits(987654321), 945)
class OneHundredAndthirtytwoTest(unittest.TestCase):

    def test_is_nested_returns_true_when_nested_brackets_exist(self):
        self.assertTrue(is_nested("[[abc]def]"))

    def test_is_nested_returns_false_when_no_nested_brackets_exist(self):
        self.assertFalse(is_nested("[abc]def"))



class One_hundred_and_thirty_threeTest(unittest.TestCase):
    
    def test_sum_squares_empty_list(self):
        self.assertEqual(sum_squares([]), 0)
        
    def test_sum_squares_positive_numbers(self):
        self.assertEqual(sum_squares([3, 4, 5]), 50)
        
    def test_sum_squares_negative_numbers(self):
        self.assertEqual(sum_squares([-3, -4, -5]), 50)
        
    def test_sum_sqaures_mixed_numbers(self):
        self.assertEqual(sum_squares([-2, 3, -4, 5]), 30)


    

class OneHundredAndthirtyFourTest(unittest.TestCase):
  
    def test_last_char_is_letter(self):
        self.assertTrue(check_if_last_char_is_a_letter("Hello World a"))
        self.assertTrue(check_if_last_char_is_a_letter("Python is fun Z"))
        
    def test_last_char_is_not_letter(self):
        self.assertFalse(check_if_last_char_is_a_letter("Hello World 1"))
        self.assertFalse(check_if_last_char_is_a_letter("Python is fun !"))
        self.assertFalse(check_if_last_char_is_a_letter(""))
        self.assertFalse(check_if_last_char_is_a_letter(" "))
        self.assertFalse(check_if_last_char_is_a_letter("1234"))

class One_hundred_and_thirty_fiveTest(unittest.TestCase):

    def test_can_arrange_sorted_array(self):
        result = can_arrange([1, 2, 3, 4, 5])
        self.assertEqual(result, -1)

    def test_can_arrange_unsorted_array(self):
        result = can_arrange([1, 3, 2, 4, 5])
        self.assertEqual(result, 2)

    def test_can_arrange_no_reverse_order(self):
        result = can_arrange([1, 2, 4, 3, 5])
        self.assertEqual(result, 3)

    def test_can_arrange_with_duplicates(self):
        result = can_arrange([1, 2, 3, 3, 5])
        self.assertEqual(result, -1)
  
class One_hundred_and_thirty_sixTest(unittest.TestCase):

    def test_largest_smallest_integers_positive_case(self):
        lst = [1, 5, -3, -10, 8, 0]
        self.assertEqual(largest_smallest_integers(lst), (-10, 1))

    def test_largest_smallest_integers_empty_list(self):
        lst = []
        self.assertEqual(largest_smallest_integers(lst), (None, None))

    def test_largest_smallest_integers_only_positive_nums(self):
        lst = [4, 7, 9, 1]
        self.assertEqual(largest_smallest_integers(lst), (None, 1))

    def test_largest_smallest_integers_only_negative_nums(self):
        lst = [-6, -3, -8, -2]
        self.assertEqual(largest_smallest_integers(lst), (-8, None))

    def test_largest_smallest_integers_mixed_values(self):
        lst = [-2, 0, 3, -5, 6]
        self.assertEqual(largest_smallest_integers(lst), (-5, 3))
class OneHundredAndthirtySevenTest(unittest.TestCase):

    def test_compare_one_both_integers(self):
        self.assertEqual(compare_one(1, 2), 2)

    def test_compare_one_both_floats(self):
        self.assertEqual(compare_one(1.0, 2.0), 2.0)

    def test_compare_one_first_string(self):
        self.assertEqual(compare_one("1.5", 2), 2)

    def test_compare_one_second_string(self):
        self.assertEqual(compare_one(1, "2.5"), 2.5)

    def test_compare_one_both_strings(self):
        self.assertIsNone(compare_one("1.5", "1.5"))

    def test_compare_one_strings_with_commas(self):
        self.assertIsNone(compare_one("3,2", "3.2"))



class OneHundredAndThirtyEightTest(unittest.TestCase):

    def test_is_equal_to_sum_even_true(self):
        self.assertTrue(is_equal_to_sum_even(8))
        self.assertTrue(is_equal_to_sum_even(10))
        self.assertTrue(is_equal_to_sum_even(12))
        self.assertTrue(is_equal_to_sum_even(138))

    def test_is_equal_to_sum_even_false(self):
        self.assertFalse(is_equal_to_sum_even(7))
        self.assertFalse(is_equal_to_sum_even(9))
        self.assertFalse(is_equal_to_sum_even(11))
        self.assertFalse(is_equal_to_sum_even(137))


    

class One_hundred_and_thirty_nineTest(unittest.TestCase):
    
    def test_special_factorial_1(self):
        self.assertEqual(special_factorial(0), 1)
    
    def test_special_factorial_2(self):
        self.assertEqual(special_factorial(1), 1)
    
    def test_special_factorial_3(self):
        self.assertEqual(special_factorial(5), 34560)
    
    def test_special_factorial_4(self):
        self.assertEqual(special_factorial(10), 66528003682)
class OneHundredAndfortyTest(unittest.TestCase):

    def test_fix_spaces_empty_string(self):
        self.assertEqual(fix_spaces(""), "")

    def test_fix_spaces_no_spaces(self):
        self.assertEqual(fix_spaces("abc"), "abc")

    def test_fix_spaces_single_space(self):
        self.assertEqual(fix_spaces("a b"), "a_b")

    def test_fix_spaces_multiple_spaces(self):
        self.assertEqual(fix_spaces("a  b   c"), "a_-b___c")

    def test_fix_spaces_start_end_spaces(self):
        self.assertEqual(fix_spaces(" b c "), "_b_c_")

class OneHundredAndfortyOneTest(unittest.TestCase):

    def test_file_name_check_valid(self):
        self.assertEqual(file_name_check('document.txt'), 'Yes')
        self.assertEqual(file_name_check('program.exe'), 'Yes')
        self.assertEqual(file_name_check('library.dll'), 'Yes')

    def test_file_name_check_invalid(self):
        self.assertEqual(file_name_check('.txt'), 'No')
        self.assertEqual(file_name_check('document.'), 'No')
        self.assertEqual(file_name_check('1234.exe'), 'No')
        self.assertEqual(file_name_check('doc1234.txt'), 'No')

class OneHundredAndfortyTwoTest(unittest.TestCase):
    def test_sum_squares_with_multiple_of_3(self):
        result = sum_squares([1, 2, 3])
        self.assertEqual(result, 10)

    def test_sum_squares_with_multiple_of_4_but_not_3(self):
        result = sum_squares([1, 2, 3, 4, 5, 6])
        self.assertEqual(result, 107)

    def test_sum_squares_with_neither_multiple_of_3_nor_4(self):
        result = sum_squares([1, 2, 3, 4, 5, 6, 7])
        self.assertEqual(result, 134)
class OneHundredAndfortyThreeTest(unittest.TestCase):

    def test_words_in_sentence(self):
        self.assertEqual(words_in_sentence("Hello world"), "world")
        self.assertEqual(words_in_sentence("Python is fun"), "is fun")
class One_hundred_and_forty_fourTest(unittest.TestCase):

    def test_simplify_correct_values(self):
        self.assertTrue(simplify("2/5", "1/2"))
        self.assertTrue(simplify("6/4", "3/2"))

    def test_simplify_incorrect_values(self):
        self.assertFalse(simplify("3/4", "2/3"))
        self.assertFalse(simplify("7/8", "4/5"))
class OneHundredAndfortyFiveTest(unittest.TestCase):

    def test_order_by_points_positive_numbers(self):
        self.assertEqual(order_by_points([123, 456, 789, 101]), [101, 123, 456, 789])

    def test_order_by_points_negative_numbers(self):
        self.assertEqual(order_by_points([-123, -456, -789]), [-789, -456, -123])

    def test_order_by_points_mixed_numbers(self):
        self.assertEqual(order_by_points([123, -456, 789, -101]), [-101, 123, -456, 789])
    
class OneHundredAndfortySixTest(unittest.TestCase):
    
    def test_specialFilter_emptyList(self):
        self.assertEqual(specialFilter([]), 0)
    
    def test_specialFilter_noNumbersGreaterThanTen(self):
        self.assertEqual(specialFilter([3, 5, 7, 9]), 0)
    
    def test_specialFilter_numbersGreaterThanTenButNotMeetingCriteria(self):
        self.assertEqual(specialFilter([12, 25, 39, 48]), 0)
    
    def test_specialFilter_numbersGreaterThanTenMeetingCriteria(self):
        self.assertEqual(specialFilter([13, 57, 91, 99]), 3)
  

class OneHundredAndfortySevenTest(unittest.TestCase):
    
    def test_get_max_triples(self):
        self.assertEqual(get_max_triples(3), 1)
        self.assertEqual(get_max_triples(5), 6)
        self.assertEqual(get_max_triples(7), 15)
        self.assertEqual(get_max_triples(0), 0)
        self.assertEqual(get_max_triples(1), 0)


    
  
class OneHundredAndfortyEightTest(unittest.TestCase):

    def test_within_same_index(self):
        self.assertEqual(bf("Mercury", "Mercury"), ())

    def test_planet1_not_in_list(self):
        self.assertEqual(bf("Pluto", "Mars"), ())

    def test_planet2_not_in_list(self):
        self.assertEqual(bf("Venus", "Pluto"), ())

    def test_planets_with_invalid_order(self):
        self.assertEqual(bf("Earth", "Mercury"), ())
        self.assertEqual(bf("Neptune", "Jupiter"), ())

    def test_planets_with_valid_order(self):
        self.assertEqual(bf("Mercury", "Venus"), ("Venus",))
        self.assertEqual(bf("Earth", "Mars"), ("Mars", "Jupiter"))

    def test_planets_with_reverse_order(self):
        self.assertEqual(bf("Venus", "Mercury"), ("Mercury",))
        self.assertEqual(bf("Mars", "Earth"), ("Venus", "Mercury"))



class OneHundredAndfortynineTest(unittest.TestCase):

    def test_sorted_list_sum(self):
        self.assertEqual(sorted_list_sum([ 'abcd', 'xy', 'zt', 'abcdefg' ]), ['xy', 'zt', 'abcd'])


    

unittest
class OneHundredAndFiftyTest(unittest.TestCase):

    def test_input_is_1(self):
        self.assertEqual(x_or_y(1, 'x', 'y'), 'y')

    def test_input_is_prime(self):
        self.assertEqual(x_or_y(7, 'x', 'y'), 'x')

    def test_input_is_not_prime(self):
        self.assertEqual(x_or_y(8, 'x', 'y'), 'y')

    def test_input_is_not_prime_multiple(self):
        self.assertEqual(x_or_y(9, 'x', 'y'), 'y')

    def test_input_is_not_prime_large(self):
        self.assertEqual(x_or_y(150, 'x', 'y'), 'y')
  



class OneHundredAndFiftyOneTest(unittest.TestCase):
    
    def test_double_the_difference(self):
        self.assertEqual(double_the_difference([1, 2, 3]), 10)
        self.assertEqual(double_the_difference([0, -3, 5]), 26)
        self.assertEqual(double_the_difference([-1, 4, 6]), 0)
        self.assertEqual(double_the_difference([1.5, 3, 5]), 34)

class One_hundred_and_fifty_twoTest(unittest.TestCase):
    
    def test_compare_same_length_lists(self):
        game = [1, 2, 3]
        guess = [1, 3, 5]
        expected = [0, 1, 2]
        self.assertEqual(compare(game, guess), expected)

    def test_compare_different_length_lists(self):
        game = [5, 10, 15]
        guess = [3, 9]
        expected = [2, 1]
        self.assertEqual(compare(game, guess), expected)

    def test_compare_empty_lists(self):
        game = []
        guess = []
        expected = []
        self.assertEqual(compare(game, guess), expected)

    def test_compare_negative_numbers(self):
        game = [-1, -5, -10]
        guess = [-3, -2, -8]
        expected = [2, 3, 2]
        self.assertEqual(compare(game, guess), expected)
  
class OneHundredAndfiftyThreeTest(unittest.TestCase):

    def test_example_case(self):
        self.assertEqual(Strongest_Extension("MyClass", ["ext1", "ext2", "Ext3"]), "MyClass.Ext3")

    def test_multiple_extensions_with_same_strength(self):
        self.assertEqual(Strongest_Extension("OtherClass", ["extA", "exta", "eXtB", "EXTC"]), "OtherClass.eXtB")

    def test_empty_extensions_list(self):
        self.assertEqual(Strongest_Extension("EmptyClass", []), "EmptyClass.")

class OneHundredAndfiftyFourTest(unittest.TestCase):

    def test_cycpattern_check_true(self):
        self.assertEqual(cycpattern_check("ABCDEF", "DEFABC"), True)

    def test_cycpattern_check_false(self):
        self.assertEqual(cycpattern_check("123456", "654321"), False)

    def test_cycpattern_check_empty_strings(self):
        self.assertEqual(cycpattern_check("", ""), False)

    def test_cycpattern_check_same_strings(self):
        self.assertEqual(cycpattern_check("hello", "hello"), False)


class OneHundredAndFiftyFiveTest(unittest.TestCase):

    def test_even_odd_count(self):
        self.assertEqual(even_odd_count(123456), (3, 3))
        self.assertEqual(even_odd_count(246810), (5, 0))
        self.assertEqual(even_odd_count(-13579), (0, 5))
        self.assertEqual(even_odd_count(0), (1, 0))


    
  
class OneHundredAndfiftySixTest(unittest.TestCase):

    def test_1_to_mini_roman(self):
        self.assertEqual(int_to_mini_roman(1), 'i')
    
    def test_5_to_mini_roman(self):
        self.assertEqual(int_to_mini_roman(5), 'v')
    
    def test_9_to_mini_roman(self):
        self.assertEqual(int_to_mini_roman(9), 'ix')
    
    def test_10_to_mini_roman(self):
        self.assertEqual(int_to_mini_roman(10), 'x')
    
    def test_20_to_mini_roman(self):
        self.assertEqual(int_to_mini_roman(20), 'xx')
    
    def test_40_to_mini_roman(self):
        self.assertEqual(int_to_mini_roman(40), 'xl')
    
    def test_50_to_mini_roman(self):
        self.assertEqual(int_to_mini_roman(50), 'l')
    
    def test_90_to_mini_roman(self):
        self.assertEqual(int_to_mini_roman(90), 'xc')
    
    def test_100_to_mini_roman(self):
        self.assertEqual(int_to_mini_roman(100), 'c')
    
    def test_400_to_mini_roman(self):
        self.assertEqual(int_to_mini_roman(400), 'cd')
    
    def test_500_to_mini_roman(self):
        self.assertEqual(int_to_mini_roman(500), 'd')
    
    def test_900_to_mini_roman(self):
        self.assertEqual(int_to_mini_roman(900), 'cm')
    
    def test_1000_to_mini_roman(self):
        self.assertEqual(int_to_mini_roman(1000), 'm')

class OneHundredAndfiftySevenTest(unittest.TestCase):

    def test_right_angle_triangle_true(self):
        self.assertTrue(right_angle_triangle(3, 4, 5))
        self.assertTrue(right_angle_triangle(5, 12, 13))
        self.assertTrue(right_angle_triangle(8, 15, 17))

    def test_right_angle_triangle_false(self):
        self.assertFalse(right_angle_triangle(1, 2, 3))
        self.assertFalse(right_angle_triangle(6, 8, 10))
        self.assertFalse(right_angle_triangle(5, 5, 5))


class OneHundredAndfiftyEightTest(unittest.TestCase):
    
    def test_find_max_empty_list(self):
        self.assertEqual(find_max([]), None)
        
    def test_find_max_single_word(self):
        self.assertEqual(find_max(['hello']), 'hello')
        
    def test_find_max_multiple_words_same_length(self):
        self.assertEqual(find_max(['cat', 'dog', 'bird']), 'cat')
        
    def test_find_max_multiple_words_different_lengths(self):
        self.assertEqual(find_max(['apple', 'banana', 'cherry']), 'banana')
        
    def test_find_max_special_characters(self):
        self.assertEqual(find_max(['!@#$', '1234', 'ABCD']), '!@$')
        
    def test_find_max_mixed_case(self):
        self.assertEqual(find_max(['apple', 'APPLE', 'Banana', 'banana']), 'Banana')
  
 
class OneHundredAndfiftyNineTest(unittest.TestCase):

    def test_need_less_than_remaining(self):
        result = eat(5, 3, 7)
        self.assertEqual(result, [8, 4])

    def test_need_equal_to_remaining(self):
        result = eat(10, 5, 5)
        self.assertEqual(result, [15, 0])

    def test_need_greater_than_remaining(self):
        result = eat(20, 15, 10)
        self.assertEqual(result, [30, 0])


class OneHundredAndSixtyTest(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(do_algebra(['+', '+'], [3, 4, 2]), 9)
        
    def test_subtraction(self):
        self.assertEqual(do_algebra(['-', '-'], [10, 2, 3]), 5)
        
    def test_multiplication(self):
        self.assertEqual(do_algebra(['*', '*'], [2, 3, 4]), 24)
        
    def test_division(self):
        self.assertEqual(do_algebra(['/', '/'], [20, 2, 2]), 5.0)
class OneHundredAndsixtyOneTest(unittest.TestCase):

    def test_only_numbers(self):
        self.assertEqual(solve("12345"), "54321")

    def test_only_uppercase(self):
        self.assertEqual(solve("HELLO"), "olleh")

    def test_only_lowercase(self):
        self.assertEqual(solve("world"), "DLROW")

    def test_mixed_case(self):
        self.assertEqual(solve("HeLLo"), "oLLEh")

    def test_empty_string(self):
        self.assertEqual(solve(""), "")

    def test_special_characters(self):
        self.assertEqual(solve("Hello123!"), "!321OLLEh")
                                         
class OneHundredAndsixtyTwoTest(unittest.TestCase):

    def test_string_to_md5_with_empty_text(self):
        self.assertIsNone(string_to_md5(''))

    def test_string_to_md5_with_non_empty_text(self):
        text = 'example'
        expected_output = '1a79a4d60de6718e8e5b326e338ae533'
        self.assertEqual(string_to_md5(text), expected_output)
                                                                                           

class OneHundredAndSixtyThreeTest(unittest.TestCase):

    def test_generate_integers_when_a_is_less_than_b(self):
        result = generate_integers(3, 7)
        self.assertEqual(result, [4, 6, 8])

    def test_generate_integers_when_a_is_greater_than_b(self):
        result = generate_integers(9, 5)
        self.assertEqual(result, [6, 8])

    def test_generate_integers_when_a_equals_b(self):
        result = generate_integers(4, 4)
        self.assertEqual(result, [4, 6, 8])

    def test_generate_integers_when_a_and_b_out_of_range(self):
        result = generate_integers(1, 9)
        self.assertEqual(result, [2, 4, 6, 8])

    def test_generate_integers_when_a_and_b_within_range(self):
        result = generate_integers(5, 6)
        self.assertEqual(result, [6])

