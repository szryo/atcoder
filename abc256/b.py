N = int(input())

A = [int(x) for x in input().split()]

for i in range(len(A)):
    A[i] += sum(A[i+1:])

print(len([x for x in A if x > 3]))
    