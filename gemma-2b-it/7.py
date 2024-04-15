# Generated code for task 8
def solution():
    ```python
    def filter_by_substring(strings: List[str], substring: str) -> List[str]:
        """ Filter an input list of strings only for ones that contain given substring
        Args:
            strings (List[str]): The input list of strings.
            substring (str): The substring to search for.
    
        Returns:
            List[str]: The list of strings that contain the substring.
        """
        # Check if the substring is in any of the strings in the list
        filtered_strings = [x for x in strings if substring in x]
        return filtered_strings
    ```
    
    **Test cases:**
    ```python
    # Test cases
    test_cases = [
        ([], 'a'),
        (['abc', 'bacd', 'cde', 'array'], 'a'),
        (['hello', 'world', 'python'], 'world'),
        (['a', 'b', 'c', 'd', 'e', 'f'], 'c'),
    ]
    for test in test_cases:
        result = filter_by_substring(test[0], test[1])
        assert result == test[1]
    ```

# You can add tests or other function calls here.
