# Generated code for task 137
def solution():
    ```python
    def largest_smallest_integers(lst):
        """
        Create a function that returns a tuple (a, b), where 'a' is the
        largest of negative integers, and 'b' is the smallest
        of positive integers in a list.
        If there is no negative or positive integers, return them as None.
    
        Examples:
        largest_smallest_integers([2, 4, 1, 3, 5, 7]) == (None, 1)
        largest_smallest_integers([]) == (None, None)
        largest_smallest_integers([0]) == (None, None)
        """
    
        # Find the smallest negative integer in the list
        smallest = list(filter(lambda x: x < 0, lst))
    
        # Find the largest positive integer in the list
        largest = list(filter(lambda x: x > 0, lst))
    
        # Return the tuple of largest and smallest integers
        return (max(smallest) if smallest else None, min(largest) if largest else None)
    ```
    
    **Test cases:**
    ```python
    test_cases = [
        ([2, 4, 1, 3, 5, 7], (None, 1)),
        ([], (None, None),
        ([0], (None, None),
    ]
    for test in test_cases:
        result = largest_smallest_integers(test[0])
        assert result == test[1]
    ```

# You can add tests or other function calls here.
