# Generated code for task 17
def solution():
    ```python
    def count_distinct_characters(string: str) -> int:
        """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    
        Args:
            string (str): The string to check.
    
        Returns:
            int: The number of distinct characters in the string.
        """
    
        # Convert the string to lowercase for case-insensitive counting
        string = string.lower()
    
        # Convert all characters to lowercase for case-insensitive counting
        string = string.lower()
    
        # Remove all duplicate characters from the string
        unique_characters = set(string)
    
        # Return the number of unique characters in the string
        return len(unique_characters)
    
    
    # Test the function
    print(count_distinct_characters('xyzXYZ'))
    print(count_distinct_characters('Jerry'))
    ```
    
    **Output:**
    
    ```
    3
    4
    ```
    
    **Explanation:**
    
    * The `count_distinct_characters` function takes a string as input.
    * It converts the string to lowercase for case-insensitive counting.
    * It converts all characters to lowercase for case-insensitive counting.
    * It removes all duplicate characters from the string.
    * It returns the number of unique characters in the string.

# You can add tests or other function calls here.
