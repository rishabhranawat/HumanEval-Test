# Generated code for task 122
def solution():
    ```python
    def solution(lst):
        """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    
        Examples
        solution([5, 8, 7, 1]) ==> 12
        solution([3, 3, 3, 3, 3]) ==> 9
        solution([30, 13, 24, 321]) ==>0
        """
        # create a new variable to store the sum
        sum = 0
        # iterate over the list
        for idx, x in enumerate(lst):
            # if the index is even and the element is odd, add it to the sum
            if idx%2==0 and x%2==1:
                sum += x
        # return the sum
        return sum
    ```
    
    **Test cases:**
    ```python
    test_cases = [[5, 8, 7, 1], [3, 3, 3, 3, 3], [30, 13, 24, 321]]
    for test_case in test_cases:
        print(f"Input: {test_case}")
        result = solution(test_case)
        print(f"Output: {result}")
    ```
    
    **Output:**
    ```
    Input: [5, 8, 7, 1]
    Output: 12
    
    Input: [3, 3, 3, 3, 3]
    Output: 9
    
    Input: [30, 13, 24, 321]
    Output: 0
    ```

# You can add tests or other function calls here.
