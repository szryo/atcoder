#N = int(input())
A,B,C =[int(x) for x in input().split()]

if 0 in [A,B]:
    if A == 0 and B == 0:
        print("=")
        exit()
    if A == 0:
        if  C%2 == 0:
            print("<")
            exit()
        else:
            if B > 0:
                print("<")
                exit()
            else:
                print(">")
                exit()
    if B == 0:
        if  C%2 == 0:
            print(">")
            exit()
        else:
            if A > 0:
                print(">")
                exit()
            else:
                print("<")
                exit()

if C % 2 == 0:
    if A < 0:
        A = -A
    if B < 0:
        B = -B
    if A > B:
        print(">")
        exit()
    elif A < B:
        print("<")
        exit()
    else:
        print("=")
        exit()
else:
    if A < 0 and B < 0:
        if A > B:
            print(">")
            exit()
        elif A < B:
            print("<")
            exit()
        else:
            print("=")
            exit()
    elif A < 0 and B >= 0:
        print("<")
        exit()
    elif A >= 0 and B < 0:
        print(">")
        exit()
    else:
        if A > B:
            print(">")
            exit()
        elif A < B:
            print("<")
            exit()
        else:
            print("=")