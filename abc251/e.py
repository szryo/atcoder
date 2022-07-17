score = list()
n = int(input())
count = 0
while count < n:
	s = int(input())
	if s < 0:
		continue
	score.append(s)
	count = count + 1
print(sum(score)/count)