x1 = int(input())
x2 = int(input())
x3 = int(input())
x4 = int(input())
x5 = int(input())

if x1 < 40:
    x1 = 40
if x2 < 40:
    x2 = 40
if x3 < 40:
    x3 = 40
if x4 < 40:
    x4 = 40
if x5 < 40:
    x5 = 40
    
sum = (x1+x2+x3+x4+x5)
avg = int(sum/5)


print(avg)