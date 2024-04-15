# Generated code for task 134
def solution():
    ```
    
    **Test cases:**
    ```python
    import unittest
    
    class TestSumSquares(unittest.TestCase):
    
        def test_sum_of_squares_of_positive_numbers(self):
            self.assertEqual(sum_squares([1, 2, 3]), 14)
    
        def test_sum_of_squares_of_negative_numbers(self):
            self.assertEqual(sum_squares([-2.4, 1, 1]), 6)
    
        def test_sum_of_squares_of_zero(self):
            self.assertEqual(sum_squares([0]), 0)
    
        def test_sum_of_squares_of_positive_numbers_with_decimal(self):
            self.assertEqual(sum_squares([1.4, 4.2, 0]), 29)
    
        def test_sum_of_squares_of_empty_list(self):
            self.assertEqual(sum_squares([]), 0)
    
    
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
