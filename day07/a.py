import sys
from collections import defaultdict

grid = [list(line.strip()) for line in sys.stdin]

ans = 0

seen = [[0 for __ in range(len(grid[0]))] for _ in range(len(grid))]

def dfs(i, j):
    global ans
    if i == len(grid): return
    if j < 0 or j >= len(grid[0]): return
    if seen[i][j]: return

    seen[i][j] = 1

    if i + 1 < len(grid) and grid[i + 1][j] == '^':
        dfs(i + 1, j - 1)
        dfs(i + 1, j + 1)
        ans += 1
    elif i + 1 < len(grid):
        dfs(i + 1, j)


for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == 'S':
            dfs(i, j)


print(ans)    
