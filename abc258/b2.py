N = int(input())
A = []
nA = []

for _ in range(N):
    tmp = [int(x) for x in list(input())]
    A.append(tmp)

maxN = 0
for i in range(N):
    for j in range(N):
        c = 0
        tmp = []
        while c < N:
            tmp.append(str(A[i][(j+c)%N]))
            c += 1
        if int("".join(tmp)) > maxN:
            maxN = int("".join(tmp))

        c = 0
        tmp = []
        while c < N:
            z = j-c if j-c > 0 else N-abs(j-c)
            tmp.append(str(A[i][(z)%N]))
            c += 1
        if int("".join(tmp)) > maxN:
            maxN = int("".join(tmp))

        c = 0
        tmp = []
        while c < N:
            tmp.append(str(A[(i+c)%N][j]))
            c += 1
        if int("".join(tmp)) > maxN:
            maxN = int("".join(tmp))

        c = 0
        tmp = []
        while c < N:
            z = i-c if i-c > 0 else N-abs(i-c)
            tmp.append(str(A[(z)%N][j]))
            c += 1
        if int("".join(tmp)) > maxN:
            maxN = int("".join(tmp))
        
        c = 0
        tmp = []
        while c < N:
            tmp.append(str(A[(i+c)%N][(j+c)%N]))
            c += 1
        if int("".join(tmp)) > maxN:
            maxN = int("".join(tmp))

        c = 0
        tmp = []
        while c < N:
            z = i-c if i-c > 0 else N-abs(i-c)
            r = j-c if j-c > 0 else N-abs(j-c)
            tmp.append(str(A[(z)%N][(r)%N]))
            c += 1
        if int("".join(tmp)) > maxN:
            maxN = int("".join(tmp))

        c = 0
        tmp = []
        while c < N:
            z = i-c if i-c > 0 else N-abs(i-c)
            tmp.append(str(A[(z)%N][(j+c)%N]))
            c += 1
        if int("".join(tmp)) > maxN:
            maxN = int("".join(tmp))
        
        c = 0
        tmp = []
        while c < N:
            r = j-c if j-c > 0 else N-abs(j-c)
            tmp.append(str(A[(i+c)%N][(r)%N]))
            c += 1
        if int("".join(tmp)) > maxN:
            maxN = int("".join(tmp))

print(maxN)