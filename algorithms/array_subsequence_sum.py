"""
We define subsequence as any subset of an array. We define a subarray as a contiguous subsequence in an array.

Given an array, find the maximum possible sum among:

    all nonempty subarrays.
    all nonempty subsequences.

Print the two values as space-separated integers on one line.

Note that empty subarrays/subsequences should not be considered.

Example
The maximum subarray sum is comprised of elements at inidices . Their sum is . The maximum subsequence sum is comprised of elements at indices and their sum is

.

Function Description

Complete the maxSubarray function in the editor below.

maxSubarray has the following parameter(s):

    int arr[n]: an array of integers

Returns

    int[2]: the maximum subarray and subsequence sums
https://www.hackerrank.com/challenges/one-month-preparation-kit-maxsubarray/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-month-preparation-kit&playlist_slugs%5B%5D=one-month-week-four 

"""


def maxSubarray(arr):
    max_val = max(arr)
    if max_val <= 0:
        return max_val, max_val
    max_sum = 0 # Will hold the maximum subsequence sum so far. a sebsequence sum only considered as long as the sum is not negative.
                # if so, then a new sum should start.
    cur_sum = 0 # Will hold the current subsequence sum,a current subsequence sum will go summing as long as the sum is not negative.
    for i in range(len(arr)):
        if cur_sum + arr[i] < 0:
            cur_sum = 0 # to discard the whole current subsequence sum so far and start with a new subsequence sum
            continue
        cur_sum += arr[i]
        max_sum = max(max_sum, cur_sum) # get the maximum subsequence sum at the current element of the array, if the so far the current
                                        # subsequence sum is greater than the held maximum one, set the maximum to the new one. remember 
                                        # that several subsequence sum can be there (restarted all over again when current subsequence sum 
                                        # becomes negative)
    return max_sum, sum([i for i in arr if i > 0]) # the second one is the subarray which is the sum of all positive values
