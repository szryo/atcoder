N,K = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]
B = [int(x) for x in input().split()]

def calcDiff(a1,a2,b1,b2):
    cur_nums = [0,0]
    cur_diff = 10**9 + 2
    ans = 0
    for firstnum in [a1,b1]:
        for secondnum in [a2,b2]:
            diff = abs(firstnum - secondnum)
            if diff < cur_diff:
                cur_diff = diff
                cur_nums = [firstnum, secondnum]
    return cur_diff, cur_nums[0], cur_nums[1]

if N == 1:
    print("Yes")
    exit()

# A.reverse()
# B.reverse()

cur_diff, cur_x1, cur_x2 = calcDiff(A[0], A[1],B[0],B[1])

before_x = cur_x2

if cur_diff > K:
    print("No")
    exit()

for i in range(N):
    if abs(A[i]-before_x) > abs(B[i]-before_x):
        current_x = B[i]
    else:
        current_x = A[i]

    if abs(current_x - before_x) > K:
        print("No")
        exit()
    
    before_x = current_x

print("Yes")