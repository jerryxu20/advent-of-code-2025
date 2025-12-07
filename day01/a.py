import sys
from collections import defaultdict

cur = 50
ans = 0

for line in sys.stdin:
    x = int(line[1:])
    if line[0] == 'L':
        cur += x
    else:
        cur += x
    cur %= 100
    if cur == 0:
        ans += 1
print(ans)