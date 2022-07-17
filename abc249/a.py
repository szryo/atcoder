A,B,C,D,E,F,X = [int(x) for x in input().split()]

taka1 = X//(A+C)
takaamari = X%(A+C)
aoki1 = X//(D+F)
aoamari = X%(D+F)

takaD = A*B*taka1 + B*(A if A < takaamari else takaamari)
aokiD = D*E*aoki1 + E*(D if D < aoamari else aoamari)
if takaD == aokiD:
    print("Draw")
elif takaD > aokiD:
    print("Takahashi")
else:
    print("Aoki")