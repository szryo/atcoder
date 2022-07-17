N,X = [int(x) for x in input().split()]

ABn = []
needReach = 0

for i in range(N):
    A,B = [int(x) for x in input().split()]
    ABn.append([A,B,needReach])
    needReach += A + B

ans = ABn[0][0]+ABn[0][1]*X
for i,abn in enumerate(ABn[1:]):
    if i < X:
        A,B,N = abn
        if ans > N+A+B*(X-(i+1)):
            ans = N+A+B*(X-(i+1))
    else:
        break
print(ans)