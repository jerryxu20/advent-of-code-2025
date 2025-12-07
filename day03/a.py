import sys
from collections import defaultdict

ans = 0
for line in sys.stdin:
    line = line.strip()

    mx = 0
    for i in range(len(line)):
        for j in range(i + 1, len(line)):
            mx = max(mx, int(line[i]) * 10 + int(line[j]))  
    ans += mx
print(ans)