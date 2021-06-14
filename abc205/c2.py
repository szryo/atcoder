#N = int(input())
A,B,C =[int(x) for x in input().split()]

if C % 2 == 0:
    if A < 0:
        A = -A
    if B < 0:
        B = -B
    tmp1 = A**C
    tmp2 = B**C
    if tmp1 > tmp2:
        print(">")
    elif tmp1 == tmp2:
        print("=")
    else:
        print("<")
else:
    tmp1 = A**C
    tmp2 = B**C
    if tmp1 > tmp2:
        print(">")
    elif tmp1 == tmp2:
        print("=")
    else:
        print("<")