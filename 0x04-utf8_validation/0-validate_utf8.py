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
    for i in data:
        if i.bit_length() > 7:
            return False
    return True
