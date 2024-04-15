# Generated code for task 103
def solution():
    ```
    
    **Test cases:**
    ```python
    import unittest
    
    class TestChooseNum(unittest.TestCase):
    
        def test_valid_inputs(self):
            self.assertEqual(choose_num(12, 15), 14)
            self.assertEqual(choose_num(13, 12), -1)
            self.assertEqual(choose_num(10, 10), 10)
    
        def test_invalid_inputs(self):
            self.assertEqual(choose_num(1, 2), -1)
            self.assertEqual(choose_num(3, 4), -1)
            self.assertEqual(choose_num(5, 6), -1)
    
    if __name__ == '__main__':
        unittest.main()
    ```
    
    **Explanation:**
    
    * The `choose_num` function takes two positive numbers, `x` and `y`, as input.
    * It first checks if `x` is greater than `y`. If it is, it returns `-1` since there is no biggest even integer in the range.
    * If `y` is even, it returns `y` itself.
    * If `x` is equal to `y`, it returns `-1` since there is no biggest even integer in the range.
    * Otherwise, it returns `y - 1` since the biggest even integer in the range is the one just less than `y`.
    
    **Note:**
    
    * The function assumes that `x` and `y` are positive integers. If either of them is negative, it will return `-1`.
    * The function uses the `if y % 2 == 0` condition to check if `y` is even. This is a common optimization for finding the biggest even integer in a range.

# You can add tests or other function calls here.
