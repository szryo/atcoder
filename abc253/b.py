H,W = [int(x) for x in input().split()]

S = []
ans_idx = []
for i in range(H):
    s = list(input())
    if s.count("o") == 2:
        idx1 = s.index("o")
        s = s[:idx1]+s[idx1+1:]
        idx2 = s.index("o")+1
        ans_idx.append([i,idx1])
        ans_idx.append([i,idx2])

    if "o" in s:
        idx = s.index("o")
        ans_idx.append([i,idx])

print(abs(ans_idx[0][0]-ans_idx[1][0]) + abs(ans_idx[0][1]-ans_idx[1][1]))
