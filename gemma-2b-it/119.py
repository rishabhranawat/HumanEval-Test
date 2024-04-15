# Generated code for task 120
def solution():
    ```
    **Test cases:**
    ```python
    def test_match_parens():
        assert match_parens(['()(', ')']) == 'Yes'
        assert match_parens([')', ')']) == 'No'
        assert match_parens(['()()()']) == 'Yes'
        assert match_parens(['(()())']) == 'Yes'
        assert match_parens(['()', ')']) == 'No'
        assert match_parens([')', '(']) == 'No'
        assert match_parens(['()', '(]) == 'No'
        assert match_parens([')', '(', ')']) == 'No'
    ```
    
    **Output:**
    ```
    True
    False
    True
    True
    False
    False
    False
    False
    ```

# You can add tests or other function calls here.
