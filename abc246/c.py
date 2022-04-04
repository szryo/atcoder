N,K,X = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]

from itertools import accumulate
import numpy as np

npA = np.array(A)
canusefull = npA//X
amari = npA%X

Kamari = K - sum(canusefull) if K >= sum(canusefull) else 0

if Kamari > len(A):
    print(0)
    exit()

samari = sorted(amari)
samari.reverse()
amariNum = sum(samari[:Kamari])

print(list(accumulate(A))[-1] - (X*(K-Kamari)+amariNum))