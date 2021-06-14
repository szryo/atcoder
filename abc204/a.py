x,y = [int(x) for x in input().split()]

if x == y:
    print(x)
else:
    a = [x,y]
    if 0 not in a:
        print(0)
    elif 1 not in a:
        print(1)
    else:
        print(2)