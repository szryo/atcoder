from collections import Counter
import bisect

N = int(input())
A = [int(x) for x in input().split()]
Q = int(input())
Query = []

dict = {}
for i in range(N):
    if dict.get(A[i]):
        dict[A[i]].append(i+1)
    else:
        dict[A[i]] = [i+1]

for _ in range(Q):
    L,R,X = [int(x) for x in input().split()]
    Query.append([L,R,X])

for i in range(Q):
    L,R,X = Query[i]
    if dict.get(X):
        left = bisect.bisect_left(dict[X],L)
        right = bisect.bisect_right(dict[X],R)
        print((right-left))
    else:
        print(0)