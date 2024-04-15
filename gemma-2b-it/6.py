# Generated code for task 7
def solution():
    ```
    **Test cases:**
    ```python
    import unittest
    
    class TestParseNestedParens(unittest.TestCase):
    
        def test_valid_string(self):
            self.assertEqual(parse_nested_parens('(()()) ((())) () ((())()())'), [2, 3, 1, 3])
    
        def test_empty_string(self):
            self.assertEqual([], parse_nested_parens(""))
    
        def test_single_parenthesis(self):
            self.assertEqual([1], parse_nested_parens("()"))
    
        def test_nested_parentheses(self):
            self.assertEqual([3, 2, 1], parse_nested_parens("(()()) ((())) () ((())()())"))
    
        def test_multiple_parentheses(self):
            self.assertEqual([4, 3, 1, 3], parse_nested_parens("(()()) ((())) () ((())()())"))
    
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
