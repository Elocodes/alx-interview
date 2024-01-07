#!/usr/bin/python3

"""
method that determines if a given data set represents a valid UTF-8 encoding.
"""


def validUTF8(data):
    """
    data set can contain multiple characeters.
    data will be represented by a list of integers.
    Each integer represents 1 byte of data
    return true if data is a valid utf-8 encoding
    """
    # track num of ex[ected following bytes
    next_bytes = 0

    for byte in data:
        # check if bytes continue
        if next_bytes > 0:
            # check if two most significant bits are '10'
            if not (byte >> 6 == 0b10):
                return False
            next_bytes -= 1
        else:
            # Check the number of leading '1' bits for length of the character
            if byte >> 7 == 0:
                # Single-byte character (0xxxxxxx)
                next_bytes = 0
            elif byte >> 5 == 0b110:
                # Two-byte character (110xxxxx 10xxxxxx)
                next_bytes = 1
            elif byte >> 4 == 0b1110:
                # Three-byte character (1110xxxx 10xxxxxx 10xxxxxx)
                next_bytes = 2
            elif byte >> 3 == 0b11110:
                # Four-byte character (11110xxx 10xxxxxx 10xxxxxx 10xxxxxx)
                next_bytes = 3
            else:
                # Invalid leading bits
                return False

    # Check if there are no unexpected incomplete characters
    return next_bytes == 0
