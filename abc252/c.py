N = int(input())

S = []

for i in range(N):
    tmp = list(input())
    tmp = [int(x) for x in tmp]
    S.append(tmp)

countS = {}

min_repeat_idx = [] #同じ位置であることが最も少ない数字
min_repeat_num = N #その時の最大のかぶり回数

min_repeat_numidx_list = []
min_repeat_numidx = 11 #数列の中の被りが発生している位置

for i in range(10):
    countS[i] = [0 for _ in range(10)]
    for n in range(N):
        countS[i][S[n].index(i)] += 1

    if max(countS[i]) < min_repeat_num:
        min_repeat_idx = [i]
        min_repeat_num = max(countS[i])

        rev_countS = list(reversed(countS[i]))
        min_repeat_numidx = (9-rev_countS.index(max(countS[i])))
        min_repeat_numidx_list = [min_repeat_numidx]
    elif max(countS[i]) == min_repeat_num:
        min_repeat_idx.append(i)

        rev_countS = list(reversed(countS[i]))
        min_repeat_numidx = (9-rev_countS.index(max(countS[i])))
        min_repeat_numidx_list.append(min_repeat_numidx)

print((10*((min_repeat_num)-1)+min(min_repeat_numidx_list)))
    


        
