import networkx as nx
import math

N = int(input())
sx,sy,tx,ty = [int(x) for x in input().split()]

G = nx.Graph()

circles = []
for i in range(N):
    G.add_node(i)
    x,y,r = [int(x) for x in input().split()]
    circles.append([x,y,r])

connection_matrix = [[0 for i in range(N)] for i in range(N)]
for i in range(N-1):
    for j in range(i+1,N):
        dist = math.sqrt(abs(circles[i][0]-circles[j][0])**2 + abs(circles[i][1]-circles[j][1])**2)

        if abs(dist - circles[i][2]) <= circles[j][2] <= abs(dist + circles[i][2]) or abs(dist - circles[j][2]) <= circles[i][2] <= abs(dist + circles[j][2]):
            G.add_edges_from([(str(i),str(j))])
            connection_matrix[i][j] = 1
            connection_matrix[j][i] = 1

G.add_nodes_from(["s","t"])

for i in range(N):
    dists = math.sqrt(abs(circles[i][0]-sx)**2 + abs(circles[i][1]-sy)**2)
    distt = math.sqrt(abs(circles[i][0]-tx)**2 + abs(circles[i][1]-ty)**2)
    if dists == circles[i][2]:
        G.add_edge(str(i),"s")
    if distt == circles[i][2]:
        G.add_edge(str(i),"t")
try:
    a = nx.shortest_path(G, source="s", target="t")
    print("Yes")
except:
    print("No")