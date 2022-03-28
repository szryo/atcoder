a,b,c,d = [int(x) for x in input().split()]

if a < c:
    print("Takahashi")
elif a > c:
    print("Aoki")
else:
    if b <= d:
        print("Takahashi")
    elif b > d:
        print("Aoki") 