import math

A,B,K = [int(x) for x in input().split()]

num = A
count = 0

while B > num:
    num = num*K
    count += 1

print(count)