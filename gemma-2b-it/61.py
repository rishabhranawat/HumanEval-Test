# Generated code for task 62
def solution():
    ```
    
    **Test cases:**
    
    ```python
    import unittest
    
    class Test(unittest.TestCase):
    
        def test_correct_bracketing(self):
            self.assertEqual(correct_bracketing("("), False)
            self.assertEqual(correct_bracketing(")"), True)
            self.assertEqual(correct_bracketing("(()())"), True)
            self.assertEqual(correct_bracketing(")(()")), False
    
    if __name__ == "__main__":
        unittest.main()
    ```
    
    **Explanation:**
    
    * The `correct_bracketing` function takes a string of brackets as input.
    * It initializes a variable `depth` to 0. This variable keeps track of the depth of the current bracket in the string.
    * The function iterates over the string and adds 1 to `depth` whenever it encounters an opening bracket `("`.
    * It subtracts 1 from `depth` whenever it encounters a closing bracket `)".
    * If the `depth` ever becomes negative, it means that there are more closing brackets than opening brackets, and the function returns `False`.
    * If the `depth` reaches 0 after the traversal, it means that all opening and closing brackets have found their matching counterparts, and the function returns `True`.
    
    **Note:**
    
    * The function assumes that the input string only contains opening and closing brackets.
    * It does not handle invalid strings, such as those with missing brackets or unbalanced parentheses.

# You can add tests or other function calls here.
