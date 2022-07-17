R,C = [int(x) for x in input().split()]

A1 = [int(x) for x in input().split()]
A2 = [int(x) for x in input().split()]

if R == 1:
    print(A1[C-1])
else:
    print(A2[C-1])