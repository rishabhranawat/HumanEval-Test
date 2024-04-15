# Generated code for task 111
def solution():
    ```python
    def exchange(lst1, lst2):
        """
        This function determines whether it is possible to perform an exchange of elements
        between two lists of numbers to make lst1 a list of only even numbers.
    
        Args:
            lst1 (list): The first list of numbers.
            lst2 (list): The second list of numbers.
    
        Returns:
            str: "YES" if it is possible to exchange elements, "NO" otherwise.
        """
    
        odd = 0
        even = 0
        for i in lst1:
            if i % 2 == 1:
                odd += 1
        for i in lst2:
            if i % 2 == 0:
                even += 1
        if even >= odd:
            return "YES"
        return "NO"
    
    
    # Test the function
    print(exchange([1, 2, 3, 4], [1, 2, 3, 4]))
    print(exchange([1, 2, 3, 4], [1, 5, 3, 4]))
    print(exchange([1, 2, 3, 5], [1, 2, 3, 4]))
    ```
    
    **Output:**
    
    ```
    YES
    NO
    NO
    ```

# You can add tests or other function calls here.
