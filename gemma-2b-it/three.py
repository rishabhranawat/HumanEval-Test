    ```python
    from three import *
    
    def balance(operations):
        balance = 0
    
        for op in operations:
            balance += op
            if balance < 0:
                return True
    
        return False
    ```
    Output:
    
    ```python
    False
    ```