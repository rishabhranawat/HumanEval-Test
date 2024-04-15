# Generated code for task 133
def solution():
    ```
    
    **Test cases:**
    ```python
    import unittest
    
    class Test(unittest.TestCase):
    
        def test_valid_string(self):
            self.assertEqual(is_nested('[[]]') , True)
    
        def test_invalid_string(self):
            self.assertEqual(is_nested('[]]]]]]]]][[[[[]') , False)
    
        def test_empty_string(self):
            self.assertEqual(is_nested(''), False)
    
        def test_single_open_and_close_bracket(self):
            self.assertEqual(is_nested('[][]'), False)
    
        def test_single_open_and_different_close_bracket(self):
            self.assertEqual(is_nested('[[]][['), True)
    
    if __name__ == '__main__':
        unittest.main()
    ```
    
    **Explanation:**
    * The `is_nested` function takes a string as input.
    * It initializes two lists, `opening_bracket_index` and `closing_bracket_index`, to keep track of the indices of the opening and closing brackets respectively.
    * It iterates through the string and adds the index of the opening bracket to `opening_bracket_index` and the index of the closing bracket to `closing_bracket_index`.
    * It reverses the `closing_bracket_index` to ensure they are sorted in reverse order.
    * It initializes a variable `cnt` to 0, which will keep track of the number of valid nested brackets.
    * It iterates through the `opening_bracket_index` and for each index, it checks if the current index is within the range of the `closing_bracket_index`. If it is, it increments `cnt` by 1.
    * Finally, it returns the value of `cnt`, which will be 2 if there are at least two valid nested brackets, and 0 otherwise.

# You can add tests or other function calls here.
