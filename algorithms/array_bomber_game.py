"""
Bomberman lives in a rectangular grid. Each cell in the grid either contains a bomb or nothing at all.

Each bomb can be planted in any cell of the grid but once planted, it will detonate after exactly 3 seconds. Once a bomb detonates, it's destroyed — along with anything in its four neighboring cells. This means that if a bomb detonates in cell
, any valid cells and

are cleared. If there is a bomb in a neighboring cell, the neighboring bomb is destroyed without detonating, so there's no chain reaction.

Bomberman is immune to bombs, so he can move freely throughout the grid. Here's what he does:

    Initially, Bomberman arbitrarily plants bombs in some of the cells, the initial state.
    After one second, Bomberman does nothing.
    After one more second, Bomberman plants bombs in all cells without bombs, thus filling the whole grid with bombs. No bombs detonate at this point.
    After one more second, any bombs planted exactly three seconds ago will detonate. Here, Bomberman stands back and observes.
    Bomberman then repeats steps 3 and 4 indefinitely.


https://www.hackerrank.com/challenges/one-month-preparation-kit-bomber-man/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-month-preparation-kit&playlist_slugs%5B%5D=one-month-week-three 
"""

def bomberMan(n, grid):
    # 1     2.    3
    # ....  xxxx  .x.x
    # o.o.  oxox  ....
    # .o..  xoxx  ...x
    
    # 4     5     6     7
    # oxox  ....  xxxx  Back to 3
    # oooo  o.o.  oxox
    # ooox  oo..  ooxx
    
    r, c = len(grid), len(grid[0])
    if n == 1:
        return grid
    elif n % 2 == 0:
        return ['O' * c] * r
    elif n % 4 == 3:
        # 1st-bomb pattern
        return detonate(grid)
    else:
        # 2nd-bomb pattern
        return detonate(detonate(grid))


def detonate(grid: List[str]) -> List[str]:
    m, n = len(grid), len(grid[0])
    g = [['O'] * n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            if grid[i][j] == '.':
                continue
            g[i][j] = '.'
            for ii, jj in ((i-1, j), (i+1, j), (i, j-1), (i, j+1)):
                if 0 <= ii < m and 0 <= jj < n:
                    g[ii][jj] = '.'
    return [''.join(row) for row in g]
                    