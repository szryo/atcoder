S = input()
T = input()

idxs = 0
idxt = 0

sli = [[S[0],1]]
tli =[[T[0],1]]

for i in range(1,max(len(S),len(T))):
        if i < len(S):
            if S[i] == S[i-1]:
                sli[-1][1] += 1
            else:
                sli.append([S[i],1])
        if i < len(T):
            if T[i] == T[i-1]:
                tli[-1][1] += 1
            else:
                tli.append([T[i],1])

if len(sli) != len(tli):
    print("No")
else:
    for i in range(len(sli)):
        if sli[i][0] != tli[i][0]:
            print("No")
            exit()
        elif sli[i][1] != tli[i][1] and (sli[i][1] > tli[i][1] or (sli[i][1]==1 or tli[i][1]==1)):
            print("No")
            exit()
        else:
            pass
    print("Yes")
            