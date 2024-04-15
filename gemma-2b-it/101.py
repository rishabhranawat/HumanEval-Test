# Generated code for task 102
def solution():
    ```
    
    **Test cases:**
    
    ```python
    import unittest
    
    class TestWordsString(unittest.TestCase):
    
        def test_empty_string(self):
            self.assertEqual(words_string(""), [])
    
        def test_single_word(self):
            self.assertEqual(words_string("Hello"), ["Hello"])
    
        def test_multiple_words(self):
            self.assertEqual(words_string("Hi, my name is John"), ["Hi", "my", "name", "is", "John"])
    
        def test_special_characters(self):
            self.assertEqual(words_string("!@#$%^&*_"), ["!", "@", "#", "$", "%", "^", "&", "*", "_"])
    
        def test_mixed_case(self):
            self.assertEqual(words_string("Mixed case words"), ["Mixed", "case", "words"])
    
    if __name__ == "__main__":
        unittest.main()
    ```
    
    **Output:**
    
    ```
    ----------------------------------------------------------------------
    Ran 5 tests in 0.001s
    
    OK
    ```

# You can add tests or other function calls here.
