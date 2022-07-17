import math
a,b,d = [int(x) for x in input().split()]

def getRD(x, y):
    r = math.sqrt(x**2+y**2)
    rad = math.atan2(y, x)
    degree = math.degrees(rad)
    return r, degree

def getXY(r, degree):
    # 度をラジアンに変換
    rad = math.radians(degree)
    x = r * math.cos(rad)
    y = r * math.sin(rad)
    return x, y

R,D = getRD(a,b)
x,y = getXY(R,(D+d))
print(x,y)