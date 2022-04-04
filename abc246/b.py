a,b = [int(x) for x in input().split()]

import math

l = math.sqrt(a**2+b**2)
print(l)
x,y = a/l, b/l

print(x,y)