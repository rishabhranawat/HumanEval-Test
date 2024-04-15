# Generated code for task 15
def solution():
    ```python
    def all_prefixes(string: str) -> List[str]:
        """ Return list of all prefixes from shortest to longest of the input string
        >>> all_prefixes('abc')
        ['a', 'ab', 'abc']
        """
        result = []
        for i in range(1, len(string) + 1):
            prefix = string[:i]
            result.append(prefix)
        return result
    ```
    
    **Explanation:**
    
    1. The `all_prefixes` function takes a single argument, `string`, which is the string for which we want to find all prefixes.
    
    
    2. The function uses a `for` loop to iterate over the string.
    
    
    3. Inside the loop, we append the string slice starting at index `i` to the `result` list. The slice length is `i + 1` because we want to include the character in the prefix and the next characters in the string.
    
    
    4. After the loop has finished, the function returns the `result` list.
    
    
    5. The `all_prefixes` function can be used as follows:
    
    ```python
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    ```
    
    **Note:**
    
    The time complexity of this algorithm is O(n), where n is the length of the input string. This is because the function iterates over the string once to find all of its prefixes.

# You can add tests or other function calls here.
