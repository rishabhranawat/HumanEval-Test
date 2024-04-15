# Generated code for task 45
def solution():
    ```
    
    **Test cases:**
    ```python
    import unittest
    
    class TestChangeBase(unittest.TestCase):
    
        def test_valid_base_1(self):
            self.assertEqual(change_base(8, 3), '22')
    
        def test_valid_base_2(self):
            self.assertEqual(change_base(8, 2), '1000')
    
        def test_valid_base_3(self):
            self.assertEqual(change_base(7, 2), '111')
    
        def test_invalid_base(self):
            with self.assertRaises(ValueError):
                change_base(10, 1)
    
    if __name__ == '__main__':
        unittest.main()
    ```
    
    **Explanation:**
    
    * The `change_base` function takes two arguments: `x` and `base`.
    * It initializes an empty string `ret` to store the result.
    * The function uses a while loop to repeatedly divide `x` by `base` and append the remainder to `ret`.
    * The function converts each remainder to a string and prepend it to the result string.
    * The function returns the final result after the loop terminates.
    * The `test_valid_base_1`, `test_valid_base_2`, and `test_valid_base_3` methods test the function with different valid base values.
    * The `test_invalid_base` method raises a `ValueError` when `base` is 1, indicating an invalid base.
    * The `unittest.main()` function runs the unit tests and displays the results.

# You can add tests or other function calls here.
