import sys
from collections import defaultdict

mx = []
arr = [ ]
lines = []
for line in sys.stdin:
    lines.append(line.rstrip('\n'))

mx = [0 for _ in range(len(lines[0].split()))]
for line in lines:
    x = line.split()
    for i in range(len(x)):
        mx[i] = max(mx[i], len(x[i]))



for line in lines:

    idx = 0
    toks = []
    for x in mx:
        a = line[idx:idx+x]
        idx += x + 1
        toks.append(a)
    arr.append(toks)

ops = arr[-1]
arr.pop()

ans = 0
for j in range(len(arr[0])):
    
    nums = [0 for _ in range(mx[j])]
    for i in range(len(arr)):
        for k in range(mx[j]):
            if arr[i][j][k] == ' ': continue
            nums[k] *= 10
            nums[k] += int(arr[i][j][k])
    
    cont = nums[0]
    for i in range(1, len(nums)):
        if ops[j].strip() == '*':
            cont *= nums[i]
        else:
            cont += nums[i]
    ans += cont
print(ans)

