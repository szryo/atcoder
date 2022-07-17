N,K,Q = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]
L = [int(x) for x in input().split()]

for i in range(Q):
    if A[L[i]-1]+1 in A:
        pass
    elif A[L[i]-1] == N:
        pass
    else:
        A[L[i]-1] += 1

A.sort()

ans = ""

for a in A:
    ans += (str(a) + " ")

print(ans)