# Generated code for task 59
def solution():
    ```
    
    **Test cases:**
    
    ```python
    import unittest
    
    class TestCommon(unittest.TestCase):
    
        def test_common_empty(self):
            self.assertEqual(common([], []), [])
    
        def test_common_single(self):
            self.assertEqual(common([1], [1]), [1])
    
        def test_common_multiple(self):
            self.assertEqual(common([1, 2, 3, 4, 5], [1, 2, 3]), [1, 2, 3])
    
        def test_common_duplicate(self):
            self.assertEqual(common([1, 2, 3, 4, 5], [2, 3, 4]), [2, 3, 4])
    
        def test_common_sorted(self):
            self.assertEqual(common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121]), [1, 5, 653])
    
    
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
