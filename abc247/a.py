S = input()
S = list(S)

ans = "0"

for i in range(len(S)-1):
    if S[i] == "0":
        ans = ans + "0"
    else:
        ans = ans + "1"

print(ans)