a,b = [int(x) for x in input().split()]
c,d = [int(x) for x in input().split()]
e,f = [int(x) for x in input().split()]

if a==c:
    if f == b:
        print(e,d)
    else:
        print(e,b)
elif a==e:
    if d == b:
        print(c,f)
    else:
        print(c,b)
else:
    if b == d:
        print(a,f)
    else:
        print(a,d)