import sys
from collections import defaultdict

cur = 50
ans = 0

for line in sys.stdin:
    x = int(line[1:])
    if line[0] == 'L':
        for _ in range(x):
            cur -= 1
            cur %= 100
            if cur == 0:
                ans += 1
    else:
        for _ in range(x):
            cur += 1
            cur %= 100
            if cur == 0:
                ans += 1
print(ans)