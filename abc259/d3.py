import numpy as np
from scipy.sparse.csgraph import shortest_path
N = int(input())
sx,sy,tx,ty = [int(x) for x in input().split()]

circles = []
for i in range(N):
    x,y,r = [int(x) for x in input().split()]
    circles.append([x,y,r])

N += 2
circles.append([sx,sy,0])
circles.append([tx,ty,0])

connection_matrix = [[0 for i in range(N)] for i in range(N)]
for i in range(N-1):
    for j in range(i+1,N):
        dist = (circles[i][0]-circles[j][0])**2 + (circles[i][1]-circles[j][1])**2

        if dist > (circles[i][2] - circles[j][2])**2 or dist < (circles[i][2] + circles[j][2])**2:
            connection_matrix[i][j] = 1
            connection_matrix[j][i] = 1

done = set()
stack = []
cur = N-1


    
    
if dfs(connection_matrix, N-2):
    print("Yes")
else:
    print("No")