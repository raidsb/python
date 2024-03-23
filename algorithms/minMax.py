"""
You will be given a list of integers, , and a single integer . You must create an array of length  from elements of  such that its unfairness is minimized. Call that array . Unfairness of an array is calculated as

Where:
- max denotes the largest integer in 
- min denotes the smallest integer in 

Example



Pick any two elements, say .

Testing for all pairs, the solution  provides the minimum unfairness.

Note: Integers in  may not be unique.
"""

def maxMin(k, arr):
    arr.sort()
    print(arr)
    i = 0
    maxMin = arr[-1] - arr[0]
    while i + k - 1 < len(arr):
        if arr[i + k - 1] - arr[i] < maxMin:
            maxMin = arr[i + k - 1] - arr[i]        
        print(i, i+k, "maxMin: ", maxMin)
        i += 1
    return maxMin