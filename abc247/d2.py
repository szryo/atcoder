import numpy as np

Q = int(input())

query = []

for _ in range(Q):
    q = input()
    query.append(q.split())

que = np.array([])

for i in range(Q):
    if query[i][0] == "1":
        x = int(query[i][1])
        c = int(query[i][2])
        que=np.append(que, [x,c])
        print(que)
    else:
        c = int(query[i][1])
        flag = 0
        ans = 0
        while flag == 0:
            if que[0][1] > c:
                ans += que[0][0]*c
                que[0][1] = int(que[0][1]) - c
                flag = 1
            else:
                ans += int(que[0][0])*int(que[0][1])
                c -= int(que[0][1])
                que = que[1:]
                if len(que) == 0:
                    break
        print(ans)
