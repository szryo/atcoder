N = int(input())

s = {1:"1"}

if N == 1:
    print("1")
    exit()

for i in range(2,N+1):
    s[i] = s[i-1] + " " + str(i) + " " + s[i-1]

print(s[i])
