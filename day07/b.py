import sys
from collections import defaultdict

grid = [list(line.strip()) for line in sys.stdin]

ans = 0

dp = [[-1 for __ in range(len(grid[0]))] for _ in range(len(grid))]

def dfs(i, j):
    if i == len(grid) - 1: return 1
    if j < 0 or j >= len(grid[0]): return 0
   
    if dp[i][j] != -1: return dp[i][j]

    dp[i][j] = 0

    if i + 1 < len(grid) and grid[i + 1][j] == '^':
        dp[i][j] += dfs(i + 1, j - 1)
        dp[i][j] += dfs(i + 1, j + 1)
    elif i + 1 < len(grid):
        dp[i][j] += dfs(i + 1, j)
    return dp[i][j]

for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == 'S':
            print(dfs(i, j))

