# Generated code for task 116
def solution():
    ```python
    def max_fill(grid, capacity):
        """
        You are given a rectangular grid of wells. Each row represents a single well,
        and each 1 in a row represents a single unit of water.
        Each well has a corresponding bucket that can be used to extract water from it, 
        and all buckets have the same capacity.
        Your task is to use the buckets to empty the wells.
        Output the number of times you need to lower the buckets.
    
        Example 1:
            Input: 
                grid : [[0,0,1,0], [0,1,0,0], [1,1,1,1]]
                bucket_capacity : 1
            Output: 6
    
        Example 2:
            Input: 
                grid : [[0,0,1,1], [0,0,0,0], [1,1,1,1], [0,1,1,1]]
                bucket_capacity : 2
            Output: 5
        
        Example 3:
            Input: 
                grid : [[0,0,0], [0,0,0]]
                bucket_capacity : 5
            Output: 0
    
        Constraints:
            * all wells have the same length
            * 1 <= grid.length <= 10^2
            * 1 <= grid[:,1].length <= 10^2
            * grid[i][j] -> 0 | 1
            * 1 <= capacity <= 10
        """
        # Initialize the total number of buckets to 0.
        buckets = 0
    
        # Initialize the number of filled wells to 0.
        filled = 0
    
        # Iterate over the grid.
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                # If the well is empty and the bucket capacity is greater than 0,
                # add the number of wells to the total number of filled wells.
                if grid[i][j] == 0 and capacity > 0:
                    buckets += math.ceil(sum(grid[i][j]) / capacity)
                    filled += 1
    
        # Return the number of times the buckets need to be lowered.
        return filled
    
    
    if __name__ == "__main__":
        grid = [[0,0,1,0], [0,1,0,0], [1,1,1,1]]
        print(max_fill(grid, 1))
    ```

# You can add tests or other function calls here.
