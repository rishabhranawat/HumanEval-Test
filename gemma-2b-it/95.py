# Generated code for task 96
def solution():
    ```python
    def check_dict_case(dict):
        """
        Given a dictionary, return True if all keys are strings in lower 
        case or all keys are strings in upper case, else return False.
        The function should return False is the given dictionary is empty.
    
        Args:
            dict (dict): The dictionary to check.
    
        Returns:
            bool: True if all keys are strings in lower case or all keys are strings in upper case, else False.
        """
    
        # If the dictionary is empty, return False.
        if len(dict.keys()) == 0:
            return False
    
        # Initialize the state variable to "start".
        state = "start"
    
        # Iterate over the keys of the dictionary.
        for key in dict.keys():
    
            # If the key is not a string, set the state to "mixed".
            if not isinstance(key, str):
                state = "mixed"
                break
    
            # If the key is in the upper case, set the state to "upper".
            elif key.isupper():
                state = "upper"
    
            # If the key is in the lower case, set the state to "lower".
            elif key.islower():
                state = "lower"
    
            # If the key is neither in the upper case nor the lower case, set the state to "mixed".
            else:
                state = "mixed"
    
        # Return the final state of the state variable.
        return state == "upper" or state == "lower"
    
    
    # Test the function.
    print(check_dict_case({"a":"apple", "b":"banana"}))  # True
    print(check_dict_case({"a":"apple", "A":"banana", "B":"banana"}))  # False
    print(check_dict_case({"a":"apple", 8:"banana", "a":"apple"}))  # False
    print(check_dict_case({"Name":"John", "Age":"36", "City":"Houston"}))  # False
    print(check_dict_case({"STATE":"NC", "ZIP":"12345" }))  # True
    ```

# You can add tests or other function calls here.
