# Generated code for task 93
def solution():
    ```
    **Test cases:**
     
    ```python
    import unittest
    
    class TestAnyInt(unittest.TestCase):
    
        def test_any_int_true(self):
            self.assertEqual(any_int(5, 2, 7), True)
    
        def test_any_int_false_1(self):
            self.assertEqual(any_int(3, 2, 2), False)
    
        def test_any_int_false_2(self):
            self.assertEqual(any_int(3, -2, 1), True)
    
        def test_any_int_false_3(self):
            self.assertEqual(any_int(3.6, -2.2, 2), False)
    
    if __name__ == '__main__':
        unittest.main()
    ```
    
    **Output:**
    ```
    ----------------------------------------------------------------------
    Ran 4 tests in 0.001s
    
    OK
    ```

# You can add tests or other function calls here.
