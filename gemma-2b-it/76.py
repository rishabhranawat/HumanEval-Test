# Generated code for task 77
def solution():
    ```python
    import unittest
    
    
    class TestSimplePower(unittest.TestCase):
    
        def test_simple_power_true(self):
            self.assertEqual(is_simple_power(1, 4), True)
            self.assertEqual(is_simple_power(2, 2), True)
            self.assertEqual(is_simple_power(8, 2), True)
            self.assertEqual(is_simple_power(3, 2), False)
            self.assertEqual(is_simple_power(3, 1), False)
            self.assertEqual(is_simple_power(5, 3), False)
    
        def test_simple_power_false(self):
            self.assertEqual(is_simple_power(1, 1), False)
            self.assertEqual(is_simple_power(2, 3), False)
            self.assertEqual(is_simple_power(8, 4), False)
            self.assertEqual(is_simple_power(3, 5), False)
            self.assertEqual(is_simple_power(5, 1), False)
            self.assertEqual(is_simple_power(7, 6), False)
    
    
    if __name__ == '__main__':
        unittest.main()
    ```
    
    **Explanation:**
    
    * The `is_simple_power` function takes two arguments: `x` and `n`.
    * It first checks if `n` is equal to 1. If `n` is 1, it returns `True` if `x` is equal to 1 (since 1 is a simple power of 1).
    * Otherwise, it initializes a variable `power` to 1 and enters a `while` loop.
    * In the loop, it updates `power` to `power * n`.
    * If `power` reaches the value of `x`, it means that `x` is a simple power of `n`, and the function returns `True`.
    * If `power` never reaches `x`, it means that `x` cannot be expressed as a simple power of `n`, and the function returns `False`.
    
    **How to use the test suite:**
    
    * Run the `unittest` command: `python test_simple_power.py`
    * The test suite will run the `test_simple_power_true` and `test_simple_power_false` functions and print the results.

# You can add tests or other function calls here.
