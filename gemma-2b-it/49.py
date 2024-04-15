# Generated code for task 50
def solution():
    ```
    
    **Test cases:**
    
    ```python
    import unittest
    
    class TestModp(unittest.TestCase):
    
        def test_valid_inputs(self):
            self.assertEqual(modp(3, 5), 3)
            self.assertEqual(modp(1101, 101), 2)
            self.assertEqual(modp(0, 101), 1)
            self.assertEqual(modp(3, 11), 8)
            self.assertEqual(modp(100, 101), 1)
    
        def test_invalid_inputs(self):
            self.assertEqual(modp(-1, 5), 1)
            self.assertEqual(modp(5, 0), 0)
            self.assertEqual(modp(10, 11), 10)
    
    
    if __name__ == '__main__':
        unittest.main()
    ```
    
    **Explanation:**
    
    * The `modp` function takes two arguments: `n` and `p`.
    * It initializes `ret` to 1, as the result for 2^0 modulo `p` is always 1.
    * It iterates through the values of `i` from 0 to `n`.
    * For each value of `i`, it calculates `ret = (2 * ret) % p`.
    * Finally, it returns the value of `ret`.
    
    **Note:**
    
    * The `modp` function uses a dynamic approach to compute the result.
    * This can be inefficient for large values of `n` and `p`.
    * For better performance, it is recommended to use a different approach, such as the binary exponentiation trick.

# You can add tests or other function calls here.
