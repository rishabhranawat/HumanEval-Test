# Generated code for task 136
def solution():
    ```python
    def can_arrange(arr):
        """
        :param arr: A list of integers.
        :return: The largest index of an element which is not greater than or
        equal to the element immediately preceding it. If no such element
        exists then return -1.
        """
        # Initialize the largest index to -1.
        ind = -1
    
        # Initialize the index of the current element to 1.
        i = 1
    
        # Iterate through the array.
        while i < len(arr):
            # If the current element is less than the element immediately
            # preceding it, update the largest index to the current index.
            if arr[i] < arr[i - 1]:
                ind = i
    
            # Increment the index of the current element.
            i += 1
    
        # Return the largest index of an element which is not greater than or
        # equal to the element immediately preceding it.
        return ind
    
    
    # Test the function.
    print(can_arrange([1, 2, 4, 3, 5]))  # Output: 3
    print(can_arrange([1, 2, 3]))  # Output: -1
    print(can_arrange([5, 4, 3, 2, 1]))  # Output: 4
    ```
    
    **Explanation:**
    
    * The `can_arrange` function takes a list of integers as input.
    * It initializes the `ind` variable to `-1`. `ind` will store the largest index of an element which is not greater than or equal to the element immediately preceding it.
    * It initializes the `i` variable to 1. `i` will store the index of the current element.
    * It iterates through the array using a while loop.
    * Inside the loop, it compares the current element to the element immediately preceding it. If the current element is less than the element immediately preceding it, it updates the `ind` variable to the current index.
    * It increments the index of the current element by 1 in each iteration.
    * After the loop, it returns the value of the `ind` variable.
    
    **Note:**
    
    The time complexity of the algorithm is O(n), where n is the length of the array. This is because the function iterates through the array once, and each element takes constant time to check.

# You can add tests or other function calls here.
