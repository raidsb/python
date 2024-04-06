"""
Jesse loves cookies and wants the sweetness of some cookies to be greater than value

. To do this, two cookies with the least sweetness are repeatedly mixed. This creates a special combined cookie with:

sweetness
Least sweet cookie

2nd least sweet cookie).

This occurs until all the cookies have a sweetness

.

Given the sweetness of a number of cookies, determine the minimum number of operations required. If it is not possible, return

.

Example

The smallest values are .
Remove them then return to the array. Now .
Remove and return to the array. Now .
Remove , return and .
Finally, remove and return to . Now .
All values are so the process stops after iterations. Return

.

Function Description
Complete the cookies function in the editor below.

cookies has the following parameters:

    int k: the threshold value
    int A[n]: an array of sweetness values

Returns

    int: the number of iterations required or 

https://www.hackerrank.com/challenges/one-month-preparation-kit-jesse-and-cookies/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-month-preparation-kit&playlist_slugs%5B%5D=one-month-week-four 
"""

import heapq
def cookies(k, A):
    # Write your code here
    count = 0
    heapq.heapify(A)
    
    while A[0] < k:
        if len(A) == 1:
            return -1
        a1 = heapq.heappop(A)
        a2 = heapq.heappop(A)
        a3 = a1 + a2 * 2
        heapq.heappush(A, a3)
        count += 1
    return count