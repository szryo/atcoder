import networkx  as nx

N,M = [int(x) for x in input().split()]

if M == 0:
    print(N)
    exit()

Graph = nx.DiGraph()
for x in range(1,N):
    Graph.add_node(x)
for _ in range(M):
    A,B = [int(x) for x in input().split()]
    Graph.add_edge(A,B)

count = 0
#print(nx.shortest_path(Graph))
p))
