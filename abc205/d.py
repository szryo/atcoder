import numpy as np
from collections import Counter
import time
N,Q = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]

start = time.time()
A = np.array(A)
for _ in range(Q):
    K = int(input())
    sec1 = time.time()
    idx = 0
    idx = np.sum(A <= K)
    sec2 = time.time()
    origin = K+idx
    flag = 0
    src = K
    dst = K+idx
    sec3 = time.time()
    AC = Counter(A)
    sec4 = time.time()
    while True:
        #print("src:{},det:{}".format(src,dst))
        count = 0
        sec5 = time.time()
        for x in range(src+1,dst+1):
            if AC[x] != 0:
                count += 1
        sec6 = time.time()
        if count == 0:
            break
        else:
            src = dst
            dst = dst + count
            count = 0
    print(sec1,sec2,sec3,sec4,sec5,sec6)
    print(dst)