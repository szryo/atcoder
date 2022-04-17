s = list(input())

s = [int(x) for x in s]

a = [0,1,2,3,4,5,6,7,8,9]

for x in a:
    if x not in s:
        print(x)