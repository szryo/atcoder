N = int(input())
T = [int(x) for x in input().split()]
 
T.sort(reverse=True)
 
T = [0 for x in range(len(T))]

for t in range(len(T)):
    T[t] = 