# Generated code for task 154
def solution():
    ```python
    def Strongest_Extension(class_name, extensions):
        """
        :param class_name: The name of the class.
        :param extensions: A list of extensions.
        :return: The strongest extension name.
        """
    
        # Find the strongest extension.
        strong = extensions[0]
        my_val = len([x for x in extensions[0] if x.isalpha() and x.isupper()]) - len([x for x in extensions[0] if x.isalpha() and x.islower()])
        for s in extensions:
            val = len([x for x in s if x.isalpha() and x.isupper()]) - len([x for x in s if x.isalpha() and x.islower()])
            if val > my_val:
                strong = s
                my_val = val
    
        # Return the strongest extension.
        ans = class_name + "." + strong
        return ans
    
    
    # Test the Strongest_Extension function.
    print(Strongest_Extension('my_class', ['AA', 'Be', 'CC']))
    ```

# You can add tests or other function calls here.
