import numpy as np
import bisect

N,K = [int(x) for x in input().split()]

a = [int(x) for x in input().split()]

a.reverse()

flag = 0

maxnum = 10**9+1

for idx in range(len(a)-K):
    canswap = 1
    cur = np.array(a[idx+1:idx+K])

    if (sum(cur > a[idx]) != 0 and a[idx] > a[idx+K]) or a[idx] > maxnum: #
        print("No")
        flag = 1
        exit()
    elif a[idx] < a[idx+K]:
        tmp = a[idx]
        a[idx] = a[idx+K]
        a[idx+K] = tmp

    if a[idx] > maxnum:
        print("No")
        flag = 1
        exit()
    else:
        maxnum = a[idx]

if flag == 0:
    flag = 1
    remain = np.array(a[-K+1:])
    if sum(remain>maxnum) != 0:
        print("No")
        exit()
    for i in range(len(remain)-1):
        if remain[i] < remain[i+1]:
            print("No")
            flag = 0
            break
    
    if flag == 1:
        print("Yes")
    
