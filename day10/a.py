import sys
from collections import defaultdict

ans = 0
for line in sys.stdin:
    line = line.strip()
    arr = line.split()
    state = arr[0]
    buttons = arr[1:]
    buttons.pop()
    
    mask = 0
    for i in range(1, len(state) - 1):
        if state[i] == '#': mask |= (1 << (i - 1))
    
    x = []
    for button in buttons:
        nums = list(map(int, button[1:-1].split(',')))
        val = 0
        for num in nums:
            val |= (1 << (num))
        x.append(val)
    dp = [100 for _ in range(1 << 10)]
    dp[0] = 0

    print(x)
    for val in x:
        dp2 = [100 for _ in range(1 << 10)]
        dp2[val] = 1
        for i in range(1 << 10):
            dp2[i ^ val] = min(dp2[i ^ val], 1 + dp[i])
        
        for i in range(1 << 10):
            dp[i] = min(dp[i], dp2[i])
    ans += dp[mask]
print(ans)