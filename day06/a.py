import sys
from collections import defaultdict

arr = [ ]
for line in sys.stdin:
    arr.append(line.split())
    
ops = arr[-1]
arr.pop()

res = list(map(int, arr[-1]))
arr.pop()


for nums in arr:
    for i in range(len(nums)):
        if ops[i] == '*':
            res[i] *= int(nums[i])
        else:
            res[i] += int(nums[i])

for j in range(len(arr[0])):
    for i in range(len(arr)):
