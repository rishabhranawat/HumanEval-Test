# Generated code for task 88
def solution():
    ```python
    def get_row(lst, x):
        """
        You are given a 2 dimensional data, as a nested lists,
        which is similar to matrix, however, unlike matrices,
        each row may contain a different number of columns.
        Given lst, and an integer x, find integers x in the list,
        and return list of tuples, [(x1, y1), (x2, y2) ...] such that
        each tuple is a coordinate - (row, columns), starting with 0.
        Sort coordinates initially by rows in ascending order.
        Also, sort coordinates of the row by columns in descending order.
    
        Examples:
        get_row([
          [1,2,3,4,5,6],
          [1,2,3,4,1,6],
          [1,2,3,4,5,1]
        ], 1) == [(0, 0), (1, 4), (1, 0), (2, 5), (2, 0)]
        get_row([], 1) == []
        get_row([[], [1], [1, 2, 3]], 3) == [(2, 2)]
        """
        # Create a list of tuples to store the coordinates
        coords = []
    
        # Iterate over the rows in the list
        for i in range(len(lst)):
            # Iterate over the columns in the list
            for j in range(len(lst[i])):
                # If the current element is equal to the given value, add it to the list of coordinates
                if lst[i][j] == x:
                    # Add the coordinate to the list of coordinates
                    coords.append((i, j))
    
        # Sort the coordinates by rows in ascending order
        coords.sort(key=lambda x: x[0])
    
        # Sort the coordinates by columns in descending order
        coords.sort(key=lambda x: x[1], reverse=True)
    
        # Return the sorted list of coordinates
        return coords
    ```

# You can add tests or other function calls here.
