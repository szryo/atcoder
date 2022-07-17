import copy

N,A,B = [int(x) for x in input().split()]

color = "."

ans = ""

firstcolor = "."

for _ in range(N):
   # for _ in range()
    color = copy.deepcopy(firstcolor)
    tmp = ""
    for _ in range(N):
        tmp = tmp + color*B
        if color == ".":
            color = "#"
        else:
            color = "."
    for _ in range(A):
        ans += tmp +"\n"
    if firstcolor == ".":
            firstcolor = "#"
    else:
        firstcolor = "."

print(ans)