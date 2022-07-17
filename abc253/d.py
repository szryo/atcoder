import math
 
 
n, a, b = map(int, input().split())
 
SUM = (n*(n+1)) // 2
 
ba =(a * b) // math.gcd(a, b)
 
 
aa = n // a
bb = n // b
 
ab = n //  ba
 
saa = (aa*(aa+1)) // 2
sbb = (bb*(bb+1)) // 2
sab = (ab*(ab+1)) // 2


 
SUM -= a*saa
SUM -= b*sbb
SUM += ba*sab
 
print(int(SUM))