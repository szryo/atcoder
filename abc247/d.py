Q = int(input())

query = []

for _ in range(Q):
    q = input()
    query.append(q.split())

que = []

for i in range(Q):
    if query[i][0] == "1":
        x = int(query[i][1])
        c = int(query[i][2])
        if len(que) != 0 and que[-1][0] == x:
            que[-1][1] += c
        else:
            que.append([x,c])
    else:
        c = int(query[i][1])
        flag = 0
        ans = 0
        while flag == 0:
            if que[0][1] > c:
                ans += que[0][0]*c
                que[0][1] = que[0][1] - c
                flag = 1
            else:
                ans += que[0][0]*que[0][1]
                c -= que[0][1]
                que.pop(0)
                if len(que) == 0:
                    break
        print(ans)
