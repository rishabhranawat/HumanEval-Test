# Generated code for task 109
def solution():
    ```python
    import unittest
    
    class Test(unittest.TestCase):
    
        def test_empty_array(self):
            self.assertEqual(count_nums([]), 0)
    
        def test_negative_numbers(self):
            self.assertEqual(count_nums([-1, 11, -11]), 1)
    
        def test_single_positive_number(self):
            self.assertEqual(count_nums([1, 1, 2]), 3)
    
        def test_multiple_positive_numbers(self):
            self.assertEqual(count_nums([1, 1, 2, 3]), 3)
    
        def test_negative_numbers_with_leading_zero(self):
            self.assertEqual(count_nums([-123, 456, 789]), 1)
    
        def test_all_digits_positive(self):
            self.assertEqual(count_nums([123, 456, 789]), 3)
    
    
    if __name__ == '__main__':
        unittest.main()
    ```
    
    **Explanation:**
    
    * The `count_nums` function takes an array of integers as input.
    * It defines another function `digits_sum` that takes an integer as input and returns the sum of the digits of that number.
    * The function first handles negative numbers by negating their value and then converts them to a list of integers.
    * It then iterates over the list of integers and adds the value of each element to the sum.
    * The function returns the count of elements in the input array that have a sum of digits greater than 0.
    * The `test_*` functions are unit tests that cover different scenarios, including empty arrays, negative numbers, single and multiple positive numbers, and numbers with leading zeros.

# You can add tests or other function calls here.
