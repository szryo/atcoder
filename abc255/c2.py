import bisect

X,A,D,N = [int(x) for x in input().split()]

if D == 0:
    print(X-A)

elif D>0:
    numlist = list(range(A,A+D*N,D))
    idx_l = bisect.bisect_left(numlist,X)
    if X < A:
        print(abs(X-numlist[0]))
    elif X > A+D*N:
        print(abs(X-numlist[-1]))
    else:
        print(abs(numlist[idx_l] - X) < D/2)
        if abs(numlist[idx_l] - X) < D/2:
            print(abs(numlist[idx_l] - X)%D)
        else:
            print(D - (abs(numlist[idx_l] - X)%D))

else:
    numlist = list(range(A,A+D*N,D))
    idx_l = bisect.bisect_left(numlist,X)
    tmp = A
    A = A+D*N
    D = D*-1
    if X <= A:
        print(abs(X-numlist[0]))
    elif X >= A+D*N:
        print(abs(X-numlist[-1]))
    else:
        print(abs(numlist[idx_l] - X))
        print(abs(numlist[idx_l] - X) < abs(D)/2)
        if abs(numlist[idx_l] - X) < abs(D)/2:
            print(abs(numlist[idx_l] - X)%abs(D))
        else:
            print(D - (abs(numlist[idx_l] - X)%abs(D)))