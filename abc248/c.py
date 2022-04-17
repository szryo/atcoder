from itertools import combinations, combinations_with_replacement
from collections import Counter

N,M,K = [int(x) for x in input().split()]

availableNums = list(range(1,(M+1 if M<K else K+1)))

combs = list(combinations_with_replacement(availableNums,N))

count = 0

for comb in combs:
    if sum(comb) <= K:
        if len(list(Counter(comb).values())) == 1:
            count += 1
        else:
            count += 2

print(count/998244353)
