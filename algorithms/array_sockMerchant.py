"""
There is a large pile of socks that must be paired by color. Given an array of integers representing the color of each sock, determine how many pairs of socks with matching colors there are.

Example


There is one pair of color  and one of color . There are three odd socks left, one of each color. The number of pairs is .

Function Description

Complete the sockMerchant function in the editor below.

sockMerchant has the following parameter(s):

int n: the number of socks in the pile
int ar[n]: the colors of each sock
Returns

int: the number of pairs
"""

def sockMerchant(n, ar):
    dict_socks = {}
    for i in ar:
        dict_socks[i] = dict_socks[i] + 1 if i in dict_socks.keys() else 1
    number_of_pairs = 0
    print(dict_socks)
    for k in dict_socks.keys():
        number_of_pairs+= dict_socks[k] // 2

    return number_of_pairs