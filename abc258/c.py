N,Q = [int(x) for x in input().split()]

s = input()

for _ in range(Q):
    n,x = [int(x) for x in input().split()]
    if n == 1:
        if x == N:
            pass
        else:
            tmp = s[-x:]
            s = tmp[::-1] + s[:-x]
    else:
        print(s[x-1])
