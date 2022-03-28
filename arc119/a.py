N = int(input())
c=1
now = 10**18+1
while True:
    b = 0
    a = N - c
    while True:
        if a%2 == 0:
            a = a/2
            b+=1
            if a+b+c <= now:
                now = a+b+c
        else:
            break
            exit()
        print(b)
    c += 2
print(now)