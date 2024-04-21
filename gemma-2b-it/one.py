    ```python
    from one import *
    ```
    
    ```python
    def paren_string(paren_string):
        result = []
        current_string = []
        current_depth = 0
    
        for c in paren_string:
            if c == '(':
                current_depth += 1
                current_string.append(c)
            elif c == ')':
                current_depth -= 1
                current_string.append(c)
    
                if current_depth == 0:
                    result.append(''.join(current_string))
                    current_string.clear()
    
        return result
    ```