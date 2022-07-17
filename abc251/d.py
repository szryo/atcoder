import numpy as np

W = int(input())

ava_nums = set([1])
add_nums = [[1,1]]
sel_nums = [1]

remain = 299

cur_num = 2

while len(ava_nums) < W:
    #その数が再現できなければ追加　
    if cur_num not in ava_nums:
        print(cur_num, sel_nums)
        #追加する場合、その数で再現可能な数をavailable_numに追加
        #print(add_nums)
        new_add_nums = [[x+cur_num,y+1] for x,y in add_nums if y !=3]
        #print(new_add_nums)
        add_nums += new_add_nums 
        sel_nums.append(cur_num)
    
    cur_num += 1

print(sel_nums)