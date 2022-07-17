import math
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
        dist = math.sqrt(abs(circles[i][0]-circles[j][0])**2 + abs(circles[i][1]-circles[j][1])**2)

        if abs(dist - circles[i][2]) <= circles[j][2] <= abs(dist + circles[i][2]) or abs(dist - circles[j][2]) <= circles[i][2] <= abs(dist + circles[j][2]):
            connection_matrix[i][j] = 1
            connection_matrix[j][i] = 1

path = shortest_path(np.array(connection_matrix), indices=[N-2,N-1])
if str(path[0][N-1]) == "inf":
    print("No")
else:
    print("Yes")