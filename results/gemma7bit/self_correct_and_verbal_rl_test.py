import unittest
from unittest import TestCase


class Generated0Test(unittest.TestCase):

    def setUp(self):
        self.numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
        self.threshold = 0.1

    def test_has_close_elements(self):
        self.assertTrue(has_close_elements(self.numbers, self.threshold))


class Generated1Test(unittest.TestCase):

    def setUp(self):
        self.paren_string = '(())(())'

    def test_separate_paren_groups(self):
        self.assertEqual(separate_paren_groups(self.paren_string), ['(())', '(())'])



class Generated2Test(unittest.TestCase):

    def test_truncate_number(self):
        self.assertEqual(truncate_number(5.0), 5.0)
        self.assertEqual(truncate_number(5.5), 5.0)
        self.assertEqual(truncate_number(6.0), 6.0)
        self.assertEqual(truncate_number(6.5), 6.0)



class Generated9Test(unittest.TestCase):

    def setUp(self):
        self.numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    def test_rolling_max(self):
        self.assertEqual(rolling_max(self.numbers), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])


class Generated10Test(unittest.TestCase):

    def setUp(self):
        self.string = 'abcba'

    def test_is_palindrome(self):
        self.assertEqual(is_palindrome(self.string), True)

    def test_make_palindrome(self):
        self.assertEqual(make_palindrome(self.string), 'abcba')



class Generated11Test(unittest.TestCase):

    def setUp(self):
        self.a = '1010'
        self.b = '1011'

    def test_string_xor(self):
        self.assertEqual(string_xor(self.a, self.b), '1011')

class Generated12Test(unittest.TestCase):

    def setUp(self):
        self.strings = ["abc", "abc", "bcd"]

    def test_longest(self):
        self.assertEqual(longest(self.strings), "abc")



class Generated13Test(unittest.TestCase):

    def setUp(self):
        self.a = 12
        self.b = 15

    def test_greatest_common_divisor(self):
        self.assertEqual(greatest_common_divisor(self.a, self.b), 3)

class Generated14Test(unittest.TestCase):

    def test_all_prefixes(self):
        string = "abc"
        result = all_prefixes(string)
        self.assertEqual(result, ["a", "ab", "abc"])

    def test_all_prefixes_empty(self):
        string = ""
        result = all_prefixes(string)
        self.assertEqual(result, [])

    def test_all_prefixes_single_character(self):
        string = "a"
        result = all_prefixes(string)
        self.assertEqual(result, ["a"])



class Generated15Test(unittest.TestCase):

    def test_string_sequence(self):
        self.assertEqual(string_sequence(0), '0')
        self.assertEqual(string_sequence(1), '0 1')
        self.assertEqual(string_sequence(2), '0 1 2')



class Generated16Test(unittest.TestCase):

    def test_count_distinct_characters(self):
        self.assertEqual(count_distinct_characters("abc"), 3)
        self.assertEqual(count_distinct_characters("aab"), 2)
        self.assertEqual(count_distinct_characters("aaab"), 2)



class Generated17Test(unittest.TestCase):

    def setUp(self):
        self.music_string = "o o| .| "

    def test_parse_music(self):
        self.assertEqual(parse_music(self.music_string), [4, 2, 1])

class Generated18Test(unittest.TestCase):

    def test_how_many_times(self):
        self.assertEqual(how_many_times("abc", "ab"), 2)
        self.assertEqual(how_many_times("abc", "ab"), 2)
        self.assertEqual(how_many_times("abc", "a"), 1)



class Generated18Test(unittest.TestCase):

    def test_how_many_times(self):
        self.assertEqual(how_many_times("abc", "ab"), 2)
        self.assertEqual(how_many_times("abc", "ab"), 2)
        self.assertEqual(how_many_times("abc", "a"), 1)

