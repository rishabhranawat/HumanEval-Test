# Generated code for task 144
def solution():
    ```python
    def words_in_sentence(sentence):
        """
        You are given a string representing a sentence,
        the sentence contains some words separated by a space,
        and you have to return a string that contains the words from the original sentence,
        whose lengths are prime numbers,
        the order of the words in the new string should be the same as the original one.
    
        Example 1:
            Input: sentence = "This is a test"
            Output: "is"
    
        Example 2:
            Input: sentence = "lets go for swimming"
            Output: "go for"
    
        Constraints:
            * 1 <= len(sentence) <= 100
            * sentence contains only letters
        """
        new_lst = []
        for word in sentence.split():
            if len(word) == 1:
                continue
            is_prime = True
            for i in range(2, len(word)):
                if len(word)%i == 0:
                    is_prime = False
                    break
            if is_prime:
                new_lst.append(word)
        return " ".join(new_lst)
    ```
    **Test cases:**
    ```python
    test_cases = [
        ("This is a test", "is"),
        ("lets go for swimming", "go for"),
        ("This sentence has only one word", "word"),
        ("This sentence has a prime number of words", "prime"),
        ("This sentence has a word with a length of 1", "1"),
        ("This sentence has a word with a length of 2", "2"),
        ("This sentence has a word with a length of 3", "3"),
    ]
    for test, expected in test_cases:
        actual = words_in_sentence(test)
        print(f"Input: {test}, Output: {actual}, Expected: {expected}")
        assert actual == expected
    ```

# You can add tests or other function calls here.
