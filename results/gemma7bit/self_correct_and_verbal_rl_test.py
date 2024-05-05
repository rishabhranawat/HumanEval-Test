import unittest
from unittest import TestCase


class Generated2Test:
    def test_truncate_number(self):
        self.assertEqual(truncate_number(5.0), 0.0)
        self.assertEqual(truncate_number(5.5), 0.0)
        self.assertEqual(truncate_number(6.0), 0.0)
        self.assertEqual(truncate_number(6.5), 1.0)

def truncate_number(num):
    return int(num) / float(num)



class Generated3Test:
    def test_below_zero(self):
        operations1 = [1, -2, 3, 4, -5]
        self.assertEqual(below_zero(operations1), True)

        operations2 = [1, 2, 3, 4, 5]
        self.assertEqual(below_zero(operations2), False)


class Generated4Test:
    def test_mean_absolute_deviation(self):
        numbers = [1, 2, 3, 4, 5]
        self.assertEqual(mean_absolute_deviation(numbers), 2.0)

    def test_mean_absolute_deviation_with_empty_list(self):
        self.assertEqual(mean_absolute_deviation([]), 0.0)

    def test_mean_absolute_deviation_with_one_element(self):
        numbers = [1]
        self.assertEqual(mean_absolute_deviation(numbers), 0.0)



class Generated5Test:
    def test_intersperse_empty(self):
        assert intersperse([], 0) == []

    def test_intersperse_single(self):
        assert intersperse([1], 0) == [1]

    def test_intersperse_multiple(self):
        assert intersperse([1, 2, 3], 2) == [1, 2, 2, 3]



class Generated7Test:
    def test_filter_by_substring(self):
        strings = ["abc", "bcd", "cde", "def"]
        substring = "bcd"
        expected_result = ["bcd"]
        assert filter_by_substring(strings, substring) == expected_result


class Generated8Test:
    def test_sum_product(self):
        numbers = [1, 2, 3, 4, 5]
        expected_sum_value = 16
        expected_prod_value = 120

        sum_value, prod_value = sum_product(numbers)

        self.assertEqual(sum_value, expected_sum_value)
        self.assertEqual(prod_value, expected_prod_value)


class Generated9Test:
    def test_rolling_max(self):
        numbers = [1, 2, 3, 4, 5]
        expected_result = [2, 3, 4, 5, 5]
        assert rolling_max(numbers) == expected_result

    def test_rolling_max_with_empty_list(self):
        numbers = []
        expected_result = []
        assert rolling_max(numbers) == expected_result

    def test_rolling_max_with_one_element(self):
        numbers = [1]
        expected_result = [1]
        assert rolling_max(numbers) == expected_result


class Generated10Test:
    def test_make_palindrome(self):
        self.assertEqual(make_palindrome("abcba"), "abcba")
        self.assertEqual(make_palindrome("abc"), "aba")
        self.assertEqual(make_palindrome("ababa"), "aba")


class Generated13Test:
    def test_greatest_common_divisor(self):
        self.assertEqual(greatest_common_divisor(12, 15), 3)
        self.assertEqual(greatest_common_divisor(12, 16), 4)
        self.assertEqual(greatest_common_divisor(2, 2), 2)


class Generated15Test:
    def test_string_sequence(self):
        self.assertEqual(string_sequence(0), '0')
        self.assertEqual(string_sequence(1), '0 1')
        self.assertEqual(string_sequence(2), '0 1 2')
        self.assertEqual(string_sequence(3), '0 1 2 3')


class Generated18Test:
    def test_how_many_times_with_empty_string(self):
        self.assertEqual(how_many_times("", ""), 0)

    def test_how_many_times_with_no_substring(self):
        self.assertEqual(how_many_times("abc", ""), 0)

    def test_how_many_times_with_substring_not_found(self):
        self.assertEqual(how_many_times("abc", "def"), 0)

    def test_how_many_times_with_substring_found_once(self):
        self.assertEqual(how_many_times("abc", "ab"), 1)

    def test_how_many_times_with_substring_found_twice(self):
        self.assertEqual(how_many_times("abc", "ab"), 2)



