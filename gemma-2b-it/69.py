# Generated code for task 70
def solution():
    ```python
    def search(lst):
        """
        You are given a non-empty list of positive integers. Return the greatest integer that is greater than 
        zero, and has a frequency greater than or equal to the value of the integer itself. 
        The frequency of an integer is the number of times it appears in the list.
        If no such a value exist, return -1.
        Examples:
            search([4, 1, 2, 2, 3, 1]) == 2
            search([1, 2, 2, 3, 3, 3, 4, 4, 4]) == 3
            search([5, 5, 4, 4, 4]) == -1
        """
    
        # Initialize the frequency array with 0s for all values from 0 to max(lst)
        frq = [0] * (max(lst) + 1)
    
        # Initialize the maximum frequency to the minimum value in the list
        max_freq = min(lst)
    
        # Update the frequency array
        for i in lst:
            frq[i] += 1
    
        # Find the index of the maximum frequency
        ans = -1
        for i in range(1, len(frq)):
            if frq[i] >= i:
                ans = i
                max_freq = frq[i]
    
        # Return the index of the maximum frequency
        return ans
    
    ```
    **Test cases:**
    ```python
    print(search([4, 1, 2, 2, 3, 1]))
    print(search([1, 2, 2, 3, 3, 3, 4, 4, 4]))
    print(search([5, 5, 4, 4, 4]))
    ```
    **Output:**
    ```
    2
    3
    -1
    ```

# You can add tests or other function calls here.
