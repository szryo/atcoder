N,K = [int(x) for x in input().split()]

A = [int(x) for x in input().split()]
B = [int(x) for x in input().split()]

B = set(B)

flag = False

for _ in range(A.count(max(A))):
    idx = A.index(max(A))
    if idx+1 in B:
        flag = True
    A[idx] -= 1

if flag:
    print("Yes")
else:
    print("No")

