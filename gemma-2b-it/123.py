# Generated code for task 124
def solution():
    ```
    **Test cases:**
    ```python
    import unittest
    
    class TestGetOddCollatz(unittest.TestCase):
    
        def test_empty_list(self):
            self.assertEqual(get_odd_collatz(0), [])
    
        def test_one(self):
            self.assertEqual(get_odd_collatz(1), [1])
    
        def test_two(self):
            self.assertEqual(get_odd_collatz(2), [1, 3])
    
        def test_three(self):
            self.assertEqual(get_odd_collatz(3), [1, 3, 5])
    
        def test_four(self):
            self.assertEqual(get_odd_collatz(4), [1, 3, 5, 7])
    
        def test_five(self):
            self.assertEqual(get_odd_collatz(5), [1, 5])
    
        def test_six(self):
            self.assertEqual(get_odd_collatz(6), [1, 3, 5, 7, 9])
    
        def test_seven(self):
            self.assertEqual(get_odd_collatz(7), [1, 3, 5, 7, 9, 11])
    
        def test_eight(self):
            self.assertEqual(get_odd_collatz(8), [1, 3, 5, 7, 9, 11, 13])
    
        def test_nine(self):
            self.assertEqual(get_odd_collatz(9), [1, 3, 5, 7, 9, 11, 13, 15])
    
        def test_ten(self):
            self.assertEqual(get_odd_collatz(10), [1, 3, 5, 7, 9, 11, 13, 15, 17])
    
    if __name__ == '__main__':
        unittest.main()
    ```

# You can add tests or other function calls here.
