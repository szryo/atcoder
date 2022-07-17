N = int(input())
S = input()
W = [int(x) for x in input().split()]

listS = [int(x) for x in list(S)]

target = sorted(list(zip(listS,W)), key = lambda x: x[1])

anslist = []
countdict = {}
adcount = 0
for i in range(N):
    if target[i][0] == 1:
        adcount += 1
        countdict[target[i][1]] = [i+1-adcount, adcount]
    else:
        countdict[target[i][1]] = [i+1-adcount, adcount]


adnum = list(countdict.values())[-1][1]
max = adnum
countlist = list(countdict.values())

for i in range(len(countlist)):
    if countlist[i][0] + adnum - countlist[i][1] > max:
        max = countlist[i][0] + adnum - countlist[i][1]

print(max)