# Generated code for task 118
def solution():
    ```python
    def test_select_words():
        assert select_words("Mary had a little lamb", 4) == ["little"]
        assert select_words("Mary had a little lamb", 3) == ["Mary", "lamb"]
        assert select_words("simple white space", 2) == []
        assert select_words("Hello world", 4) == ["world"]
        assert select_words("Uncle sam", 3) == ["Uncle"]
        assert select_words("Mary had a little lamb", 5) == []
    
    if __name__ == "__main__":
        test_select_words()
    ```
    
    **Explanation:**
    
    1. The `select_words` function takes two arguments: the string `s` and the integer `n`.
    2. It first splits the input string `s` into a list of words using the `split` method.
    3. The function initializes a list called `result` to store the words that contain exactly `n` consonants.
    4. It iterates through each word in the `words` list.
    5. For each word, it initializes a variable called `n_consonants` to 0. This variable will be used to count the number of consonants in the word.
    6. It iterates through the characters in the word. For each character, it checks if it is lowercase and not equal to 'a', 'e', 'i', 'o', or 'u'. If it is a consonant, it increments `n_consonants`.
    7. If the `n_consonants` variable is equal to `n`, it means that the word contains exactly `n` consonants, so it is added to the `result` list.
    8. Finally, the function returns the `result` list, which contains all the words from the input string that contain exactly `n` consonants.
    
    **Note:**
    
    The function assumes that the input string only contains letters and spaces. If there are other characters in the string, they will be ignored.

# You can add tests or other function calls here.
