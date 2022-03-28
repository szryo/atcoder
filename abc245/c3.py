N,K = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]
B = [int(x) for x in input().split()]

if N == 1:
    print("Yes")
    exit()

#最初の2つの数字を決定する
possible_nums = set()
for firstnum in [A[0],B[0]]:
    for secondnum in [A[1],B[1]]:
        diff = abs(firstnum - secondnum)
        if diff < K:
            possible_nums.add(secondnum)

#それ以降の数字を決定していく
for i in range(2,N):
    next_nums = set()
    for before_x in possible_nums:
        if abs(A[i] - before_x) <= K:
            next_nums.add(A[i])
        if abs(B[i] - before_x) <= K:
            next_nums.add(B[i])
    if len(next_nums) == 0:
        print("No")
        exit()
    possible_nums = next_nums
print("Yes")
    
    