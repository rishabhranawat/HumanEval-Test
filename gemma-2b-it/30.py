# Generated code for task 31
def solution():
    ```python
    def get_positive(l: list):
        """Return only positive numbers in the list.
    
        Args:
            l (list): The list of numbers to filter.
    
        Returns:
            list: The list of positive numbers in the input list.
        """
    
        # Create a new list to store the positive numbers.
        positive_numbers = []
    
        # Iterate through the input list.
        for e in l:
            # If the current element is positive, add it to the list.
            if e > 0:
                positive_numbers.append(e)
    
        # Return the list of positive numbers.
        return positive_numbers
    
    
    # Test the function.
    print(get_positive([-1, 2, -4, 5, 6]))
    print(get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))
    ```
    
    **Output:**
    
    ```
    [2, 5, 6]
    [5, 3, 2, 3, 9, 123, 1]
    ```

# You can add tests or other function calls here.
