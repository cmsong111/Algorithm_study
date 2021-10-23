import math
size, x, y = map(int,input().split())

tempx = size**2 / (((y/x)**2)+1)
tempy = size**2 / (((x/y)**2)+1)

x = int(math.sqrt(tempx))
y = int(math.sqrt(tempy))

print(x,y)
