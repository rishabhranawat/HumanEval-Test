# Generated code for task 142
def solution():
    ```
    **Test cases:**
    ```python
    import unittest
    
    class TestFile(unittest.TestCase):
    
        def test_valid_file_name(self):
            self.assertEqual(file_name_check("example.txt"), "Yes")
    
        def test_invalid_file_name_1(self):
            self.assertEqual(file_name_check("1example.dll"), "No")
    
        def test_invalid_file_name_2(self):
            self.assertEqual(file_name_check("example.txt.txt"), "No")
    
        def test_valid_file_name_3(self):
            self.assertEqual(file_name_check("example.txt.exe"), "Yes")
    
        def test_valid_file_name_4(self):
            self.assertEqual(file_name_check("example.txt.dll"), "Yes")
    
        def test_empty_file_name(self):
            self.assertEqual(file_name_check(""), "No")
    
        def test_valid_file_name_with_digit(self):
            self.assertEqual(file_name_check("example.123.txt"), "No")
    
        def test_valid_file_name_with_dot(self):
            self.assertEqual(file_name_check("example.txt."), "Yes")
    
        def test_valid_file_name_with_suffix(self):
            self.assertEqual(file_name_check("example.txt.txt"), "Yes")
    
    if __name__ == "__main__":
        unittest.main()
    ```

# You can add tests or other function calls here.
