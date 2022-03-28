n = int(input())

if n == 1:
    print(1)
    exit()

tmp = n
import math
b = int(math.log(n,2))
while True:
    #print("b",b)
    if b == 1:
        #print("last",tmp)
        print(tmp)
        exit()
    a = n//(2**b)
    #print("a",a)
    c = n - ((2**b)*a)
    #print("c",c)
    if tmp > a+b+c and a*(2**b)+c == n:
        tmp = a+b+c
    #print('sum',a,b,c,a*(2**b)+c == n,a+b+c)
    b -= 1