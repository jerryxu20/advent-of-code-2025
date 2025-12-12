import sys
from collections import defaultdict
from scipy.optimize import milp
from scipy.optimize import LinearConstraint
import numpy as np
ans = 0
for line in sys.stdin:
    line = line.strip()
    arr = line.split()
    state = arr[0]
    buttons = arr[1:]
    config = buttons[-1]
    buttons.pop()
    targ = list(map(int, config[1:-1].split(',')))
   
    x = []
    cont = []
    for button in buttons:
        nums = list(map(int, button[1:-1].split(',')))
        cont.append(nums)

    c = np.array([1 for _ in range(len(cont))])

    A = [[0 for _ in range(len(cont))]  for _ in range(len(targ))]


    for i in range(len(cont)):
        for x in cont[i]:
            A[x][i] += 1
        
    A = np.array(A)
    b_l = targ
    b_u = targ

    constraints = LinearConstraint(A, b_l, b_u)
    integrality = np.ones_like(c)
    res = milp(c=c, constraints=constraints, integrality=integrality)

    ans += sum(res.x)
print(ans)