import sys
from collections import defaultdict

grid = []
for line in sys.stdin:
    line = line.strip()
    grid.append(line)


n = len(grid)
m = len(grid[0])

ans = 0
delta = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
for i in range(n):
    for j in range(m):
        cnt = 0
        if grid[i][j] != '@': continue
        for a, b in delta:
            ii = i + a
            jj = j + b
            if ii < 0 or jj < 0 or ii >= n or jj >= m: continue
            if grid[ii][jj] == '@':
                cnt += 1
        if cnt < 4:
            ans += 1
print(ans)