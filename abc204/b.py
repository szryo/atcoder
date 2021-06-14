N = int(input())
A = [int(x) for x in input().split()]

ans = 0
for x in A:
    if x <= 10:
        pass
    else:
        ans += x-10
print(ans)