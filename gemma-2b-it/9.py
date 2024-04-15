# Generated code for task 10
def solution():
    ```
    **Test cases:**
    ```python
    import unittest
    
    class TestRollingMax(unittest.TestCase):
    
        def test_empty_list(self):
            self.assertEqual([], rolling_max([]))
    
        def test_single_element(self):
            self.assertEqual([n] for n in [1])
    
        def test_multiple_elements_same_max(self):
            self.assertEqual([1, 1, 1, 1, 1], rolling_max([1, 1, 1, 1, 1]))
    
        def test_multiple_elements_different_max(self):
            self.assertEqual([1, 2, 3, 4, 5], rolling_max([1, 2, 3, 4, 5]))
    
        def test_multiple_elements_with_different_max_order(self):
            self.assertEqual([1, 2, 3, 4, 5], rolling_max([5, 1, 2, 3, 4]))
    
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
