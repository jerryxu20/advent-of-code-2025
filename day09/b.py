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

        x1, x2 = min(a, aa), max(a, aa)
        y1, y2 = min(b, bb), max(b, bb)

        valid = 1
        for p1, p2 in lines:
            sx, lx = min(p1[0], p2[0]), max(p1[0], p2[0])
            sy, ly = min(p1[1], p2[1]), max(p1[1], p2[1])
            if not (lx <= x1 or x2 <= sx or ly <= y1 or y2 <= sy)
                valid = 0
    
        if valid:
            ans = max(ans, (abs(a - aa) + 1) * (abs(b - bb) + 1))
print(ans)