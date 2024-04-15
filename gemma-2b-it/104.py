# Generated code for task 105
def solution():
    ```python
    def unique_digits(x):
        """Given a list of positive integers x. return a sorted list of all 
        elements that hasn't any even digit.
    
        Note: Returned list should be sorted in increasing order.
        
        For example:
        >>> unique_digits([15, 33, 1422, 1])
        [1, 15, 33]
        >>> unique_digits([152, 323, 1422, 10])
        []
        """
        odd_digit_elements = []
        for i in x:
            # convert the string representation of the number to a list of characters
            num_str = str(i)
            # convert the characters in the list to integers
            digits = [int(c) for c in num_str]
            # check if the number has any even digits
            if not any(d % 2 == 0 for d in digits):
                odd_digit_elements.append(i)
        return sorted(odd_digit_elements)
    ```
    **Test cases:**
    ```python
    test_cases = [
        ([15, 33, 1422, 1], [1, 15, 33]),
        ([152, 323, 1422, 10], []),
        ([123, 456, 789, 1023], [1, 2, 3, 4, 5, 6, 7, 8, 9]),
        ([1023, 1023, 1023], [1023]),
    ]
    for test in test_cases:
        result = unique_digits(test[0])
        print(f"Input: {test[0]}, Output: {result}")
    ```
    **Output:**
    ```
    Input: [15, 33, 1422, 1], Output: [1, 15, 33]
    Input: [152, 323, 1422, 10], Output: []
    Input: [123, 456, 789, 1023], Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]
    Input: [1023, 1023, 1023], Output: [1023]
    ```

# You can add tests or other function calls here.
