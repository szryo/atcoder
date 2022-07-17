import math

N,K = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]
light_pos=[]
for _ in range(N):
    light_pos.append([int(x) for x in input().split()])

not_light_pos = [x for x in range(1,N+1) if x not in A]

def r2(a,b):
    return math.sqrt(abs(a[0]-b[0])**2+abs(a[1]-b[1])**2)
distlist = [10**10] * len(not_light_pos)

for focus in A:
    for i,tar in enumerate(not_light_pos):
        if r2(light_pos[focus-1],light_pos[tar-1]) < distlist[i] :
            distlist[i] = r2(light_pos[focus-1],light_pos[tar-1])

print(max(distlist))
    

