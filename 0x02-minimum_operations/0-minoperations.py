#!/usr/bin/python3
"""
calculates the fewest number of operations needed to result
in exactly n H characters in the file.
"""


def minOperations(n: int) -> int:
    """Returns min number of operation to reach n(H)"""
    if n <= 1:
        return 0

    i = 2
    num_operation = 0

    while i <= n:
        while n % i == 0:
            num_operation += i
            n //= i
        i += 1
    return num_operation
