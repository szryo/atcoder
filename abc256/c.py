h1,h2,h3,w1,w2,w3 = [int(x) for x in input().split()]

N = max([h1,h2,h3,w1,w2,w3])

count = 0

for n11 in range(1,N):
    for n12 in range(1,N):
        for n21 in range(1,N):
            for n22 in range(1,N):
                n13 = h1 - n11 - n12
                n23 = h2 - n21 - n22
                n31 = w1 - n11 - n21
                n32 = w2 - n12 - n22
                n33h = h3 - n31 - n32
                n33w = w3 - n13 - n23
                if n13 > 0 and n23 > 0 and n31 > 0 and n32 > 0 and n33h == n33w and n33h > 0:
                    count += 1

print(count)