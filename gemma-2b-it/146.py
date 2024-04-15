# Generated code for task 147
def solution():
    ```
    **Test cases:**
    ```python
    import unittest
    
    class TestSpecialFilter(unittest.TestCase):
    
        def test_valid_input(self):
            self.assertEqual(specialFilter([15, -73, 14, -15]), 1)
    
        def test_invalid_input(self):
            self.assertEqual(specialFilter([33, -2, -3, 45, 21, 109]), 2)
    
        def test_empty_list(self):
            self.assertEqual(specialFilter([]), 0)
    
    if __name__ == '__main__':
        unittest.main()
    ```
    
    **Explanation:**
    
    * The `specialFilter` function takes an array of numbers as input.
    * It initializes a variable `count` to 0. This variable will be used to keep track of the number of elements that meet the specified conditions.
    * The function iterates through each element in the input array `nums`.
    * For each element, it checks if the element is greater than 10 and both the first and last digits of the element are odd (1, 3, 5, 7, 9).
    * If the condition is met, it increments the `count` variable by 1.
    * After the loop has finished, the function returns the final value of the `count` variable.
    * The `unittest` module is used to define the test cases and run the tests.

# You can add tests or other function calls here.
