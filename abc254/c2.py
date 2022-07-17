import numpy as np
import bisect

N,K = [int(x) for x in input().split()]

a = [int(x) for x in input().split()]

a.reverse()

print(a)

idx = 0
flag = 0
while True:
    maxidx = a.index(max(a))
    print(max(a),maxidx)
    if (maxidx) % K == idx:
        idx += 1
        if idx == K:
            idx = 0
        a[maxidx] = 0
    else:
        print("No")
        flag = 0
        break
if flag:
    print("Yes")