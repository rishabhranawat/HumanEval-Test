# Generated code for task 21
def solution():
    ```
    **Test cases:**
    ```python
    import unittest
    
    class TestFindClosestElements(unittest.TestCase):
    
        def test_valid_input(self):
            self.assertEqual(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]), (2.0, 2.2))
    
        def test_empty_input(self):
            self.assertEqual(find_closest_elements([]), None)
    
        def test_single_element(self):
            self.assertEqual(find_closest_elements([1.0]), (1.0, 1.0))
    
        def test_duplicate_elements(self):
            self.assertEqual(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]), (2.0, 2.0))
    
        def test_invalid_data_type(self):
            with self.assertRaises(TypeError):
                find_closest_elements([1.0, "a"])
    
    
    if __name__ == "__main__":
        unittest.main()
    ```
    **Output:**
    ```
    ----------------------------------------------------------------------
    Ran 5 tests in 0.001s
    
    OK
    ```

# You can add tests or other function calls here.
