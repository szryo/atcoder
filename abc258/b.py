N = int(input())
A = []
nA = []

for _ in range(N):
    tmp = [int(x) for x in list(input())]
    A.append(tmp)
    nA += tmp

maxN = max(nA)
maxIdx = [x for x,y in enumerate(nA) if y == maxN]


maxNum = []
for idx in maxIdx:
    row = idx//N
    col = idx%N
    print(row,col)

    if row != 0 and col != 0 and row != N-1 and col != 0:
        maxN2 = 0
        maxIdx2 = []
        for dif in [-(N+1), -N, -N+1, -1, 1, N-1, N, N+1]:
            if maxN2 < nA[idx+dif]:
                maxN2 = nA[idx+dif]
                maxIdx2 = [idx+dif]
            elif maxN2 == nA[idx+dif]:
                maxIdx2.append(idx+dif)
        print()