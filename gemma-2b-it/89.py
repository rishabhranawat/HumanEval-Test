# Generated code for task 90
def solution():
    ```
    
    **Test cases:**
    ```python
    import unittest
    
    class TestEncrypt(unittest.TestCase):
    
        def test_encrypt_simple(self):
            self.assertEqual(encrypt('hi'), 'lm')
    
        def test_encrypt_long_string(self):
            self.assertEqual(encrypt('asdfghjkl'), 'ewhjklnop')
    
        def test_encrypt_special_chars(self):
            self.assertEqual(encrypt('gf'), 'kj')
    
        def test_encrypt_empty_string(self):
            self.assertEqual(encrypt(''), '')
    
    if __name__ == '__main__':
        unittest.main()
    ```
    
    **Explanation:**
    * The `encrypt` function takes a string as an argument.
    * It creates a string `d` containing the alphabet with the letters shifted down by two places.
    * It iterates over the string and adds the encrypted character to the `out` variable.
    * If the character is in the alphabet, it gets the character at the position `(d.index(c)+2*2) % 26` in the alphabet.
    * Otherwise, it adds the character as it is.
    * Finally, it returns the `out` string.

# You can add tests or other function calls here.
