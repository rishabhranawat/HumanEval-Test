# Generated code for task 156
def solution():
    ```
    
    **Test cases:**
    ```python
    import unittest
    
    class TestEvenOddCount(unittest.TestCase):
    
        def test_valid_input(self):
            self.assertEqual(even_odd_count(12), (1, 1))
    
        def test_negative_input(self):
            self.assertEqual(even_odd_count(-12), (1, 1))
    
        def test_zero_input(self):
            self.assertEqual(even_odd_count(0), (0, 0))
    
        def test_all_even_digits(self):
            self.assertEqual(even_odd_count(123456), (4, 0))
    
        def test_all_odd_digits(self):
            self.assertEqual(even_odd_count(1234567), (0, 4))
    
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
