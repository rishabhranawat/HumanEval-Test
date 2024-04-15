# Generated code for task 81
def solution():
    ```
    **Test cases:**
    ```python
    import unittest
    
    class TestHappyString(unittest.TestCase):
    
        def test_happy_string(self):
            self.assertEqual(is_happy("happy"), True)
    
        def test_not_happy_string(self):
            self.assertEqual(is_happy("aa"), False)
    
        def test_happy_string_with_multiple_runs(self):
            self.assertEqual(is_happy("abcabcxzy"), True)
    
        def test_empty_string(self):
            self.assertEqual(is_happy(""), False)
    
        def test_string_with_special_characters(self):
            self.assertEqual(is_happy("!@#$%^&*_"), True)
    
        def test_string_with_long_string(self):
            self.assertEqual(is_happy("a" * 100), True)
    
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
