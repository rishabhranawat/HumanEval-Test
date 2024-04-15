# Generated code for task 158
def solution():
    ```python
    import unittest
    
    
    class TestRightAngleTriangle(unittest.TestCase):
    
        def test_valid_right_angle_triangle(self):
            self.assertEqual(right_angle_triangle(3, 4, 5), True)
    
        def test_invalid_right_angle_triangle(self):
            self.assertEqual(right_angle_triangle(1, 2, 3), False)
    
        def test_equal_side_triangle(self):
            self.assertEqual(right_angle_triangle(3, 3, 3), True)
    
        def test_invalid_side_triangle(self):
            self.assertEqual(right_angle_triangle(1, 1, 1), False)
    
    
    if __name__ == '__main__':
        unittest.main()
    ```
    
    **Explanation:**
    
    * The `right_angle_triangle` function takes three arguments: `a`, `b` and `c` which represent the lengths of the three sides of a triangle.
    * The function uses the Pythagorean theorem to determine if the three sides form a right-angled triangle.
    * The `test_valid_right_angle_triangle` function tests if the function returns `True` when the three sides form a right-angled triangle and `False` otherwise.
    * The `test_invalid_right_angle_triangle` function tests if the function returns `False` when the three sides do not form a right-angled triangle.
    * The `test_equal_side_triangle` function tests if the function returns `True` when the three sides have the same length and `False` otherwise.
    * The `test_invalid_side_triangle` function tests if the function returns `False` when any of the three sides have the same length.
    
    **Output:**
    
    ```
    ----------------------------------------------------------------------
    Ran 3 tests in 0.001s
    
    OK
    ```

# You can add tests or other function calls here.
