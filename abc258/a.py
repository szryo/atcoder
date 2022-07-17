#[int(x) for x in input().split()]
K = int(input())

if K >= 60:
    print(f"22:{str(K-60).zfill(2)}")
else:
    print(f"21:{str(K).zfill(2)}")