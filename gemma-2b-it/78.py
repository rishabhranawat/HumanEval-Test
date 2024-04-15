# Generated code for task 79
def solution():
    ```python
    def hex_key(num):
        """
        This function receives a hexadecimal number as a string and counts the number 
        of hexadecimal digits that are primes (prime number, or a prime, is a natural 
        number greater than 1 that is not a product of two smaller natural numbers).
    
        Args:
            num (str): The hexadecimal number to check.
    
        Returns:
            int: The number of prime hexadecimal digits in the input string.
        """
    
        # Create a set of prime digits.
        primes = ('2', '3', '5', '7', 'B', 'D')
    
        # Initialize the count of prime digits to 0.
        total = 0
    
        # Iterate over the string.
        for i in range(0, len(num)):
            # If the current character is in the set of prime digits, increment the count.
            if num[i] in primes:
                total += 1
    
        # Return the count of prime digits.
        return total
    
    
    # Test the function.
    print(hex_key("AB"))  # Output: 1
    print(hex_key("1077E"))  # Output: 2
    print(hex_key("ABED1A33"))  # Output: 4
    print(hex_key("123456789ABCDEF0"))  # Output: 6
    print(hex_key("2020"))  # Output: 2
    ```

# You can add tests or other function calls here.
