N = [int(x) for x in input().split()]
ans = [6,5,4,3,2,1]
sum = 0
for x in N:
    sum += ans[x-1]
print(sum)