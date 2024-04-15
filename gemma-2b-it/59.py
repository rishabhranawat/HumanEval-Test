# Generated code for task 60
def solution():
    ```
    
    **Test cases:**
    
    ```python
    import unittest
    
    class Test(unittest.TestCase):
    
        def test_valid_prime(self):
            self.assertEqual(largest_prime_factor(13195), 29)
    
        def test_invalid_prime(self):
            self.assertEqual(largest_prime_factor(2048), 2)
    
        def test_find_largest_prime_factor(self):
            self.assertEqual(largest_prime_factor(255), 5)
            self.assertEqual(largest_prime_factor(1234567), 13)
    
    if __name__ == '__main__':
        unittest.main()
    ```
    
    **Explanation:**
    
    * The `is_prime` function is defined first to check if a number is prime.
    * The `largest_prime_factor` function then iterates through all numbers from 2 to `n`.
    * For each number `j`, it checks if it is a prime factor of `n` and if it is, it updates the `largest` variable to the maximum of its current value and `j`.
    * Finally, the function returns the value of `largest` after the loop completes.
    
    **Note:**
    
    * The time complexity of this algorithm is O(n log log(n)), where n is the input number.
    * This is a probabilistic algorithm, so it may not always find the largest prime factor of a number.

# You can add tests or other function calls here.
