N = int(input())
A = [int(x) for x in input().split()]

A.sort()

if A[0] != 0:
    print(0)
else:
    for i in range(1,len(A)):
        if (A[i] != A[i-1]+1) and (A[i] != A[i-1]):
            print(A[i-1]+1)
            exit()
    print(A[-1]+1)
    