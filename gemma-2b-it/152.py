# Generated code for task 153
def solution():
    ```python
    def compare(game,guess):
        """I think we all remember that feeling when the result of some long-awaited
        event is finally known. The feelings and thoughts you have at that moment are
        definitely worth noting down and comparing.
        Your task is to determine if a person correctly guessed the results of a number of matches.
        You are given two arrays of scores and guesses of equal length, where each index shows a match. 
        Return an array of the same length denoting how far off each guess was. If they have guessed correctly,
        the value is 0, and if not, the value is the absolute difference between the guess and the score.
    
        example:
    
        compare([1,2,3,4,5,1],[1,2,3,4,2,-2]) -> [0,0,0,0,3,3]
        compare([0,5,0,0,0,4],[4,1,1,0,0,-2]) -> [4,4,1,0,0,6]
        """
        return [abs(x-y) for x,y in zip(game,guess)]
    ```
    **Explanation:**
    
    1. The `compare` function takes two arguments: `game` and `guess`.
    2. It initializes a list called `differences` to store the differences between each guess and the corresponding score.
    3. It iterates over the game and guess lists, comparing each element.
    4. If the guess is correct, it adds 0 to the `differences` list. Otherwise, it adds the absolute difference between the guess and the score to the `differences` list.
    5. Finally, the function returns the `differences` list, which contains the differences between the guesses and the scores.
    
    **Example Usage:**
    
    ```python
    compare([1,2,3,4,5,1],[1,2,3,4,2,-2])
    ```
    
    **Output:**
    
    ```
    [0, 0, 0, 0, 3, 3]
    ```

# You can add tests or other function calls here.
