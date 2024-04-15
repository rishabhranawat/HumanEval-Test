# Generated code for task 104
def solution():
    ```
    Here is the comprehensive test suite for the `rounded_avg` function:
    
    ```python
    import unittest
    
    
    class TestRoundedAvg(unittest.TestCase):
    
        def setUp(self):
            pass
    
        def test_valid_inputs(self):
            self.assertEqual(rounded_avg(1, 5), "0b11")
            self.assertEqual(rounded_avg(7, 5), "-1")
            self.assertEqual(rounded_avg(10, 20), "0b1111")
            self.assertEqual(rounded_avg(20, 33), "0b11010")
    
        def test_invalid_inputs(self):
            self.assertEqual(rounded_avg(0, 5), "-1")
            self.assertEqual(rounded_avg(5, 0), "-1")
            self.assertEqual(rounded_avg(10, 10), "-1")
            self.assertEqual(rounded_avg(20, 25), "-1")
    
    
    if __name__ == "__main__":
        unittest.main()
    ```
    
    This test suite covers the following scenarios:
    
    * Valid inputs with different values of n and m.
    * Invalid inputs with n or m being 0.
    * Special case of n being greater than m.
    
    The `rounded_avg` function is tested with various inputs to ensure that it is working correctly.

# You can add tests or other function calls here.
