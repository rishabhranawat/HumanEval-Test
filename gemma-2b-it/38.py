# Generated code for task 39
def solution():
    ```python
    def encode_cyclic(s: str):
        """
        returns encoded string by cycling groups of three characters.
        """
        # split string to groups. Each of length 3.
        groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
        # cycle elements in each group. Unless group has fewer elements than 3.
        groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
        return "".join(groups)
    
    
    def decode_cyclic(s: str):
        """
        takes as input string encoded with encode_cyclic function. Returns decoded string.
        """
        # return original string if it is a single character long.
        if len(s) == 1:
            return s
        # reverse the order of the groups.
        groups.reverse()
        # return the decoded string.
        return "".join(groups)
    
    
    # test cases
    print(encode_cyclic("ABCDEFGABC"))
    print(decode_cyclic("AEIOUYIU"))
    print(encode_cyclic("123456789"))
    print(decode_cyclic("987654321"))
    print(encode_cyclic("ZYXWVUT"))
    print(decode_cyclic("VWUXYZW"))
    ```

# You can add tests or other function calls here.
