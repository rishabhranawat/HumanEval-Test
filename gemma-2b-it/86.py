# Generated code for task 87
def solution():
    ```python
    import unittest
    
    class TestAntiShuffle(unittest.TestCase):
    
        def test_empty_string(self):
            self.assertEqual(anti_shuffle(''), '', 'Empty string should return itself')
    
        def test_single_word(self):
            self.assertEqual(anti_shuffle('hello'), 'hello', 'Single word should be preserved')
    
        def test_mixed_case_words(self):
            self.assertEqual(anti_shuffle('HELLO WORLD!!!'), 'Hello !!!Wdlor', 'Mixed case words should be preserved')
    
        def test_special_characters(self):
            self.assertEqual(anti_shuffle('!@#$%^&*_'), '!@#$%^&*_', 'Special characters should be preserved')
    
        def test_multiple_spaces(self):
            self.assertEqual(anti_shuffle('hello world'), 'hello world', 'Multiple spaces should be preserved')
    
        def test_leading_trailing_spaces(self):
            self.assertEqual(anti_shuffle('  hello  world  '), '  hello  world  ', 'Leading and trailing spaces should be preserved')
    
    
    if __name__ == '__main__':
        unittest.main()
    ```
    
    **Explanation:**
    
    * The `anti_shuffle` function takes a string as input.
    * It uses the `split()` method to split the string into a list of words.
    * The function then uses a list comprehension to join the words back together in an ordered manner, based on the ASCII value of the characters in the words.
    * The function uses the `sorted()` function to sort the characters in each word in ascending order.
    * The function then joins the sorted characters back together into a string, using the `join()` method.
    * The function returns the ordered string.
    
    **Note:**
    
    * The function preserves the order of words and blank spaces in the sentence.
    * It also preserves special characters, but they are inserted between words in the output string.

# You can add tests or other function calls here.
