N,X = [int(x) for x in input().split()]

string = ""

for i in range(26):
    string += str(chr(65+i)) * N

print(string[X-1])