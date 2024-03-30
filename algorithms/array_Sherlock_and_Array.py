"""
Watson gives Sherlock an array of integers. His challenge is to find an element of the array such that the sum of all elements to the left is equal to the sum of all elements to the right.

Example


is between two subarrays that sum to .


The answer is  since left and right sum to .

You will be given arrays of integers and must determine whether there is an element that meets the criterion. If there is, return YES. Otherwise, return NO.

Function Description

Complete the balancedSums function in the editor below.

balancedSums has the following parameter(s):

int arr[n]: an array of integers
Returns

string: either YES or NO
Input Format

The first line contains , the number of test cases.

The next  pairs of lines each represent a test case.
- The first line contains , the number of elements in the array .
- The second line contains  space-separated integers  where .
"""

def balancedSums_exceeds_time_limit(arr):
    for i in range(len(arr)):
        sectional_arr_left = []
        if i == 0:
            sectional_arr_left = []
        elif i == 1:
            sectional_arr_left = [arr[0]]
        else:
            sectional_arr_left = arr[0: i]
        
        sectional_arr_right = []
        if i == len(arr) - 1:
            sectional_arr_right = []
        elif i == len(arr) - 1 - 1:
            sectional_arr_right = [arr[len(arr) - 1]]
        else:
            sectional_arr_right = arr[i+1: len(arr)]
        
        if sum(sectional_arr_left) == sum(sectional_arr_right):
            return "YES"
    return "NO"

def balancedSums2(arr):
    for i in range(len(arr)):
        sectional_left_sum = 0
        if i == 0:
            sectional_left_sum = 0
        elif i == 1:
            sectional_left_sum = arr[0]
        else:
            sectional_left_sum = sum(arr[0: i])
        
        sectional_right_sum = 0
        if i == len(arr) - 1:
            sectional_right_sum = 0
        elif i == len(arr) - 1 - 1:
            sectional_right_sum = arr[len(arr) - 1]
        else:
            sectional_right_sum = sum(arr[i+1: len(arr)])
        
        if sectional_left_sum == sectional_right_sum:
            return "YES"
    return "NO"

def balancedSums(arr):
    total_sum = sum(arr)
    right_sum = total_sum - arr[0]
    left_sum = 0
    arr_idx = 0
    
    while True:
        print(left_sum, right_sum)
        if left_sum == right_sum:
            return "YES"
        arr_idx += 1
        if arr_idx == len(arr):
            return "NO"
        right_sum = right_sum - arr[arr_idx]
        left_sum = left_sum + arr[arr_idx - 1]