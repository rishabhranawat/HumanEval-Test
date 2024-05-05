import unittest
from unittest import TestCase

class Generated0Test:
    def test_has_close_elements(self):
        self.assertFalse(has_close_elements([], 0.1))
        self.assertFalse(has_close_elements([1.0], 0.1))
        self.assertFalse(has_close_elements([1.0, 2.0], 0.1))
        self.assertTrue(has_close_elements([1.0, 1.1], 0.1))
        self.assertFalse(has_close_elements([1.0, 2.0, 3.0, 4.0], 0.1))
        self.assertTrue(has_close_elements([1.0, 1.1, 2.0, 2.1], 0.1))
        self.assertFalse(has_close_elements([1.0, 2.0], 0.5))
        self.assertTrue(has_close_elements([1.0, 2.0], 0.1))


# class Generated1Test:
#     def test_separate_paren_groups(self):
#         self.assertEqual(separate_paren_groups(""), [])
#         self.assertEqual(separate_paren_groups("("), ["()"])
#         self.assertEqual(separate_paren_groups("(())"), ["()", "()"])
#         self.assertEqual(separate_paren_groups("(())(())"), ["()", "()", "()"])
#         self.assertEqual(separate_paren_groups("(())("), ["()", "()"])
#         self.assertEqual(separate_paren_groups("(()")), ["()"])
#         with self.assertRaises(ValueError):
#             separate_paren_groups("(abc")

class Generated2Test:
    def test_truncate_number(self):
        assert truncate_number(3.14) == 0.14
        assert truncate_number(0.5) == 0.5
        assert truncate_number(1.0) == 0.0
        assert truncate_number(-0.5) == -0.5
        assert truncate_number(-1.0) == -1.0
        assert truncate_number(3.14159) == 0.14159
        assert truncate_number(0.0) == 0.0
        assert truncate_number(1.5) == 0.5
        assert truncate_number(-1.5) == -0.5


class Generated3Test:
    def test_below_zero(self):
        operations = [1, 2, -3]
        self.assertTrue(below_zero(operations))

    def test_above_zero(self):
        operations = [1, 2, 3]
        self.assertFalse(below_zero(operations))

    def test_zero(self):
        operations = [0]
        self.assertFalse(below_zero(operations))

    def test_empty_list(self):
        operations = []
        self.assertFalse(below_zero(operations))


class Generated4Test(unittest.TestCase):
    def test_mean_absolute_deviation(self):
        numbers = [1, 2, 3, 4, 5]
        self.assertAlmostEqual(mean_absolute_deviation(numbers), 1.5811388300841898)

        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertAlmostEqual(mean_absolute_deviation(numbers), 2.25)

        numbers = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        self.assertAlmostEqual(mean_absolute_deviation(numbers), 2.25)

        numbers = [0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5]
        self.assertAlmostEqual(mean_absolute_deviation(numbers), 3.1666666666666665)


class Generated5Test:
    def test_intersperse_empty_list(self):
        self.assertEqual(intersperse([], 0), [])

    def test_intersperse_single_element_list(self):
        self.assertEqual(intersperse([1], 0), [1, 0])

    def test_intersperse_multi_element_list(self):
        self.assertEqual(intersperse([1, 2, 3], 0), [1, 0, 2, 0, 3])

    def test_intersperse_odd_delimiter(self):
        self.assertEqual(intersperse([1, 2, 3], 1), [1, 1, 2, 1, 3])

    def test_intersperse_even_delimiter(self):
        self.assertEqual(intersperse([1, 2, 3], 2), [1, 2, 2, 3])


class Generated6Test:
    def test_parse_nested_parens(self):
        assert parse_nested_parens("") == []
        assert parse_nested_parens("(3 4)") == [3, 4]
        assert parse_nested_parens("(3 (4 5) 6)") == [3, 4, 5, 6]
        assert parse_nested_parens("(3 (4 5) 6 (7 8))") == [3, 4, 5, 6, 7, 8]
        assert parse_nested_parens("(3 (4 5) 6 (7 8) (9))") == [3, 4, 5, 6, 7, 8, 9]
        assert parse_nested_parens("(3 (4 5) 6 (7 8) (9 (10)))") == [3, 4, 5, 6, 7, 8, 9, 10]
        assert parse_nested_parens("(3 (4 5) 6 (7 8) (9 (10) 11))") == [3, 4, 5, 6, 7, 8, 9, 10, 11]
        assert parse_nested_parens("(3 (4 5) 6 (7 8) (9 (10) 11) (12))") == [3, 4, 5, 6, 7, 8, 9, 10, 11, 12]


class Generated7Test:
    def test_empty_list(self):
        self.assertEqual(filter_by_substring([], ""), [])

    def test_single_element_list(self):
        self.assertEqual(filter_by_substring(["apple"], "a"), ["apple"])

    def test_multiple_elements_list(self):
        self.assertEqual(filter_by_substring(["apple", "banana", "cherry"], "a"), ["apple", "banana"])

    def test_substring_not_found(self):
        self.assertEqual(filter_by_substring(["apple", "banana", "cherry"], "d"), [])

    def test_substring_found_in_middle(self):
        self.assertEqual(filter_by_substring(["apple", "banana", "cherry"], "n"), ["banana"])

    def test_substring_found_at_end(self):
        self.assertEqual(filter_by_substring(["apple", "banana", "cherry"], "y"), ["cherry"])

    def test_substring_found_at_start(self):
        self.assertEqual(filter_by_substring(["apple", "banana", "cherry"], "a"), ["apple"])


class Generated8Test:
    def test_sum_product(self):
        assert sum_product([1, 2, 3]) == (6, 6)
        assert sum_product([4, 5, 6]) == (15, 120)
        assert sum_product([7, 8, 9]) == (24, 504)
        assert sum_product([1, 2, 3, 4, 5]) == (15, 120)
        assert sum_product([]) == (0, 1)


class Generated9Test:
    def test_empty_list(self):
        self.assertEqual(rolling_max([]), [])

    def test_single_element_list(self):
        self.assertEqual(rolling_max([1]), [1])

    def test_monotonic_increasing_list(self):
        self.assertEqual(rolling_max([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_monotonic_decreasing_list(self):
        self.assertEqual(rolling_max([5, 4, 3, 2, 1]), [5, 4, 3, 2, 1])

    def test_mixed_list(self):
        self.assertEqual(rolling_max([1, 3, 2, 4, 5, 2, 6]), [1, 3, 2, 4, 5, 6])

    def test_edge_cases(self):
        self.assertEqual(rolling_max([None]), [None])
        self.assertEqual(rolling_max([1, None, 2]), [1, None, 2])
        self.assertEqual(rolling_max([1, 2, None]), [1, 2, None])


class Generated10Test:
    def test_is_palindrome(self):
        self.assertTrue(is_palindrome("racecar"))
        self.assertTrue(is_palindrome("level"))
        self.assertTrue(is_palindrome("radar"))
        self.assertFalse(is_palindrome("hello"))
        self.assertFalse(is_palindrome("world"))

    def test_make_palindrome(self):
        self.assertEqual(make_palindrome("racecar"), "racecar")
        self.assertEqual(make_palindrome("hello"), "hello")
        self.assertEqual(make_palindrome("world"), "world")
        self.assertEqual(make_palindrome("level"), "level")
        self.assertEqual(make_palindrome("radar"), "radar")


class Generated11Test:
    def test_string_xor(self):
        assert string_xor("", "") == ""
        assert string_xor("a", "") == "a"
        assert string_xor("", "a") == "a"
        assert string_xor("a", "a") == ""
        assert string_xor("a", "b") == "c"
        assert string_xor("b", "a") == "c"
        assert string_xor("a", "c") == "e"
        assert string_xor("c", "a") == "e"
        assert string_xor("a", "e") == "f"
        assert string_xor("e", "a") == "f"
        assert string_xor("a", "f") == "g"
        assert string_xor("f", "a") == "g"
        assert string_xor("a", "g") == "h"
        assert string_xor("g", "a") == "h"
        assert string_xor("a", "h") == "i"
        assert string_xor("h", "a") == "i"
        assert string_xor("a", "i") == "j"
        assert string_xor("i", "a") == "j"
        assert string_xor("a", "j") == "k"
        assert string_xor("j", "a") == "k"
        assert string_xor("a", "k") == "l"
        assert string_xor("k", "a") == "l"
        assert string_xor("a", "l") == "m"
        assert string_xor("l", "a") == "m"
        assert string_xor("a", "m") == "n"
        assert string_xor("m", "a") == "n"
        assert string_xor("a", "n") == "o"
        assert string_xor("n", "a") == "o"
        assert string_xor("a", "o") == "p"
        assert string_xor("o", "a") == "p"
        assert string_xor("a", "p") == "q"
        assert string_xor("p", "a") == "q"
        assert string_xor("a", "q") == "r"
        assert string_xor("q", "a") == "r"
        assert string_xor("a", "r") == "s"
        assert string_xor("r", "a") == "s"
        assert string_xor("a", "s") == "t"
        assert string_xor("s", "a") == "t"
        assert string_xor("a", "t") == "u"
        assert string_xor("t", "a") == "u"
        assert string_xor("a", "u") == "v"
        assert string_xor("u", "a") == "v"
        assert string_xor("a", "v") == "w"
        assert string_xor("v", "a") == "w"
        assert string_xor("a", "w") == "x"
        assert string_xor("w", "a") == "x"
        assert string_xor("a", "x") == "y"
        assert string_xor("x", "a") == "y"
        assert string_xor("a", "y") == "z"
        assert string_xor("y", "a") == "z"
        assert string_xor("a", "z") == "a"
        assert string_xor("z", "a") == "a"


class Generated12Test:
    def test_empty_list(self):
        self.assertIsNone(longest([]))

    def test_single_string(self):
        self.assertEqual(longest(["hello"]), "hello")

    def test_multiple_strings(self):
        self.assertEqual(longest(["hello", "world", "foo"]), "world")

    def test_max_length(self):
        self.assertEqual(longest(["hello", "world", "fool"]), "world")

    def test_edge_cases(self):
        self.assertIsNone(longest(["", ""]))
        self.assertIsNone(longest(["", "hello"]))
        self.assertIsNone(longest(["hello", ""]))


class Generated13Test:
    def test_gcd_of_two_positive_integers(self):
        assert greatest_common_divisor(12, 15) == 3
    def test_gcd_of_two_negative_integers(self):
        assert greatest_common_divisor(-12, -15) == 3
    def test_gcd_of_positive_and_negative_integers(self):
        assert greatest_common_divisor(12, -15) == 3
    def test_gcd_of_zero_and_nonzero_integer(self):
        assert greatest_common_divisor(0, 15) == 0
    def test_gcd_of_nonzero_integer_and_zero(self):
        assert greatest_common_divisor(15, 0) == 0
    def test_gcd_of_two_equal_integers(self):
        assert greatest_common_divisor(15, 15) == 15
    def test_gcd_of_two_consecutive_integers(self):
        assert greatest_common_divisor(14, 15) == 1
    def test_gcd_of_two_large_integers(self):
        assert greatest_common_divisor(1000, 1001) == 1


class Generated14Test:
    def test_empty_string(self):
        self.assertEqual(all_prefixes(""), [])

    def test_single_character_string(self):
        self.assertEqual(all_prefixes("a"), ["a"])

    def test_string_with_multiple_characters(self):
        self.assertEqual(all_prefixes("hello"), ["h", "he", "hel", "hello"])

    def test_string_with_duplicate_characters(self):
        self.assertEqual(all_prefixes("hello world"), ["h", "he", "hel", "hello", "world"])

    def test_string_with_null_character(self):
        self.assertEqual(all_prefixes("\0hello"), ["\0", "\0h", "\0he", "\0hel", "\0hello"])


class Generated15Test:
    def test_string_sequence(self):
        self.assertEqual(string_sequence(1), "1")
        self.assertEqual(string_sequence(2), "1 2")
        self.assertEqual(string_sequence(3), "1 2 3")
        self.assertEqual(string_sequence(4), "1 2 3 4")
        self.assertEqual(string_sequence(5), "1 2 3 4 5")
        self.assertEqual(string_sequence(6), "1 2 3 4 5 6")
        self.assertEqual(string_sequence(7), "1 2 3 4 5 6 7")
        self.assertEqual(string_sequence(8), "1 2 3 4 5 6 7 8")
        self.assertEqual(string_sequence(9), "1 2 3 4 5 6 7 8 9")
        self.assertEqual(string_sequence(10), "1 2 3 4 5 6 7 8 9 10")


class Generated16Test:
    def test_empty_string(self):
        self.assertEqual(count_distinct_characters(""), 0)
    
    def test_string_with_only_lowercase_letters(self):
        self.assertEqual(count_distinct_characters("a"), 1)
    
    def test_string_with_only_uppercase_letters(self):
        self.assertEqual(count_distinct_characters("A"), 1)
    
    def test_string_with_mixed_case_letters(self):
        self.assertEqual(count_distinct_characters("aMpLe"), 3)
    
    def test_string_with_duplicate_letters(self):
        self.assertEqual(count_distinct_characters("aabb"), 3)
    
    def test_string_with_non_ascii_characters(self):
        self.assertEqual(count_distinct_characters("a\u00e9"), 2)


class Generated17Test:
    def test_parse_music(self):
        assert parse_music("o o| .|") == [4, 2, 1]
        assert parse_music("o| .| o") == [2, 1, 4]
        assert parse_music(".| o o") == [1, 4, 2]
        assert parse_music("o o o|") == [4, 4, 2]
        assert parse_music("o| .| o|") == [2, 1, 4, 2]
        assert parse_music("o| o| .|") == [2, 4, 1, 2]
        assert parse_music(".| o| o") == [1, 2, 4]
        assert parse_music(".| o o|") == [1, 4, 2]
        assert parse_music("o| .| .|") == [2, 1, 1]
        assert parse_music("o| .| o|") == [2, 1, 4]
        assert parse_music("o| o| .|") == [2, 4, 1]
        assert parse_music("o| o| o|") == [2, 4, 2]
        assert parse_music(".| .| o") == [1, 1, 4]
        assert parse_music(".| o| .") == [1, 2, 1]
        assert parse_music(".| o| o") == [1, 2, 4]
        assert parse_music(".| o| o|") == [1, 2, 4, 2]
        assert parse_music("o| .| .") == [2, 1, 1]
        assert parse_music("o| .| o") == [2, 1, 4]
        assert parse_music("o| o| .") == [2, 4, 1]
        assert parse_music("o| o| o") == [2, 4, 2]
        assert parse_music("o| o| o|") == [2, 4, 2, 2]


class Generated18Test:
    def test_empty_string(self):
        self.assertEqual(how_many_times("", ""), 0)
    
    def test_empty_substring(self):
        self.assertEqual(how_many_times("hello", ""), 0)
    
    def test_single_match(self):
        self.assertEqual(how_many_times("hello", "h"), 1)
    
    def test_multi_match(self):
        self.assertEqual(how_many_times("hellohello", "h"), 2)
    
    def test_no_match(self):
        self.assertEqual(how_many_times("hello", "a"), 0)
    
    def test_edge_cases(self):
        self.assertEqual(how_many_times("", "h"), 0)
        self.assertEqual(how_many_times("h", ""), 0)
        self.assertEqual(how_many_times("hello", "hel"), 1)
        self.assertEqual(how_many_times("hello", "lo"), 1)


class Generated19Test:
    def test_sort_numbers(self):
        assert sort_numbers("zero one two three four five six seven eight nine") == "zero one two three four five six seven eight nine"
        assert sort_numbers("nine eight seven six five four three two one zero") == "zero one two three four five six seven eight nine"
        assert sort_numbers("three two one zero") == "zero one two three"
        assert sort_numbers("five four six seven eight nine three two one zero") == "zero one two three four five six seven eight nine"
        assert sort_numbers("one zero two three four five six seven eight nine") == "zero one two three four five six seven eight nine"
        assert sort_numbers("seven six five four three two one zero") == "zero one two three four five six seven eight nine"
        assert sort_numbers("two one zero three four five six seven eight nine") == "zero one two three four five six seven eight nine"
        assert sort_numbers("eight seven six five four three two one zero") == "zero one two three four five six seven eight nine"
        assert sort_numbers("six five four three two one zero") == "zero one two three four five six seven eight nine"
        assert sort_numbers("four three two one zero") == "zero one two three four five six seven eight nine"
        assert sort_numbers("nine eight seven six five four three two one zero") == "zero one two three four five six seven eight nine"

