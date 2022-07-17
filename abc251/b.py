import bisect
import math
import itertools

H,W = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]

count = 0
already = set()

for n in range(1,4):
    for comb in itertools.combinations(A,n):
        if sum(comb) <= W and sum(comb) not in already:
           count += 1
           already.add(sum(comb))

print(count) 
    