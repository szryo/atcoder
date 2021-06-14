N = int(input())
A =[int(x) for x in input().split()]

for x in range(1,N+1):
    if A.count(x) != 1:
        print("No")
        exit()
print("Yes")