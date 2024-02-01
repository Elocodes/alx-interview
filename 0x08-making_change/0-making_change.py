#!/usr/bin/python3
"""
Given a pile of coins of different values, determine the fewest
number of coins needed to meet a given amount total.

Return: fewest number of coins needed to meet total
If total is 0 or less, return 0
If total cannot be met by any number of coins you have, return -1
coins is a list of the values of the coins in your possession
The value of a coin will always be an integer greater than 0
You can assume you have an infinite number of each denomination of coin in the list
Your solution’s runtime will be evaluated in this task
"""

def makeChange(coins, total):
    """ make change """
    if total <= 0:
        return 0
    # store the fewest num of coins to make change for amoutns 0 to total
    dp = [float('inf')] * (total + 1)
    dp[0] = 0
    for coin in coins:
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)
    return dp[total] if dp[total] != float('inf') else -1
