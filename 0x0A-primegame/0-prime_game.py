#!/usr/bin/python3
"""
prime game
"""


def isWinner(x, nums):
    """
    where x is the number of rounds and nums is an array of n
    Return: name of the player that won the most rounds
    If the winner cannot be determined, return None
    You can assume n and x will not be larger than 10000
    """
    if x <= 0 or nums is None or x != len(nums):
        return None

    def sieve_of_eratosthenes(limit):
        """ check prime """
        is_prime = [True] * (limit + 1)
        is_prime[0] = is_prime[1] = False
        p = 2
        while p * p <= limit:
            if is_prime[p]:
                for i in range(p * p, limit + 1, p):
                    is_prime[i] = False
            p += 1
        return is_prime

    def remove_multiples(primes, x):
        """ removing multiples"""
        n = len(primes)
        for i in range(2, n):
            if i * x < n:
                primes[i * x] = False
            else:
                break

    ben = 0
    maria = 0

    max_num = max(nums)
    primes = sieve_of_eratosthenes(max_num)

    for i in nums:
        if sum(primes[0:i + 1]) % 2 == 0:
            ben += 1
        else:
            maria += 1

    if ben > maria:
        return "Ben"
    if maria > ben:
        return "Maria"

    return None
