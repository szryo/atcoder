import bisect
Q = int(input())

stack = {}

nums = []

for _ in range(Q):
    query = [int(x) for x in input().split()]
    if query[0] == 1:
        if stack.get(query[1]):
            stack[query[1]] += 1
        else:
            stack[query[1]] = 1
            bisect.insort_left(nums,query[1])

    elif query[0] == 2:
        if stack.get(query[1]):
            if stack[query[1]] > query[2]:
                stack[query[1]] -= query[2]
            else:
                del stack[query[1]]
                nums.pop(bisect.bisect_left(nums,query[1]))

        else:
            pass
    elif query[0] == 3:
        print(nums[-1]-nums[0])