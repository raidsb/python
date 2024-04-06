"""
You have an infinite number of 4 types of lego blocks of sizes given as (depth x height x width):

d	h	w
1	1	1
1	1	2
1	1	3
1	1	4

Using these blocks, you want to make a wall of height
and width

. Features of the wall are:

- The wall should not have any holes in it.
- The wall you build should be one solid structure, so there should not be a straight vertical break across all rows of bricks.
- The bricks must be laid horizontally.

How many ways can the wall be built?

Example


The height is and the width is

. Here are some configurations:

image 

https://www.hackerrank.com/challenges/one-month-preparation-kit-lego-blocks/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-month-preparation-kit&playlist_slugs%5B%5D=one-month-week-four 

"""

def legoBlocks(n, m):
    MOD = 1000000007
    # The number of combinations to build a single row
    # for m = 0 to 3
    combinations = [1, 1, 2, 4]
    # Each row is independent so the total combinations is
    # the number of combinations for one row power 'n'
    total = [1,1, 2**n, 4**n]
    # For m > 3, the total combinations is the sum of the
    # combinations for the last 4 widths:
    # Total combination for m - 1 by adding block width 1
    # Total combination for m - 2 by adding block width 2
    # Total combination for m - 3 by adding block width 3
    # Total combination for m - 4 by adding block width 4
    while len(combinations) <= m:
        c = sum(combinations[-4:]) % MOD
        combinations.append(c) # possible combinations for one row
        total.append(pow(c,n,MOD)) # possible combinations for 'n' rows
    
    # To find the number of unstable combinations in a wall size i,
    # we progressively split the wall into two parts, j and (i-j).
    # (the wall is unstable if it can be divided to two or more parts)
    # The total unstable combinations for wall size i is the sum of all
    # the stable combinations for size j, multiply by the total combinations
    # (stable and unstable) for size i-j for each j=1 to i-1.
    # For i=1, the stable combination = 1.
    stable =[0,1]
    for i in range(2, m+1):
        # unstable[i] = sum((stable[j]*total[i-j]) for j in range(1,i))
        # stable[i] = total[i] - unstable[i]
        stable.append(total[i] - sum((stable[j]*total[i-j]) for j in range(1,i)) % MOD)
        
    return stable[m] % MOD