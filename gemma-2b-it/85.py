# Generated code for task 86
def solution():
    ```python
    def add(lst):
        """Given a non-empty list of integers lst. add the even elements that are at odd indices..
    
    
        Examples:
            add([4, 2, 6, 7]) ==> 2 
        """
        even_sum = sum([lst[i] for i in range(1, len(lst), 2) if lst[i]%2 == 0])
        return even_sum
    
    
    # Test the add function
    assert add([4, 2, 6, 7]) == 2
    assert add([1, 3, 5, 7]) == 6
    assert add([2, 4, 6, 8]) == 12
    ```
    
    **Explanation:**
    
    1. The `add` function takes a list of integers `lst` as input.
    2. It uses a list comprehension to filter the list of elements based on their indices.
    3. The `range(1, len(lst), 2)` function generates the indices of elements in the list, starting from 1 and incrementing by 2.
    4. The `if` statement checks if the element at the current index is even (divisible by 2) using the condition `lst[i]%2 == 0`.
    5. If the condition is true, it adds the element to the `even_sum` variable.
    6. Finally, the function returns the `even_sum` after calculating it.
    
    **Note:**
    
    The time complexity of this algorithm is O(n), where n is the length of the list. This is because it iterates over the list and adds each even element to the `even_sum` variable.

# You can add tests or other function calls here.
