N = int(input())
sosu = []

lim = int(pow((N/2),(1/3)))+1

for i in range(2, lim+1):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        sosu.append(i)

count = 0

flag = 0

for i in range(len(sosu)):
    for j in reversed(range(i+1,len(sosu))):
        if sosu[i] * (sosu[j]**3) <= N:
            count += j-i
            if j == i+1:
                print(count)
                exit()
            break
        else:
            continue
print(count)
