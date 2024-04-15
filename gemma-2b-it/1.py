# Generated code for task 2
def solution():
    ```
    **Test cases:**
    ```python
    import unittest
    
    class TestSeparateParentheses(unittest.TestCase):
    
        def test_valid_string(self):
            self.assertEqual(separate_paren_groups('( ) (( )) (( )( ))'), ['()', '(())', '(()())'])
    
        def test_empty_string(self):
            self.assertEqual(separate_paren_groups(''), [])
    
        def test_single_parenthesis(self):
            self.assertEqual(separate_paren_groups('()'), ['()'])
    
        def test_nested_parentheses(self):
            self.assertEqual(separate_paren_groups('( ( ) )'), ['()', '()']
    
        def test_string_with_multiple_groups(self):
            self.assertEqual(separate_paren_groups('( ) ( ( ) ( )'), ['()', '()(), ()()']
    
        def test_string_with_leading_and_trailing(self):
            self.assertEqual(separate_paren_groups(' ( ) ( ) ( )'), ['()', '()()', '()()', '']
    
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
