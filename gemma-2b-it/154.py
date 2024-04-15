# Generated code for task 155
def solution():
    ```python
    def cycpattern_check(a , b):
        """
        You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
        cycpattern_check("abcd","abd") => False
        cycpattern_check("hello","ell") => True
        cycpattern_check("whassup","psus") => False
        cycpattern_check("abab","baa") => True
        cycpattern_check("efef","eeff") => False
        cycpattern_check("himenss","simen") => True
    
        """
        l = len(b)
        pat = b + b
        for i in range(len(a) - l + 1):
            for j in range(l + 1):
                if a[i:i+l] == pat[j:j+l]:
                    return True
        return False
    
    ```
    
    **Explanation:**
    
    1. The `cycpattern_check` function takes two arguments: `a` and `b`.
    2. It first calculates the length of the second word `b` and the length of the first word `a` minus the length of the second word.
    3. It then creates a pattern string `pat` that is the same length as the second word.
    4. It iterates over the first word `a` and for each position `i`, it iterates over the pattern string `pat` and checks if the substring of `a` starting at position `i` is equal to the substring of `pat` starting at position `j`.
    5. If a match is found, it returns `True`.
    6. If no match is found, it returns `False`.
    
    **Example Usage:**
    
    ```python
    >>> cycpattern_check("abcd", "abd")
    False
    >>> cycpattern_check("hello", "ell")
    True
    >>> cycpattern_check("whassup", "psus")
    False
    >>> cycpattern_check("abab", "baa")
    True
    >>> cycpattern_check("efef", "eeff")
    False
    >>> cycpattern_check("himenss", "simen")
    True
    ```

# You can add tests or other function calls here.
