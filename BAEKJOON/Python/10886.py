count = int(input())
good=[]
bad=[]
for i in range(count):
    a = int(input())
    if a == 0:
        bad.append(1)
    if a == 1:
        good.append(1)

if sum(bad) > sum(good):
    print("Junhee is not cute!")
elif sum(bad) < sum(good):
    print( "Junhee is cute!")