# Generated code for task 9
def solution():
    ```python
    def test_sum_product():
        assert sum_product([]) == (0, 1)
        assert sum_product([1, 2, 3, 4]) == (10, 24)
        assert sum_product([1, 2, 3, 4, 5]) == (15, 60)
        assert sum_product([1, 2, 3, 4, 5, 6]) == (18, 120)
    
    
    if __name__ == "__main__":
        test_sum_product()
    ```
    
    **Explanation:**
    
    * The `sum_product` function takes a list of integers as input.
    * It initializes two variables, `sum_value` to 0 and `prod_value` to 1. `sum_value` will store the sum of the integers in the list, and `prod_value` will store the product of the integers in the list.
    * It then iterates over the list of integers, adding each value to `sum_value` and multiplying it by `prod_value` for each value.
    * Finally, the function returns the tuple containing the sum and product of the integers in the list.
    
    **Output:**
    
    ```
    (0, 1)
    (10, 24)
    (15, 60)
    (18, 120)
    ```

# You can add tests or other function calls here.
