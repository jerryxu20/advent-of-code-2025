import sys
s = input()
arr = s.split(',')

ans = 0
for x in arr:
    if not x: continue
    a, b = map(int, x.split('-'))

    for i in range(a, b + 1):
        t = str(i)
        if t[0:(len(t)//2)] * 2 == t:
            ans += i
print(ans)