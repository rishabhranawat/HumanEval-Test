# Generated code for task 129
def solution():
    ```
    Here is the comprehensive test suite for the `prod_signs` function:
    
    ```python
    import unittest
    
    
    class TestProdSigns(unittest.TestCase):
    
        def test_empty_array(self):
            self.assertEqual(prod_signs([]), None)
    
        def test_single_negative(self):
            self.assertEqual(prod_signs([0]), 0)
    
        def test_negative_product_positive_sum(self):
            self.assertEqual(prod_signs([-1, 2, 2, -4]), -9)
    
        def test_positive_product_negative_sum(self):
            self.assertEqual(prod_signs([1, 2, 3, 4]), 12)
    
        def test_all_negative(self):
            self.assertEqual(prod_signs([-1, -2, -3]), -6)
    
        def test_all_positive(self):
            self.assertEqual(prod_signs([1, 2, 3, 4]), 12)
    
    
    if __name__ == '__main__':
        unittest.main()
    ```

# You can add tests or other function calls here.
