import sys
from collections import defaultdict

ints = []
for line in sys.stdin:
    line = line.strip()
    if not line: break
    a, b = map(int, line.split('-'))
    ints.append((a, b))
print(ints)


ans = 0
for x in sys.stdin:
    for a, b in ints:
        if int(x) >= a and int(x) <= b:
            ans += 1
            break
print(ans)