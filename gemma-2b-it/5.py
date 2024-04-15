# Generated code for task 6
def solution():
    ```
    
    **Test cases:**
    ```python
    import unittest
    
    class TestIntersepe(unittest.TestCase):
    
        def test_empty_list(self):
            self.assertEqual(interse( [], 4), [])
    
        def test_single_element(self):
            self.assertEqual(interse([1], 4), [1])
    
        def test_multiple_elements(self):
            self.assertEqual(interse([1, 2, 3], 4), [1, 4, 2, 4, 3])
    
        def test_different_delimeters(self):
            self.assertEqual(interse([1, 2, 3], 2), [1, 2, 3])
    
    if __name__ == '__main__':
        unittest.main()
    ```
    
    **Output:**
    ```
    ----------------------------------------------------------------------
    Ran 3 tests in 0.001s
    
    OK
    ```

# You can add tests or other function calls here.
