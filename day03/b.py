import sys
from collections import defaultdict

ans = 0
for line in sys.stdin:
    line = line.strip()

    mx = [0 for _ in range(12)]
    for i in range(len(line)):
        for j in range(11, 0, -1):
            mx[j] = max(mx[j], mx[j - 1] * 10 + int(line[i]))
        mx[0] = max(mx[0], int(line[i]))
    ans += mx[11]
print(ans)