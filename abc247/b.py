from collections import Counter
import copy

N = int(input())
slist = []
tlist = []
ndict = {}
alist = []
used = []
flag = 0
for i in range(N):
    s,t = [x for x in input().split()]
    used.append(s)
    used.append(t)
    slist.append(s)
    tlist.append(t)
    ndict[s] = t

for i in range(N):
    if Counter(used)[slist[i]] >= 2 and Counter(used)[tlist[i]] >= 2 :
        if Counter(used)[slist[i]] == 2 and slist[i] == tlist[i]:
            pass
        else:
            print("No")
            exit()
print("Yes")




    
