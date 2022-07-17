import math
N,A,B = [int(x) for x in input().split()]

allsum = ((N+1)*N)//2

amax = N // A
bmax = N // B

lcm = (A*B)//math.gcd(A,B)
lcmmax = N // lcm

anum = ((A+(A*amax))*amax)//2
bnum = ((B+(B*bmax))*bmax)//2
lcmnum = ((lcm+(lcm*lcmmax))*lcmmax)//2

print(int(allsum-anum-bnum+lcmnum))