import sys
from collections import defaultdict

adj = defaultdict(list)

for line in sys.stdin:
    a, out = line.split(':')
    for nxt in out.split():
        adj[a].append(nxt)
        adj[nxt]

seen = defaultdict(int)
order = []

def dfs(node):
    seen[node] = 1
    for nxt in adj[node]:
        if seen[nxt] == 2:
            continue
        dfs(nxt)
    seen[node] = 2
    order.append(node)

for node in adj:
    if node not in seen:
        dfs(node)

print(order)
order = order[::-1]

dp = defaultdict(int)
dac = defaultdict(int)
fft = defaultdict(int)
both = defaultdict(int)

dp["svr"] = 1

print(order)
for node in order:
    if node == "fft":
        fft[node] = dp[node]
        both[node] = dac[node]
    if node == "dac":
        dac[node] = dp[node]
        both[node] = fft[node]    

    for nxt in adj[node]:
        dp[nxt] += dp[node]
        dac[nxt] += dac[node]
        fft[nxt] += fft[node]
        both[nxt] += both[node]

print(both["out"])