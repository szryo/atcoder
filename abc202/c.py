N = int(input())
A = [int(x) for x in input().split()]
B = [int(x) for x in input().split()]
C = [int(x) for x in input().split()]

d = {x+1:0 for x in range(N)}
D = [B[x-1] for x in C]
for x in range(N):
    #d[x] = D.count(x)
    d[D[x]] += 1 
ans = [d[x] for x in A]

print(sum(ans))