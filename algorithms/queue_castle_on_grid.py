"""
You are given a square grid with some cells open (.) and some blocked (X). Your playing piece can move along any row or column until it reaches the edge of the grid or a blocked cell. Given a grid, a start and a goal, determine the minmum number of moves to get to the goal.

Example.

The grid is shown below:

...
.X.
...

The starting position
so start in the top left corner. The goal is . The path is . It takes

moves to reach the goal.

Function Description
Complete the minimumMoves function in the editor.

minimumMoves has the following parameter(s):

    string grid[n]: an array of strings that represent the rows of the grid
    int startX: starting X coordinate
    int startY: starting Y coordinate
    int goalX: ending X coordinate
    int goalY: ending Y coordinate

Returns

    int: the minimum moves to reach the goal

Input Format

The first line contains an integer
, the size of the array grid.
Each of the next lines contains a string of length .
The last line contains four space-separated integer

https://www.hackerrank.com/challenges/one-month-preparation-kit-castle-on-the-grid/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-month-preparation-kit&playlist_slugs%5B%5D=one-month-week-four 
"""

def minimumMoves(grid, startX, startY, goalX, goalY):
    # Write your code here
    N = len(grid)
    
    # start traversing with the starting cell
    q = [[startX, startY]]
    
    # Keep track of the visited cells so far. We need this because every cell has 4 nerighbouring cells and any of them can be already visited.
    # if a cell is already visited, then no need to visit again.
    visit = set()
    
    # counter of moves so far. Important: steps on the same row or on the same col counted as one step regardless of how many cell2cell transition.
    moves = 0
    while q:
        moves += 1
        # len(q) does not change in the loop even if more cells added later in the Q in the loop. This garantees that cells on the same graph level
        # (and only cells on the same graph level) are explored.
        for i in range(len(q)):
            arr = q.pop(0)
            x, y = arr[0], arr[1]
            # these are the coordinates of the neighbouring cells.
            for d in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                newX, newY = x, y
                # the while loop will keep traversing cells on the same row or the same col depending on the coordinates used is d.
                while True:
                    # Keep on the same row or col path
                    newX += d[0]
                    newY += d[1]
                    
                    # Reached the borders of the grid or a block 'X' means that the current same row/col path is finished and need to change to another path,
                    # so exit the while loop.
                    if newX not in range(0, N) or newY not in range(0, N) or grid[newX][newY] == 'X':
                        break # while
                    
                    # if otherwise reached the goal cell return the current number of moves.
                    if newX == goalX and newY == goalY:
                        return moves
                    # if not, then check if not visited and add to queue.
                    elif (newX, newY) not in visit:
                        visit.add((newX, newY))
                        q.append([newX, newY])
    return -1
        