# Generated code for task 71
def solution():
    ```
    
    **Test cases:**
    ```python
    import unittest
    
    class TestStrangeSort(unittest.TestCase):
    
        def test_empty_list(self):
            self.assertEqual(strange_sort_list([]), [])
    
        def test_single_element(self):
            self.assertEqual(strange_sort_list([1]), [1])
    
        def test_duplicate_elements(self):
            self.assertEqual(strange_sort_list([1, 1, 2]), [1, 2, 1])
    
        def test_different_min_max_values(self):
            self.assertEqual(strange_sort_list([5, 5, 5, 5]), [5, 5, 5, 5])
    
        def test_negative_values(self):
            self.assertEqual(strange_sort_list([-1, 2, 3]), [-1, 2, 3])
    
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
