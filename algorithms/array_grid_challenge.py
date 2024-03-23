"""
Given a square grid of characters in the range ascii[a-z], rearrange elements of each row alphabetically, ascending. Determine if the columns are also in ascending alphabetical order, top to bottom. Return YES if they are or NO if they are not.

Example

The grid is illustrated below.

a b c
a d e
e f g
The rows are already in alphabetical order. The columns a a e, b d f and c e g are also in alphabetical order, so the answer would be YES. Only elements within the same row can be rearranged. They cannot be moved to a different row.

Function Description

Complete the gridChallenge function in the editor below.

gridChallenge has the following parameter(s):

string grid[n]: an array of strings
Returns

string: either YES or NO
"""

def gridChallenge(grid):
    new_grid = []
    for r in grid:
        r_list = list(r)
        r_list.sort()
        r_sorted = ''.join(r_list)
        new_grid.append(r_sorted)
    print(new_grid)
    in_order = 'YES'
    for j in range(len(new_grid[0])):
        for i in range(len(new_grid) - 1):
            print(j, i, i + 1)
            if ord(new_grid[i][j]) > ord(new_grid[i+1][j]):
                in_order = 'NO'
                break
    return in_order