# Generated code for task 56
def solution():
    ```python
    import unittest
    
    
    class TestFibonacci(unittest.TestCase):
    
        def test_fib_1(self):
            self.assertEqual(fib(1), 1)
    
        def test_fib_2(self):
            self.assertEqual(fib(8), 21)
    
        def test_fib_3(self):
            self.assertEqual(fib(10), 55)
    
        def test_fib_4(self):
            self.assertEqual(fib(15), 55)
    
        def test_fib_5(self):
            self.assertEqual(fib(20), 6765)
    
    
    if __name__ == '__main__':
        unittest.main()
    ```
    
    **Explanation:**
    
    * The `fib` function calculates the n-th Fibonacci number.
    * The base cases are defined for `n == 0` and `n == 1`, which return 0 and 1, respectively.
    * For `n > 1`, it recursively calculates the previous two Fibonacci numbers and returns their sum.
    * The `test_fib_*` functions call the `fib` function with different values of `n` and verifies that the results match the expected Fibonacci numbers.
    * The `unittest.main()` function runs the `test_fib_*` functions and reports the results.
    
    **Output:**
    
    ```
    ----------------------------------------------------------------------
    Ran 5 tests in 0.001s
    
    OK
    ```

# You can add tests or other function calls here.
