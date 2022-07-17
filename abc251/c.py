N = int(input())

str_dict = {}
best_i = 0
best_t = 0
best_s = ""

for i in range(N):
    S,T = input().split()
    T = int(T)
    if str_dict.get(S):
        pass
    else:
        if T > best_t:
            best_i = i
            best_t = T
            best_s = S
        str_dict[S] = T

print(best_i+1)