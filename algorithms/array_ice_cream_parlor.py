"""
Two friends like to pool their money and go to the ice cream parlor. They always choose two distinct flavors and they spend all of their money.

Given a list of prices for the flavors of ice cream, select the two that will cost all of the money they have.

Example.  

The two flavors that cost  and  meet the criteria. Using -based indexing, they are at indices  and .

Function Description

Complete the icecreamParlor function in the editor below.

icecreamParlor has the following parameter(s):

int m: the amount of money they have to spend
int cost[n]: the cost of each flavor of ice cream
Returns

int[2]: the indices of the prices of the two flavors they buy, sorted ascending
"""

def icecreamParlor(m, arr):
    for i in range(len(arr)):
        arr_rest = arr[i+1:len(arr)]
        if m - arr[i] in arr_rest:
            return [i+1, arr.index(m - arr[i], i+1)+1]