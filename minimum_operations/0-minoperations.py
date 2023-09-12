#!/usr/bin/python3
"""Minimum Operations"""

def minOperations(n):
    if n <= 1:
        return 0

    # Create a list to store the minimum operations for each number of 'H' characters
    dp = [float('inf')] * (n + 1)

    # The base case: it takes 0 operations to have 1 'H' character
    dp[1] = 0

    for i in range(2, n + 1):
        # For each number i, try to find the best way to reach it
        for j in range(2, i + 1):
            if i % j == 0:
                # If i is divisible by j, we can copy j characters and paste (i // j - 1) times
                dp[i] = min(dp[i], dp[j] + (i // j))

    return dp[n] if dp[n] != float('inf') else 0

# Testing the function
if __name__ == "__main__":
    n = 4
    print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

    n = 12
    print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

