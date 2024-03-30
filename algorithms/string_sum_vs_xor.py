"""
Given an integer , find each  such that:

where  denotes the bitwise XOR operator. Return the number of 's satisfying the criteria.

Example

There are four values that meet the criteria:

Return .
"""

def sumXor(n):
    bin_n = '{0:b}'.format(n)
    number_of_zeroes = bin_n.count('0')
    return 2 ** number_of_zeroes if n != 0 else 1