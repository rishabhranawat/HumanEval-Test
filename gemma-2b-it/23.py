# Generated code for task 24
def solution():
    ```python
    def strlen(string: str) -> int:
        """ Return length of given string
    
        Args:
            string (str): The string to get length of
    
        Returns:
            int: The length of the string
        """
    
        # If the string is empty, return 0
        if not string:
            return 0
    
        # Otherwise, return the length of the string
        return len(string)
    
    
    # Test the function
    print(strlen(''))
    print(strlen('abc'))
    ```
    
    **Output:**
    
    ```
    0
    3
    ```
    
    **Explanation:**
    
    * The `strlen` function takes a single argument, `string`, which is the string to get length of.
    * The function uses the `len` function to calculate the length of the string.
    * If the string is empty, the function returns 0.
    * Otherwise, the function returns the length of the string.
    * The `test` function calls the `strlen` function with different strings and prints the results.

# You can add tests or other function calls here.
