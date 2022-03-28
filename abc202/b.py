S = input()
S = [int(x) for x in S]

S.reverse()

tmp = []
for x in S:
    if x == 6:
        tmp.append(9)
    elif x == 9:
        tmp.append(6)
    else:
        tmp.append(x)

ans = ""
for x in tmp:
    ans += str(x)
print(ans)
