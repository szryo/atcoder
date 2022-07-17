X,A,D,N = [int(x) for x in input().split()]

if D > 0:
    if A < X < A+D*N:
        if abs(X-A)%D <= D//2:
            print(abs(X-A)%abs(D))
        else:
            print(abs(D - (abs((X-A))%abs(D))))
    elif X <= A:
        print(abs(A-X))
    else:
        print(abs(X-(A+(D*N))))
else:
    A2 = A+D*N
    D2 = D * -1
    if A2 < X < A2+D2*N:
        if abs(X-A2)%D2 <= D2//2:
            print(abs((X-A2))%abs(D2))
        else:
            print(abs(D2 - (abs((X-A2))%abs(D2))))
    elif X <= A2:
        print(abs(A2-X))
    else:
        print(abs(X-(A2+D2*N)))