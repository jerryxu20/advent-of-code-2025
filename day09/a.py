import sys

pts = []
for line in sys.stdin:
    a, b = map(int, line.strip().split(','))
    pts.append((a, b))


lines = []
for i in range(len(pts)):
    lines.append((pts[i], pts[(i + 1) % len(pts)]))


ans = 0
for a, b in pts:
    for aa, bb in pts:
        ans = max(ans, (abs(a - aa) + 1) * (abs(b - bb) + 1))
print(ans)