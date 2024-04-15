# Generated code for task 113
def solution():
    ```python
    def reverse_delete(s, c):
        """
        :type s: str
        :type c: str
        :rtype: tuple
        """
        # Create a new string with the characters from s that are not in c
        result = ''.join([char for char in s if char not in c])
        # Check if the result string is palindrome
        return (result, result[::-1] == result)
    ```
    **Example Usage:**
    ```python
    print(reverse_delete("abcde", "ae"))
    print(reverse_delete("abcdef", "b"))
    print(reverse_delete("abcdedcba", "ab"))
    ```
    **Output:**
    ```
    ('bcd', False)
    ('acdef', False)
    ('cdedc', True)
    ```

# You can add tests or other function calls here.
