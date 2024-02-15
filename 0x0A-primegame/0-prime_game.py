#!/usr/bin/python3
""" Prime game """


def isWinner(x, nums):
    """ Determine the winner """
    if x <= 0 or nums is None or x != len(nums):
        return None

    def sieve_eratosthenes(n):
        """ Implement sieve"""
        is_prime = [True] * (n + 1)
        is_prime[0] = is_prime[1] = False
        p = 2
        while p * p <= n:
            if is_prime[p]:
                for i in range(p * p, n + 1, p):
                    is_prime[i] = False
            p += 1
        return is_prime

    def remove_multiples(primes, x):
        """ Implement remove multiples"""
        n = len(primes)
        for i in range(2, n):
            if i * x < n:
                primes[i * x] = False
            else:
                break

    ben = 0
    maria = 0

    max_num = max(nums)
    primes = sieve_eratosthenes(max_num)

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
