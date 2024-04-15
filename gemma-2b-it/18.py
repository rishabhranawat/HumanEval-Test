# Generated code for task 19
def solution():
    ```
    
    **Test cases:**
    ```python
    import unittest
    
    class TestHowManyTimes(unittest.TestCase):
    
        def test_empty_string_and_substring(self):
            self.assertEqual(how_many_times('', 'a'), 0)
    
        def test_multiple_occurrences(self):
            self.assertEqual(how_many_times('aaa', 'a'), 3)
    
        def test_equal_substring(self):
            self.assertEqual(how_many_times('aaaa', 'aa'), 3)
    
        def test_different_strings(self):
            self.assertEqual(how_many_times('hello', 'world'), 0)
    
    
    if __name__ == '__main__':
        unittest.main()
    ```
    
    **Explanation:**
    
    * The `how_many_times` function takes two arguments: the original string and the substring to find.
    * It initializes a variable `times` to 0. This variable will keep track of the number of times the substring appears in the original string.
    * The function iterates through the original string using a for loop.
    * For each position `i` in the string, it checks if the substring is a substring of the original string starting from position `i`. This is done with the condition `if string[i:i+len(substring)] == substring`.
    * If the substring is found, it increments the `times` variable by 1.
    * After the loop has finished, the function returns the final value of the `times` variable.
    
    **Note:**
    
    * The time complexity of this algorithm is O(n), where n is the length of the original string. This is because the function iterates through the string once to find all the occurrences of the substring.

# You can add tests or other function calls here.
