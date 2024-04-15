# Generated code for task 98
def solution():
    ```python
    import unittest
    
    
    class TestMultiply(unittest.TestCase):
    
        def test_valid_multiply(self):
            self.assertEqual(multiply(148, 412), 16)
            self.assertEqual(multiply(19, 28), 72)
            self.assertEqual(multiply(2020, 1851), 0)
            self.assertEqual(multiply(14, -15), 20)
    
        def test_invalid_multiply(self):
            self.assertEqual(multiply(10, 10), 100)
            self.assertEqual(multiply(100, 100), 10000)
            self.assertEqual(multiply(1000, 1000), 1000000)
            self.assertEqual(multiply(-10, 10), -100)
    
    
    if __name__ == '__main__':
        unittest.main()
    ```
    
    **Explanation:**
    
    * The `multiply` function takes two integers as input.
    * It calculates the absolute value of the remainder of the division of the two numbers by 10.
    * If the result is positive, it is multiplied by the other number.
    * Otherwise, it is multiplied by -1.
    * The function returns the product of the two numbers.
    * The `test_valid_multiply` method tests the function with valid inputs.
    * The `test_invalid_multiply` method tests the function with invalid inputs.
    * The `unittest.main()` function runs the unit tests.

# You can add tests or other function calls here.
