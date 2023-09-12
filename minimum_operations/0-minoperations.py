#!/usr/bin/python3
"""Minimum Operations"""
def minOperations(n):
    if n <= 1:
        return 0

    dp = [0] * (n + 1)

    for i in range(2, n + 1):
        dp[i] = i 
 # Initialize with the maximum possible operations

        for j in range(2, i):
            if i % j == 0:
                dp[i] = min(dp[i], dp[j] + (i // j))

    return dp[n] if dp[n] != float('inf') else 0

