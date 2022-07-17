N,Q = [int(x) for x in input().split()]

s = input()

curx = 0
for _ in range(Q):
    n,x = [int(x) for x in input().split()]
    if n == 1:
        if x == N:
            pass
        else:
            curx = (curx + x)%N
    else:
        if x < curx:
            print(s[-(curx-x)-1])
        else:
            print(s[x-curx-1])
