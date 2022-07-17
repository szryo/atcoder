N = int(input())

if N == 1:
    print("1")

else:
    ans = [[1]]
    before = [1]
    cur = [1]
    for i in range(1,N):
        cur = [1]
        for idx in range(len(before)-1):
            cur.append(before[idx]+before[idx+1])
        cur.append(1)
        ans.append(cur)
        before = cur

    for i in ans:
        print("".join([str(s)+" " for s in i]))