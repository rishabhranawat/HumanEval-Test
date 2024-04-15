# Generated code for task 64
def solution():
    ```python
    import unittest
    
    
    class TestFib(unittest.TestCase):
    
        def test_fib_0(self):
            self.assertEqual(fibfib(0), 0)
    
        def test_fib_1(self):
            self.assertEqual(fibfib(1), 0)
    
        def test_fib_2(self):
            self.assertEqual(fibfib(2), 1)
    
        def test_fib_3(self):
            self.assertEqual(fibfib(3), 1)
    
        def test_fib_4(self):
            self.assertEqual(fibfib(4), 2)
    
        def test_fib_5(self):
            self.assertEqual(fibfib(5), 4)
    
        def test_fib_8(self):
            self.assertEqual(fibfib(8), 24)
    
        def test_fib_10(self):
            self.assertEqual(fibfib(10), 120)
    
    
    if __name__ == '__main__':
        unittest.main()
    ```
    
    **Explanation:**
    
    * The `fibfib` function calculates the n-th element of the Fibonacci sequence.
    * The base cases handle the three initial values of the sequence: 0, 1, and 2.
    * For values of n greater than 2, the function recursively calculates the previous three Fibonacci numbers and returns the sum of these three numbers.
    * The `test_*` functions are unit tests that verify that the `fibfib` function works as expected.

# You can add tests or other function calls here.
