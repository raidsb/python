"""
Starting with a 1-indexed array of zeros and a list of operations, for each operation add a value to each the array element between two given indices, inclusive. Once all operations have been performed, return the maximum value in the array.

Example

Queries are interpreted as follows:

    a b k
    1 5 3
    4 8 7
    6 9 1

Add the values of
between the indices and

inclusive:

index->	 1 2 3  4  5 6 7 8 9 10
	[0,0,0, 0, 0,0,0,0,0, 0]
	[3,3,3, 3, 3,0,0,0,0, 0]
	[3,3,3,10,10,7,7,7,0, 0]
	[3,3,3,10,10,8,8,8,1, 0]

The largest value is
after all operations are performed. 

https://www.hackerrank.com/challenges/one-month-preparation-kit-crush/problem?isFullScreen=true&h_l=interview&playlist_slugs[]=preparation-kits&playlist_slugs[]=one-month-preparation-kit&playlist_slugs[]=one-month-week-four

"""

"""
in this problem, we don't need to update all elements within a range of a query, we only need to set the first element in the range with the 
update value. this is becuase the solution is designed to accumulate all values in the array and get the max as we assumulate.
important note: we set the element AFTER END of the range to -k, since we are accumulating, this makes sure that the sum at this element discard 
the unapplicable update while accumulating.
"""


def arrayManipulation(n, queries):
    deltas = [0] * (n+1)  # to avoid index of of range problem and process end of a range efficiently
    for a, b, k in queries:
        deltas[a-1] += k  # set the first of the range 
        deltas[b] -= k    # set element ouside the range back to correct value while accumulating

    max_val = val = 0
    for delta in deltas:
        val += delta
        max_val = max(max_val, val)
    return max_val