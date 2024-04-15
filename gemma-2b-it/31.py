# Generated code for task 32
def solution():
    ```
    
    **Test cases:**
    
    | Input | Expected Output |
    |---|---|
    | 6 | False |
    | 101 | True |
    | 11 | True |
    | 13441 | True |
    | 61 | True |
    | 4 | False |
    | 1 | False |
    
    **Explanation:**
    
    * The `is_prime` function takes an integer `n` as input.
    * It first checks if `n` is less than 2. If it is, it returns `False` because 1 and all negative numbers are not prime.
    * Otherwise, it checks if `n` is divisible by any numbers from 2 to `n - 1` (inclusive). If it is divisible by any of these numbers, it returns `False` because `n` cannot be prime if it has divisors.
    * If it successfully passes all the tests, it returns `True`, indicating that `n` is a prime number.
    
    **Note:**
    
    * The time complexity of this algorithm is O(n), where n is the input size. This is because it checks all possible divisors of `n` in linear time.
    * The algorithm is not optimized for performance, and there are more efficient algorithms to solve this problem.

# You can add tests or other function calls here.
