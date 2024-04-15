# Generated code for task 23
def solution():
    ```python
    def filter_integers(values: List[Any]) -> List[int]:
        """ Filter given list of any python values only for integers
        >>> filter_integers(['a', 3.14, 5])
        [5]
        >>> filter_integers([1, 2, 3, 'abc', {}, []])
        [1, 2, 3]
        """
        return [x for x in values if isinstance(x, int)]
    
    # Test the function
    print(filter_integers(['a', 3.14, 5]))
    print(filter_integers([1, 2, 3, 'abc', {}, []]))
    ```
    
    **Explanation:**
    
    1. The `filter_integers` function takes a list of any type as input.
    2. It uses a list comprehension to filter the input list.
    3. The `isinstance(x, int)` expression checks if the current element is an integer.
    4. If it is an integer, it is added to the output list.
    5. The function returns the output list at the end.
    
    **Output:**
    
    ```
    [5]
    [1, 2, 3]
    ```

# You can add tests or other function calls here.
