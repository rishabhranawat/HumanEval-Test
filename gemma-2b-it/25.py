# Generated code for task 26
def solution():
    ```
    **Test cases:**
    ```python
    import unittest
    
    class TestFactorize(unittest.TestCase):
    
        def test_factorize_empty(self):
            self.assertEqual(factorize(0), [])
    
        def test_factorize_one(self):
            self.assertEqual(factorize(1), [1])
    
        def test_factorize_two(self):
            self.assertEqual(factorize(2), [2])
    
        def test_factorize_three(self):
            self.assertEqual(factorize(3), [1, 3])
    
        def test_factorize_six(self):
            self.assertEqual(factorize(6), [1, 2, 3])
    
        def test_factorize_eight(self):
            self.assertEqual(factorize(8), [2, 2, 2])
    
        def test_factorize_twentyfive(self):
            self.assertEqual(factorize(25), [5, 5])
    
        def test_factorize_seventy(self):
            self.assertEqual(factorize(70), [2, 5, 7])
    
        def test_factorize_ninety(self):
            self.assertEqual(factorize(90), [2, 3, 3, 5])
    
    if __name__ == '__main__':
        unittest.main()
    ```
    **Output:**
    ```
    ----------------------------------------------------------------------
    Ran 10 tests in 0.001s
    
    OK
    ```

# You can add tests or other function calls here.
