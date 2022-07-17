H,W = [int(x) for x in input().split()]

R,C = [int(x) for x in input().split()]

def check(a,b,c,d):
    if abs(a-c)+abs(b-d) == 1:
        return True
    else:
        return False

count = 0

for x in range(1,H+1):
    for y in range(1,W+1):
        if check(R,C,x,y):
            count += 1

print(count)