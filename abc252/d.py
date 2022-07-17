import collections

N = int(input())
A = [int(x) for x in input().split()]

larger_nums_count = []

count = 0

for i in range(1,N-1):
    left = A[:i]
    right = A[i+1:]
    sleft = set(left)
    sright = set(right)
    sleft.discard(A[i])
    sright.discard(A[i])

    differencel = sleft-sright
    differencer = sright-sleft

    cl = collections.Counter(left)
    cr = collections.Counter(right)

    diflnum = 0
    difrnum = 0
    for num in differencel:
        diflnum += cl[num]
    
    for num in differencer:
        difrnum += cr[num]

    union = sleft.intersection(sleft,sright)

    uninuml = 0
    uninumr = 0

    for num in union:
        uninuml += cl[num]
        uninumr += cr[num]

    count += diflnum*difrnum
    count += diflnum*uninumr
    count += uninuml*difrnum
    
print(count)

