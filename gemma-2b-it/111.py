# Generated code for task 112
def solution():
    ```
    **Test cases:**
    ```python
    import unittest
    
    class TestHistogram(unittest.TestCase):
    
        def test_empty_string(self):
            self.assertEqual(histogram(''), {})
    
        def test_single_character(self):
            self.assertEqual(histogram('a b c'), {'a': 1, 'b': 1, 'c': 1})
    
        def test_multiple_characters(self):
            self.assertEqual(histogram('a b b a'), {'a': 2, 'b': 2})
    
        def test_multiple_equal_occurrence(self):
            self.assertEqual(histogram('a b c a b'), {'a': 2, 'b': 2})
    
        def test_single_occurrence(self):
            self.assertEqual(histogram('a b c a b'), {'a': 2, 'b': 2})
    
        def test_string_with_only_whitespace(self):
            self.assertEqual(histogram('  '), {})
    
    if __name__ == '__main__':
        unittest.main()
    ```
    
    **Output:**
    ```
    ----------------------------------------------------------------------
    Ran 5 tests in 0.001s
    
    OK
    ```

# You can add tests or other function calls here.
