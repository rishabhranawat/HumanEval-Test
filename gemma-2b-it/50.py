# Generated code for task 51
def solution():
    ```python
    def test_encode_shift():
        assert encode_shift("hello") == "hello"
        assert encode_shift("world") == "world"
        assert encode_shift("a") == "z"
        assert encode_shift("z") == "a"
    
    
    def test_decode_shift():
        assert decode_shift("hello") == "hello"
        assert decode_shift("world") == "world"
        assert decode_shift("a") == "z"
        assert decode_shift("z") == "a"
    
    if __name__ == "__main__":
        test_encode_shift()
        test_decode_shift()
    ```
    
    **Explanation:**
    
    * `encode_shift` function takes a string and shifts every character in the alphabet by 5 positions to the right. It uses the formula `((ord(ch) + 5 - ord("a")) % 26) + ord("a")` to calculate the new position of the character in the alphabet.
    * `decode_shift` function takes an encoded string and shifts every character back by 5 positions to the left. It uses the formula `((ord(ch) - 5 - ord("a")) % 26) + ord("a")` to calculate the new position of the character in the alphabet.
    
    **Output:**
    
    ```
    hello
    world
    z
    a
    ```

# You can add tests or other function calls here.
