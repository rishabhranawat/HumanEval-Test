# Generated code for task 36
def solution():
    ```python
    def max_element(l: list):
        """Return maximum element in the list.
    
        Args:
            l (list): The list of elements.
    
        Returns:
            int: The maximum element in the list.
        """
    
        # Initialize the maximum element to the first element of the list.
        m = l[0]
    
        # Iterate through the list.
        for e in l:
            # If the current element is greater than the maximum element, update the maximum element.
            if e > m:
                m = e
    
        # Return the maximum element.
        return m
    
    
    # Test the function.
    print(max_element([1, 2, 3]))
    print(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))
    ```
    
    **Output:**
    
    ```
    3
    123
    ```
    
    **Explanation:**
    
    * The `max_element` function takes a list of elements as input.
    * It initializes the maximum element to the first element of the list.
    * It then iterates through the list and updates the maximum element if it is greater than the current maximum element.
    * Finally, it returns the maximum element.

# You can add tests or other function calls here.
