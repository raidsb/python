"""
Sherlock considers a string to be valid if all characters of the string appear the same number of times. It is also valid if he can remove just character at index in the string, and the remaining characters will occur the same number of times. Given a string

, determine if it is valid. If so, return YES, otherwise return NO.

Example
This is a valid string because frequencies are

.

This is a valid string because we can remove one and have

of each character in the remaining string.

This string is not valid as we can only remove occurrence of . That leaves character frequencies of

.

Function Description

Complete the isValid function in the editor below.

isValid has the following parameter(s):

    string s: a string

Returns

    string: either YES or NO

https://www.hackerrank.com/challenges/one-month-preparation-kit-sherlock-and-valid-string/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-month-preparation-kit&playlist_slugs%5B%5D=one-month-week-three 
"""
def isValid(s):
    counts = []
    while s != '':
        print(s[0], s.count(s[0]))
        counts.append(s.count(s[0]))
        s = ''.join([c for c in s if c != s[0]])
        print(s)
    print(counts)
    max_count = max(counts)
    min_count = min(counts)
    max_counts = counts.count(max_count)
    min_counts = counts.count(min_count)
    
    # case counts example [3, 3, 3, 4, 5]
    if len(set(counts)) > 2:
        return 'NO'
    if len(counts) == 1:
        print('yes1')
        return 'YES'
    if max_count == min_count:
        print('yes2')
        return 'YES'
    if max_counts == 1 and min_counts > 1 and max_count - min_count == 1:
        print('yes3')
        return 'YES'
    if max_counts > 1 and min_counts == 1 and min_count == 1:
        print('yes4')
        return 'YES'
    if max_count - min_count != 1:
        return 'NO'
    
    return 'NO'