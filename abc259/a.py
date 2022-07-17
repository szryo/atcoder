# [int(x) for x in input().split()]
N,M,X,T,D = [int(x) for x in input().split()]

if N >= M >= X:
    print(T)
else:
    print(T-(X-M)*D)