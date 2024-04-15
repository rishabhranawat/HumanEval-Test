# Generated code for task 92
def solution():
    ```python
    import re
    
    def is_bored(S):
        """
        You'll be given a string of words, and your task is to count the number
        of boredoms. A boredom is a sentence that starts with the word "I".
        Sentences are delimited by '.', '?' or '!'.
       
        For example:
        >>> is_bored("Hello world")
        0
        >>> is_bored("The sky is blue. The sun is shining. I love this weather")
        1
        """
    
        # Split the string into sentences
        sentences = re.split(r'[.?!]\s*', S)
    
        # Count the number of sentences that start with "I "
        return sum(sentence[0:2] == 'I ' for sentence in sentences)
    
    
    if __name__ == "__main__":
        print(is_bored("Hello world"))
        print(is_bored("The sky is blue. The sun is shining. I love this weather"))
    ```
    
    **Output:**
    
    ```
    0
    1
    ```
    
    **Explanation:**
    
    * The `is_bored` function takes a string `S` as input.
    * It uses the `re.split` function to split the input string into a list of sentences.
    * The function uses a list comprehension to check the first two characters of each sentence and count the number of sentences that start with "I ".
    * The function uses the `sum` function to add the counts of all the sentences that start with "I ".
    * The `__name__ == "__main__"` block calls the `is_bored` function with two arguments and prints the results.

# You can add tests or other function calls here.
