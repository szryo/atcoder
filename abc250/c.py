N,Q = [int(x) for x in input().split()]

numL = list((range(1,N+1)))
idxL = list((range(0,N)))

for i in range(Q):
    x = int(input())
    idx = idxL[x-1]
    if idx == N-1:
        idxL[numL[idx]-1] -= 1
        idxL[numL[idx-1]-1] += 1
        tmp = numL[idx]
        numL[idx] = numL[idx-1]
        numL[idx-1] = tmp
    else:
        idxL[numL[idx]-1] += 1
        idxL[numL[idx+1]-1] -= 1
        tmp = numL[idx]
        numL[idx] = numL[idx+1]
        numL[idx+1] = tmp
        
print("".join([str(x)+" " for x in numL]))
