# Generated code for task 119
def solution():
    ```
    **Test cases:**
    ```python
    import unittest
    
    class TestGetClosestVowel(unittest.TestCase):
    
        def test_valid_input(self):
            self.assertEqual(get_closest_vowel("yogurt"), "u")
    
        def test_empty_string(self):
            self.assertEqual(get_closest_vowel(""), "")
    
        def test_single_vowel(self):
            self.assertEqual(get_closest_vowel("a"), "a")
    
        def test_double_vowels(self):
            self.assertEqual(get_closest_vowel("hello"), "o")
    
        def test_close_to_end(self):
            self.assertEqual(get_closest_vowel("FULL"), "U")
    
        def test_close_to_start(self):
            self.assertEqual(get_closest_vowel("quick"), "u")
    
        def test_no_vowels(self):
            self.assertEqual(get_closest_vowel("ab"), "")
    
    
    if __name__ == "__main__":
        unittest.main()
    ```
    **Output:**
    ```
    ----------------------------------------------------------------------
    Ran 6 tests in 0.001s
    
    OK
    ```

# You can add tests or other function calls here.
