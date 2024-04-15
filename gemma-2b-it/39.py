# Generated code for task 40
def solution():
    ```
    
    **Test cases:**
    
    ```python
    import unittest
    
    class TestPrimeFib(unittest.TestCase):
    
        def test_prime_fib_1(self):
            self.assertEqual(prime_fib(1), 2)
    
        def test_prime_fib_2(self):
            self.assertEqual(prime_fib(2), 3)
    
        def test_prime_fib_3(self):
            self.assertEqual(prime_fib(3), 5)
    
        def test_prime_fib_4(self):
            self.assertEqual(prime_fib(4), 13)
    
        def test_prime_fib_5(self):
            self.assertEqual(prime_fib(5), 89)
    
    if __name__ == '__main__':
        unittest.main()
    ```
    
    **Explanation:**
    
    * The `is_prime` function is used to check if a number is prime. It returns `False` for numbers less than 2 and `True` for numbers greater than 1.
    * The `prime_fib` function uses a generator expression to calculate the Fibonacci sequence up to the `n`-th term.
    * The generator expression uses the `f` list, which contains the first two Fibonacci numbers.
    * The function keeps track of the current position in the Fibonacci sequence and checks if it is a prime number at each step.
    * If a prime number is found, the function decrements `n` by the amount of the prime number and returns the final result.
    * The `test_prime_fib_*` functions call the `prime_fib` function with different values of `n` and verifies that the results are correct.

# You can add tests or other function calls here.
