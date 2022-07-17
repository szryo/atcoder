a,b,c = [int(x) for x in input().split()]

sortednum = sorted([a,b,c])

if sortednum[1] == b:
    print("Yes")
else:
    print("No")