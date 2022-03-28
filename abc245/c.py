N,K = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]
B = [int(x) for x in input().split()]

if N == 1:
    print("Yes")
    exit()

if abs(max(A[-1],B[-1]) - min(A[-2],B[-2])) > abs(min(A[-1],B[-1]) - max(A[-2],B[-2])):
    tmp_x1 = min(A[-1],B[-1])
    tmp_x2 = max(A[-2],B[-2])
    
else:
    tmp_x1 = max(A[-1],B[-1])
    tmp_x2 = min(A[-2],B[-2])

if abs(tmp_x1 - tmp_x2) > K:
    print("No")
    exit()

before_x = tmp_x1

for i in reversed(range(N-2)):
    if abs(A[i]-X[-1]) > abs(B[i]-X[-1]):
        current_x = B[i]
    else:
        current_x = A[i]

    if abs(current_x - before_x) > K:
        print("No")
        exit()
    
    before_x = current_x

print("Yes")