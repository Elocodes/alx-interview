#!/usr/bin/python3
"""
prime game
"""


def isWinner(x, nums):
    """ winner """
    if x <= 0 or nums is None or x != len(nums):
        return None

    def sieve_of_eratosthenes(limit):
        """ sieve """
        primes = []
        is_prime = [True] * (limit + 1)
        is_prime[0] = is_prime[1] = False

        for number in range(2, int(limit**0.5) + 1):
            if is_prime[number]:
                primes.append(number)
                for multiple in range(number * number, limit + 1, number):
                    is_prime[multiple] = False

        return primes

    def canWin(n):
        """ winner """
        primes = sieve_of_eratosthenes(n)
        memo = {}

        if n in memo:
            return memo[n]

        for prime in primes:
            if n % prime == 0:
                next_num = n // prime
                if not canWin(next_num):
                    memo[n] = True
                    return True

        memo[n] = False
        return False

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
