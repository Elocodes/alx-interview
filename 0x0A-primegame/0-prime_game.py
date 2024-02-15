#!/usr/bin/python3
"""
Maria and Ben are playing a game. Given a set of consecutive integers
starting from 1 up to and including n, they take turns choosing a prime number
from the set and removing that number and its multiples from the set.
"""


def sieve_of_eratosthenes(limit):
    """ check prime """
    primes = []
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False

    for number in range(2, int(limit**0.5) + 1):
        if is_prime[number]:
            primes.append(number)
            for multiple in range(number * number, limit + 1, number):
                is_prime[multiple] = False

    return primes


def isWinner(x, nums):
    """
    where x is the number of rounds and nums is an array of n
    Return: name of the player that won the most rounds
    If the winner cannot be determined, return None
    You can assume n and x will not be larger than 10000
    """
    def canWin(n):
        """ determine player wins """
        primes = sieve_of_eratosthenes(n)
        memo = {}

        def helper(num):
            """ helper func """
            if num in memo:
                return memo[num]

            for prime in primes:
                if num % prime == 0:
                    next_num = num // prime
                    if not helper(next_num):
                        memo[num] = True
                        return True

            memo[num] = False
            return False

        return helper(n)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if canWin(n):
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif maria_wins < ben_wins:
        return "Ben"
    else:
        return None
