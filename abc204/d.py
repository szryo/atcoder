N = int(input())
T = [int(x) for x in input().split()]
 
T.sort(reverse=True)
 
A,B = 0,0
 
for x in T:
    if x+A > x+B:
        B = x+B
    else:
        A = x+A
    #print(A,B)
if A >= B:
    print(A)
else:
    print(B)