N = int(input())
pos = []
P = []
for i in range(N):
    x,y,p = [int(x) for x in input().split()]
    pos.append([x,y])
    P.append(p)

nsdict = {}

import math

minnum = 10 ** 18
minidx = []

for i in range(N):
    tmp = []
    for j in range(N):
        if i == j:
            tmp.append(10**18)
        else:
            dist = math.sqrt(abs(pos[i][0] - pos[j][0])**2 + abs(pos[i][1] - pos[j][1])**2)
            ns = math.ceil(dist/P[j])
            if minnum == ns:
                minidx.append(i)
            elif minnum > ns:
                minidx = [i]
                minnum = ns
            tmp.append(ns)
    nsdict[i] = tmp

start = minidx[0]

alr = ([start])
print(nsdict)
curs = 0
canreach = nsdict[start]
print(start,canreach)
while alr != set(range(N)):
    next = canreach.index(min(canreach))
    if canreach[next] > curs:
        curs = canreach[next]
    alr.add(next)
    canreach[next] = 10**18
    
    canreach = canreach + nsdict[next]
