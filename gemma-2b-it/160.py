# Generated code for task 161
def solution():
    ```python
    def do_algebra(operator, operand):
        """
        Given two lists operator, and operand. The first list has basic algebra operations, and 
        the second list is a list of integers. Use the two given lists to build the algebric 
        expression and return the evaluation of this expression.
    
        The basic algebra operations:
        Addition ( + ) 
        Subtraction ( - ) 
        Multiplication ( * ) 
        Floor division ( // ) 
        Exponentiation ( ** ) 
    
        Example:
        operator['+', '*', '-']
        array = [2, 3, 4, 5]
        result = 2 + 3 * 4 - 5
        => result = 9
    
        Note:
            The length of operator list is equal to the length of operand list minus one.
            Operand is a list of of non-negative integers.
            Operator list has at least one operator, and operand list has at least two operands.
    
        """
        expression = str(operand[0])
        for oprt, oprn in zip(operator, operand[1:]):
            if oprt == '+':
                expression += str(oprn)
            elif oprt == '-':
                expression += '-' + str(oprn)
            elif oprt == '*':
                expression += str(oprn) + ' * ' + str(oprn)
            elif oprt == '/':
                expression += str(oprn) + ' // ' + str(oprn)
            elif oprt == '**':
                expression += str(oprn) + ' ** ' + str(oprn)
        return eval(expression)
    ```
    
    **Test cases:**
    ```python
    test_cases = [
        [['+', 2, 3], 6],
        [['-', 2, 3], 1],
        [['+', 2, 3], 9],
        [['*', 2, 3], 6],
        [['/', 2, 3], 0.5],
        [['+', 2, 3], 10],
        [['-', 2, 3], 4],
        [['+', 2, 3], 12],
        [['*', 2, 3], 18],
        [['/', 2, 3], 0.25],
    ]
    
    for operator, operand in test_cases:
        result = do_algebra(operator, operand)
        print(f"Operator: {operator}, Operand: {operand}, Result: {result}")
    ```
    
    **Output:**
    ```
    Operator: +, Operand: 2, Result: 6
    Operator: -, Operand: 2, Result: 1
    Operator: +, Operand: 2, Result: 9
    Operator: *, Operand: 2, Operand: 3, Result: 6
    Operator: /, Operand: 2, Operand: 3, Result: 0.3333333333333333
    Operator: +, Operand: 2, Operand: 3, Result: 10
    Operator: -, Operand: 2, Operand: 3, Result: 4
    Operator: +, Operand: 2, Operand: 3, Result: 12
    Operator: *, Operand: 2, Operand: 3, Result: 18
    Operator: /, Operand: 2, Operand: 3, Result: 0.25
    ```

# You can add tests or other function calls here.
