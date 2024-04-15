# Generated code for task 33
def solution():
    ```
    **Test cases:**
    ```python
    import unittest
    
    class Test(unittest.TestCase):
    
        def test_valid_poly(self):
            self.assertEqual(find_zero([1, 2]), -0.5)
            self.assertEqual(find_zero([-6, 11, -6, 1]), 1.0)
    
        def test_invalid_poly(self):
            self.assertEqual(find_zero([1, 3]), 0.0)
            self.assertEqual(find_zero([1, 2, 3]), 1.0)
    
        def test_empty_poly(self):
            self.assertEqual(find_zero([]), None)
    
        def test_single_zero(self):
            self.assertEqual(find_zero([1]), 0.0)
    
    if __name__ == '__main__':
        unittest.main()
    ```
    **Explanation:**
    * The `poly` function calculates the polynomial with the given coefficients and point.
    * The `find_zero` function uses a binary search to find the zero point of the polynomial.
    * The algorithm starts by initializing the begin and end variables to the minimum and maximum values of the search range, respectively.
    * The algorithm then repeatedly narrows the search range by checking the values of the polynomial at the begin and end points.
    * If the polynomial evaluated at the center point is positive, the begin point is updated to the center point.
    * Otherwise, the end point is updated to the center point.
    * The algorithm continues until the search range is sufficiently small or the difference between the begin and end points is less than a specified tolerance.
    * The function returns the value of the zero point.

# You can add tests or other function calls here.
