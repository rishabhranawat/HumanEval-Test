# Generated code for task 101
def solution():
    ```python
    def make_a_pile(n):
        """
        Given a positive integer n, you have to make a pile of n levels of stones.
        The first level has n stones.
        The number of stones in the next level is:
            - the next odd number if n is odd.
            - the next even number if n is even.
        Return the number of stones in each level in a list, where element at index
        i represents the number of stones in the level (i+1).
    
        Examples:
        >>> make_a_pile(3)
        [3, 5, 7]
        """
        # Create a list of the number of stones in each level
        levels = [n + 2 * i for i in range(n)]
        return levels
    
    
    # Test the function
    print(make_a_pile(3))
    ```
    
    **Output:**
    
    ```
    [3, 5, 7]
    ```
    
    **Explanation:**
    
    * The `make_a_pile` function takes a positive integer `n` as input.
    * It initializes a list called `levels` to store the number of stones in each level of the pile.
    * The first level has `n` stones.
    * The number of stones in the next level is odd if `n` is odd and even if `n` is even.
    * The function returns the list of `levels` after calculating the number of stones in each level.

# You can add tests or other function calls here.
