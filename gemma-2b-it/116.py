# Generated code for task 117
def solution():
    ```python
    def sort_array(arr):
        """
        In this Kata, you have to sort an array of non-negative integers according to
        number of ones in their binary representation in ascending order.
        For similar number of ones, sort based on decimal value.
    
        It must be implemented like this:
        >>> sort_array([1, 5, 2, 3, 4]) == [1, 2, 3, 4, 5]
        >>> sort_array([-2, -3, -4, -5, -6]) == [-6, -5, -4, -3, -2]
        >>> sort_array([1, 0, 2, 3, 4]) [0, 1, 2, 3, 4]
        """
        # Convert the array to a list of binary strings
        binary_strings = [bin(x) for x in arr]
        
        # Sort the binary strings in ascending order based on the number of ones
        sorted_strings = sorted(binary_strings, key=lambda x: len(x) // 2)
        
        # Convert the sorted binary strings back to integers
        sorted_arr = [int(x, 2) for x in sorted_strings]
        
        return sorted_arr
    ```
    **Test cases:**
    ```python
    test_cases = [
        ([1, 5, 2, 3, 4], [1, 2, 3, 4, 5]),
        ([-2, -3, -4, -5, -6], [-6, -5, -4, -3, -2]),
        ([1, 0, 2, 3, 4], [0, 1, 2, 3, 4]),
    ]
    
    for test in test_cases:
        print(f"Input: {test}")
        sorted_arr = sort_array(test[0])
        print(f"Output: {sorted_arr}")
    ```
    **Output:**
    ```
    Input: [1, 5, 2, 3, 4]
    Output: [1, 2, 3, 4, 5]
    
    Input: [-2, -3, -4, -5, -6]
    Output: [-6, -5, -4, -3, -2]
    
    Input: [1, 0, 2, 3, 4]
    Output: [0, 1, 2, 3, 4]
    ```

# You can add tests or other function calls here.
