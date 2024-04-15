# Generated code for task 148
def solution():
    ```python
    def get_max_triples(n):
        """
        You are given a positive integer n. You have to create an integer array a of length n.
            For each i (1 ≤ i ≤ n), the value of a[i] = i * i - i + 1.
            Return the number of triples (a[i], a[j], a[k]) of a where i < j < k, 
        and a[i] + a[j] + a[k] is a multiple of 3.
    
        Example :
            Input: n = 5
            Output: 1
            Explanation: 
            a = [1, 3, 7, 13, 21]
            The only valid triple is (1, 7, 13).
        """
        # Initialize the list of triples to empty
        ans = []
        # Initialize the current triplet to the first three elements of the list
        a = [i*i - i + 1 for i in range(1,n+1)]
        # Initialize the count of triples to 0
        count = 0
        # Iterate over the list of tuples
        for i in range(len(a)):
            for j in range(i+1,len(a)):
                for k in range(j+1,len(a)):
                    # Check if the triplet satisfies the condition
                    if (a[i]+a[j]+a[k])%3 == 0:
                        # Add the triplet to the list of triples
                        ans.append((a[i],a[j],a[k]))
                        # Increment the count of triples
                        count += 1
        # Return the number of triples
        return count
    ```

# You can add tests or other function calls here.
