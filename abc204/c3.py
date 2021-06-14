import networkx  as nx

N,M = [int(x) for x in input().split()]

if M == 0:
    print(N)
    exit()

List = [0 for x in range(N)]

Record = []
    
for _ in range(M):
    A,B = [int(x) for x in input().split()]
    Record.append([A,B])
    List[A] += 1