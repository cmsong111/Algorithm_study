num = set(range(1,10001))
rmv = set()
for i in range(1,10001):
    for j in str(i):
        i += int(j)
    rmv.add(i)
num = num - rmv
for k in sorted(num):
    print(k)