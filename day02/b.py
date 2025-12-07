import sys
s = input()
arr = s.split(',')

ans = 0
for x in arr:
    if not x: continue
    a, b = map(int, x.split('-'))

    for i in range(a, b + 1):
        t = str(i)
        for j in range(1, len(t)):
            if len(t) % j == 0 and t[0:j] * (len(t)//j) == t:
                ans += i
                break
print(ans)